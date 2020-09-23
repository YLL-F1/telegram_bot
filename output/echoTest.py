#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram_bot.funtion import function, function_de ,risk_computation


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
#def start(update, context):
#   """Send a message when the command /start is issued."""
#   update.message.reply_text('Hi!')

def start(update, context):
    update.message.reply_text("加密数据请输入: /EN xxxxxxxx\n解密密数据请输入: /DE xxxxxxxx\n")
    keyboard = [[InlineKeyboardButton("BTC地址", callback_data='3FKwE5rvJxVcwJhjiPgScLVpR2cfeU3kMk'),
                 InlineKeyboardButton("XMR地址", callback_data='3FKwE5rvJxVcwJhjiPgScLVpR2cfeU3kMk')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('请选择捐赠货币:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="{}".format(str(query.data)))

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("加密数据请输入: /EN xxxxxxxx\n解密密数据请输入: /DE xxxxxxxx\n")


def en(update, context):
    key = ' '.join(context.args)
    jj = update.message.text +'\nbase64加密: ' + function.base64_en(key) + '\nAssic加密: ' + function.assic_en(key) + '\nMD5加密: ' + function.md5_en(key)
    jj = jj + '\n转16进制字符串: ' + function.hex_en(key) + '\n转16进制0x类型: ' + function.hex_en_0x(key)
    context.bot.send_message(chat_id=update.effective_chat.id, text=jj)

def de(update, context):
    key = ' '.join(context.args)
    jj = update.message.text +'\nbase6解密: ' + function_de.base64_de(key) + '\nAssic解密'
    jj = jj + function_de.assic_de(key)
    context.bot.send_message(chat_id=update.effective_chat.id, text=jj)

def N(update, context):
    key = ' '.join(context.args)
    jj = update.message.text +'\n' + risk_computation(key)
    context.bot.send_message(chat_id=update.effective_chat.id, text=jj)