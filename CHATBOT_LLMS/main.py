from chatbot import Chatbot

bot = Chatbot()
while True:
    pergunta = input('Você: ')
    print('Bot:', bot.responder(pergunta))