import os
import requests
import dotenv
import telebot
from telebot.types import Message
from telebot.types import KeyboardButton
from telebot.types import ReplyKeyboardMarkup


dotenv.load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]
WOLF_PORT = os.environ["WOLF_PORT"]


bot = telebot.TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Auuf!"))
    bot.send_message(message.chat.id, "Auuuf!", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def process_message(message: Message):
    response = requests.get(url=f"http://127.0.0.1:{WOLF_PORT}/wolf/")
    text = response.text
    bot.reply_to(message, text)


if __name__ == "__main__":
    print(bot.get_my_name().name, "started")
    bot.infinity_polling()
