import telebot
from decouple import config

bot = telebot.TeleBot(config('TELEGRAM_TOKEN'))

