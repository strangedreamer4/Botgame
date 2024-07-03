from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import InlineQueryHandler, CommandHandler, CallbackContext, Updater
import random

# Replace with the new bot token
BOT_TOKEN = '6901974736:AAEzVedOeO3hIkmYCv-8aSxdnpUsOJOjg5k'

# Sample trivia questions
TRIVIA_QUESTIONS = [
    {
        'question': 'What is the capital of France?',
        'answers': ['Paris', 'Berlin', 'Rome', 'Madrid'],
        'correct': 0
    },
    {
        'question': 'Who wrote "To Kill a Mockingbird"?',
        'answers': ['Harper Lee', 'Mark Twain', 'Ernest Hemingway', 'F. Scott Fitzgerald'],
        'correct': 0
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'answers': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'correct': 2
    }
]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your trivia game bot. Type @cyberprimeofficalbot in any chat to start playing.')

def inlinequery(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query.lower()
    
    if query == "":
        return

    question = random.choice(TRIVIA_QUESTIONS)
    answers = question['answers']
    correct_answer = answers[question['correct']]

    results = [
        InlineQueryResultArticle(
            id='1',
            title=question['question'],
            input_message_content=InputTextMessageContent(f"Q: {question['question']}\n\nA: {correct_answer}"),
            description=" ".join(answers),
        )
    ]

    update.inline_query.answer(results)

def main() -> None:
    updater = Updater(BOT_TOKEN)
    
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
