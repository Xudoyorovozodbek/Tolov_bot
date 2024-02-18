
import telebot
from telebot import types


API_TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.username
    bot.send_message(message.chat.id, f"Assalomu alaykum, {user_name}!")
    msg = bot.reply_to(message, "To'lov amalga oshirish uchun karta olish! \n Iltimos, ismingizni to'liq holda kiriting:")
    bot.register_next_step_handler(msg, process_name_step)

# Foydalanuvchi ismini qabul qilish
def process_name_step(message):
    chat_id = message.chat.id
    name = message.text
    msg = bot.reply_to(message, f"Rahmat, {name}! \n 8600530482257253 \n karta raqamiga to'lovni amalga oshiring va chekni adminga yboring pastdagi buyruqni orqali \n /admin")
    bot.register_next_step_handler(msg, starts)


@bot.message_handler(commands=['admin'])
def starts(message):
    user_name = message.from_user.username
    user = 'https://t.me/xudoyorov_ozodbek'
    channel_text = f"Chek yuborish uchun , {user_name}, iltimos, {user} ga o'ting va chekni yuboring."
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Chekni yuborish", url=user))
    bot.send_message(message.chat.id, channel_text, reply_markup=markup)

bot.polling(none_stop=True)

