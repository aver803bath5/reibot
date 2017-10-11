# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging
import re
import json
import requests
from urllib.parse import (unquote, quote)
from bs4 import BeautifulSoup
from configparser import ConfigParser
import sys
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me! <3")

def girlfriend(bot, update):
    logger.info("girlfriend called")
    search = '初音未來'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    url = 'https://www.google.com.tw/search?q='+ quote(search) +'&source=lnms&tbm=isch'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div',{'class':'rg_meta'})
    pick_num = random.randint(0, len(data))
    link , Type =json.loads(data[pick_num].text)['ou']  ,json.loads(data[pick_num].text)['ity']
    logger.info('sent girlfriend image '+link)
    update.message.reply_photo(link)
    update.message.reply_text('這是我女朋友給你看看\n')

def wifu(bot, update):
    logger.info("wifu called")
    search = '新垣結衣'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    url = 'https://www.google.com.tw/search?q='+ quote(search) +'&source=lnms&tbm=isch'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('div',{'class':'rg_meta'})
    pick_num = random.randint(0, len(data))
    link , Type =json.loads(data[pick_num].text)['ou']  ,json.loads(data[pick_num].text)['ity']
    logger.info('sent wifu image '+link)
    update.message.reply_photo(link)
    update.message.reply_text('這是我老婆給你看看')

def software(bot,update):
    logger.info("software called")
    update.message.reply_text(u"初音不是軟體，你才軟體，你全家都軟體！")

def one_hundred(bot, update):
    search = '超過100分'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    url = 'https://www.google.com.tw/search?q='+ quote(search) +'&source=lnms&tbm=isch'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find('div',{'class':'rg_meta'})
    link , Type =json.loads(data.text)['ou']  ,json.loads(data.text)['ity']
    logger.info('one_hundred called')
    update.message.reply_photo(link)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    cfg = ConfigParser()
    cfg.read('config')
    token = cfg.get('auth', 'token')
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(RegexHandler(u'女朋友', girlfriend))
    dp.add_handler(RegexHandler(u'老婆', wifu))
    dp.add_handler(RegexHandler(u'軟體', software))
    dp.add_handler(RegexHandler(u'100分|一百分', one_hundred))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
