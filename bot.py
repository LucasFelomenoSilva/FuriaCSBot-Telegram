from flask import Flask, request
import telegram
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
bot = telegram.Bot(token=TOKEN)

from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

app = Flask(__name__)

model = genai.GenerativeModel('gemini-2.0-pro')
chat = model.start_chat()

contexto = "Você é um assistente especializado em FURIA Esports no cenário de CS:GO. Responda apenas relacionado à FURIA."


def start(update: Update, context):
    update.message.reply_text("👋 Olá! Sou o bot da FURIA Esports! Digite sua pergunta ou use os comandos disponíveis: /jogadores, /historico, /eventos.")

def jogadores(update: Update, context):
    mensagem = "🎮 Jogadores atuais da FURIA:\n- KSCERATO\n- yuurih\n- chelo\n- arT\n- FalleN"
    update.message.reply_text(mensagem)

def historico(update: Update, context):
    mensagem = "📜 Histórico da FURIA:\nFundada em 2017, a FURIA se destacou no cenário internacional de CS:GO com grandes participações em Majors e torneios de prestígio."
    update.message.reply_text(mensagem)

def eventos(update: Update, context):
    mensagem = "📅 Próximos eventos da FURIA:\n- ESL Pro League\n- BLAST Premier\n- IEM Cologne"
    update.message.reply_text(mensagem)


def receber_mensagem(update: Update, context):
    mensagem_usuario = update.message.text

    prompt_completo = f"{contexto}\nUsuário: {mensagem_usuario}\nAssistente:"
    resposta = chat.send_message(prompt_completo)

    update.message.reply_chat_action(action=telegram.constants.ChatAction.TYPING)

    update.message.reply_text(resposta.text)


@app.route(f"/bot{TOKEN}", methods=["POST"])
def webhook():
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("jogadores", jogadores))
    dispatcher.add_handler(CommandHandler("historico", historico))
    dispatcher.add_handler(CommandHandler("eventos", eventos))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_mensagem))

    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def index():
    return "Bot da FURIA no ar!"

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
