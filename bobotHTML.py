from flask import Flask
import bot

app = Flask(__name__)

@app.route('/')
def bonjour():
    return "BobOt: Bonjour ! Je m'appelle BoBot.\n Demande-moi ce que tu veux sur la promo Data IA. Si tu veux partir, écris q!"

@app.route('/<question>')
def requete(question):
    return bot.bobot(question)

if __name__ == "__main__":
    app.run()
