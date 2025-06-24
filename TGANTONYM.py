import nltk
from nltk.corpus import wordnet
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Функция для поиска антонимов слова
def get_antonyms(word):
    antonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                for ant in lemma.antonyms():
                    antonyms.add(ant.name())
    return antonyms

# Команда /start и приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для поиска антонимов английских слов.\n"
        "Напиши мне слово, и я постараюсь найти его антонимы.\n"
        "Для помощи используй команду /help."
    )

# Команда /help — помощь
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Как использовать бота:\n"
        "- Отправь английское слово, чтобы получить его антонимы.\n"
        "- Команда /about — информация о проекте.\n"
        "- Команда /help — эта справка."
    )

# Команда /about — информация о проекте
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Антоним-бот v1.0\n"
        "Создан для поиска антонимов английских слов с помощью WordNet и Python.\n"
        "Автор: Ваше имя или никнейм."
    )

# Обработка текстовых сообщений — поиск антонимов
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = update.message.text.strip().lower()
    antonyms = get_antonyms(word)
    if antonyms:
        await update.message.reply_text(f"Антонимы слова '{word}': {', '.join(sorted(antonyms))}")
    else:
        await update.message.reply_text(f"К сожалению, антонимы для слова '{word}' не найдены.")

if __name__ == '__main__':
    TOKEN = '8135015732:AAFW6RZRo-IpfXmaAaORWFshrrmejLZdPdE'  # Вставьте сюда токен от @BotFather

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()


