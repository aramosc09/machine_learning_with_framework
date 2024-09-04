from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import AIMessage, HumanMessage
from operator import itemgetter

class ChatBot:
    def __init__(self, api, language='English'):
        """
        Init chatbot with prompt, model, trimmer and streaming config.
        
        Args:
        - prompt: System prompt given to the model at each Human message.
        - model: model in charge of returning an answer to user.
        - trimmer: To process each message. This avoids message to be too long for the model to answer.
        - config: To get session id.
        """
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant expert in data analysis. Answer all questions to the best of your ability in {language}.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        try:
            self.model = ChatOpenAI(model="gpt-4o-mini",openai_api_key=api)
        except Exception as e:
            print(e)

        self.trimmer = trim_messages(
            max_tokens=1000,
            strategy="last",
            token_counter=self.model,
            include_system=True,
            allow_partial=False,
            start_on="human",
        )
        self.messages = []  # to save history
        self.config = {"configurable": {"session_id": "abc1"}}
        self.language = language
    
    def add_message(self, content, is_human=True):
        """
        Adds a Human or AI message to history.
        
        Args:
        - content: Message content.
        - is_human: Boolean to if message is from Human (True) or AI (False).
        """
        if is_human:
            self.messages.append(HumanMessage(content=content))
        else:
            self.messages.append(AIMessage(content=content))
    
    def chat(self, input_text):
        """
        Processes user input to model and streams LLM answer.
        
        Args:
        - input_text: User message.
        - language: default is English
        
        Returns:
        - response_content: complete answer when stream ends
        """
        # Add user input to chat history
        self.add_message(input_text, is_human=True)
        
        # Create chain, trimmed if necessary
        chain = (
            RunnablePassthrough.assign(messages=itemgetter("messages") | self.trimmer)
            | self.prompt
            | self.model
        )
        
        response_content = ""
        
        # Stream answer
        for response in chain.stream(
            {
                "messages": self.messages,
                "language": self.language
            },
            config=self.config
        ):
            print(response.content, end="", flush=True)
            response_content += response.content
        
        # Add AI response to history
        self.add_message(response_content, is_human=False)
        print()
        return response_content

    def get_conversation(self):
        """
        Returns conversation as a list.
        
        Returns:
        - messages: list of all messages in current conversation.
        """
        return self.messages
    
    def print_conversation(self):
        """
        Prints whole conversation in console.
        """
        for msg in self.messages:
            sender = "Human" if isinstance(msg, HumanMessage) else "AI"
            print(f"{sender}: {msg.content}")
