import sqlite3
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6098251295:AAGgBPpph0-aGgH_97xFVXJnnY2vy0Hrxh0')
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
p_name varchar,
id_tele varchar,
number varchar)""")
con.commit()
name = ''
tg_id = ''


def save(name, tg_id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute(f"""insert into users(p_name, id_tele) values ('{name}'
                , '{str(tg_id)}')""")
    con.commit()
def get_all_data():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    d = cur.execute('select * from users').fetchall()
    print(d)
    return d

@bot.message_handler(content_types=['text'])
def say_hello(message):
    if message.text == '/start':
        name = message.from_user.first_name
        tg_id = message.from_user.id
        save(name, tg_id)
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        show_db = KeyboardButton('show database')
        markup.add(show_db)
        bot.send_message(message.chat.id, 'Привет, Алень', reply_markup=markup)
    if message.text == 'show database':
        d = get_all_data()
        m = ''
        for i in d:
            m += f'name = {i[0]}'
            m += f'tg_id = {i[1]} \n'
        bot.send_message(message.chat.id, m)

bot.polling()