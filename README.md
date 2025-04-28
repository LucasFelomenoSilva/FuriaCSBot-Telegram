# Telegram Bot FURIA Esports

Bem-vindo ao Chatbot FURIA Esports!  
Este projeto foi desenvolvido para criar uma experiência interativa para os fãs da equipe **FURIA Esports** no cenário de **Counter-Strike (CS)**. O bot utiliza a **inteligência artificial generativa** da **Google Gemini** para fornecer respostas dinâmicas e contextuais, tornando a interação com o bot mais fluída e natural.

---

## Funcionalidades

- **Recepção automática** com uma saudação inicial e sugestões de perguntas rápidas.
- **Respostas dinâmicas e contextuais** utilizando o modelo **Google Gemini**.
- **Interação natural** com os usuários através do **Telegram**.
- **Fácil acesso** ao bot via Telegram, com integração simples para obter respostas sobre FURIA Esports.

---

## Tecnologias Utilizadas

- **Backend**: Python (Flask), Google Generative AI (Gemini)
- **API do Telegram**: `python-telegram-bot`
- **Outros**: `python-dotenv`, `Flask-Cors`

---

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasFelomenoSilva/FURIA-Esports-Telegram-Bot.git
   cd FURIA-Esports-Telegram-Bot

2. Instale as dependências Python:
```
pip install -r requirements.txt
```
3. Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:
```
TELEGRAM_BOT_TOKEN=<seu_token_aqui>
GEMINI_API_KEY=<sua_chave_api_aqui>
```
4. Execute o bot:
```
python bot.py
```

---

## Observações
- Certifique-se de que seu backend (app.py) esteja rodando antes de usar o frontend.

- A chave da API Gemini pode ser obtida pela plataforma Google AI.

## Autor
Lucas Felomeno Silva

