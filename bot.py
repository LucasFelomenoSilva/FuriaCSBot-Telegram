
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat()

contexto = "Você é um assistente especializado em FURIA Esports no cenário do CS. Sempre forneça respostas relacionadas ao time, seus jogadores, histórico e próximos eventos, sem ser explícito demais sobre o time. Mantenha a conversa natural e focada na FURIAGG."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('👋 Olá! Sou o assistente oficial da FURIA Esports. Pergunte o que quiser! 🎯')

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem_usuario = update.message.text
    pensando_msg = await update.message.reply_text('⌛ Estou pensando na melhor resposta para você...')

    prompt_completo = f"{contexto}\nUsuário: {mensagem_usuario}\nAssistente:"
    resposta = chat.send_message(prompt_completo)

    resposta_final = f"🦊 **FURIA Responde:**\n\n{resposta.text}"

    await pensando_msg.edit_text(resposta_final, parse_mode="Markdown")


app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

app.run_polling()