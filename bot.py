import os
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def set_commands(application):
    commands = [
        BotCommand("start", "Iniciar conversa com o bot"),
        BotCommand("jogadores", "Ver jogadores da FURIA 🎮"),
        BotCommand("historico", "Histórico do time 📜"),
        BotCommand("eventos", "Próximos eventos 📅"),
    ]
    await application.bot.set_my_commands(commands)
    print("✅ Comandos definidos com sucesso!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o Bot da FURIA 🎮")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Digite um comando válido ou use /start!")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    await set_commands(application)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await application.run_polling()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
