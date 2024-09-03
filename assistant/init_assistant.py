from assistant.assistant import ChatBot

def init_assistant(api):
    if api:
        try:
            chatbot = ChatBot(api)
            print('Assistant initialized!')
            return chatbot
        except:
            print('API was invalid. Proceeding without assistant...')
            return None
    else:
        print('Proceeding to analyze without assistant...')
        return None