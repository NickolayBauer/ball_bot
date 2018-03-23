# -*- coding: utf-8 -*-
import telebot
import random
bot = telebot.TeleBot("483430314:AAEv73Q6-IN7FS06pLL0FgukLsep4ZpmRp4")

mass_word = ['нет',
             'возможно',
             'вполне вероятно',
             'сокрее да, чем нет',
             'да']

def cho():
    return random.choice(mass_word)

@bot.message_handler(commands=['cnance'])
def compliment(message):
    bot.send_message(message.chat.id, 'Помогу узнать, вероятность того или иного события\n'
                                      'Пример <есть шансы, что меня не отчислят?>'
                                      'version - 0.1\n'
                                      'author - @Nickolas_510')


    @bot.message_handler(func=lambda message: True and  "есть шансы" in  message.text.lower() , content_types=['text'])
    def get_start(message):
        bot.send_message(message.chat.id, cho(), reply_to_message_id = message.message_id)

if __name__ == "__main__":
    bot.polling(none_stop=True)


