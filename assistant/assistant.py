from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import AIMessage, HumanMessage
from operator import itemgetter

class ChatBot:
    def __init__(self, api, language='English'):
        """
        Inicializa el chatbot con el prompt, modelo, trimmer opcional y config de streaming.
        
        Args:
        - prompt: El objeto prompt que formatea las entradas del usuario.
        - model: El modelo que generará las respuestas.
        - trimmer: Una función opcional para procesar los mensajes.
        - config: Configuración para el streaming (si es requerido por el modelo).
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
        self.messages = []  # Almacenamos los mensajes
        self.config = config = {"configurable": {"session_id": "abc1"}}  # Configuración para el stream
        self.language = language
    
    def add_message(self, content, is_human=True):
        """
        Añade un mensaje a la conversación, ya sea humano o de la IA.
        
        Args:
        - content: El contenido del mensaje.
        - is_human: Booleano para determinar si es un mensaje humano (True) o AI (False).
        """
        if is_human:
            self.messages.append(HumanMessage(content=content))
        else:
            self.messages.append(AIMessage(content=content))
    
    def chat(self, input_text):
        """
        Procesa la interacción con el usuario, enviando el input al modelo y devolviendo la respuesta en tiempo real.
        
        Args:
        - input_text: El mensaje del usuario.
        - language: El idioma de la interacción (por defecto es inglés).
        
        Returns:
        - response_content: El contenido completo del mensaje generado por el modelo.
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

    def get_conversation(self):
        """
        Devuelve la conversación completa en formato de lista.
        
        Returns:
        - messages: Una lista de los mensajes hasta el momento.
        """
        return self.messages
    
    def print_conversation(self):
        """
        Imprime la conversación completa en la consola.
        """
        for msg in self.messages:
            sender = "Human" if isinstance(msg, HumanMessage) else "AI"
            print(f"{sender}: {msg.content}")
