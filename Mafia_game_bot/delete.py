import telebot
import config
bot = telebot.TeleBot(config.token)
bot.deleteWebhook()