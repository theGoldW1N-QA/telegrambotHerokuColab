#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5335395820:AAFB6A_2WxEcHscMsjtgnsqe1uFBWlgLITo'
from telebot import types
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton(text="Привет, бот!")
	markup.add(item1)
	bot.send_message(message.chat.id, text="Приветствую, {0.first_name}!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	sti2 = open('fox.webp', 'rb')
	if message.chat.type == 'private':
		if message.text == "Привет, бот!":
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton("🗄 Мой репозиторий")
			item2 = types.KeyboardButton("✈ Написать в Telegram")
			item3 = types.KeyboardButton("✍🏻 Написать в VK")
			item4 = types.KeyboardButton("✉️ Моя почта")
			item5 = types.InlineKeyboardButton(text="📖 О себе", callback_data='about')
			markup.add(item1,item2,item3,item4,item5)
			bot.send_message(message.chat.id, "Предлагаю Вашему вниманию небольшую информацию о себе 😇",reply_markup=markup)
		elif message.text == "🗄 Мой репозиторий":
			bot.send_message(message.chat.id, 'https://github.com/theGoldW1N-QA')
		elif message.text == "✈ Написать в Telegram":
			bot.send_message(message.chat.id, 'http://t.me/theGoldW1N')
		elif message.text == "✍🏻 Написать в VK":
			bot.send_message(message.chat.id, 'https://vk.com/im?sel=73685698')
		elif message.text == "✉️ Моя почта":
			bot.send_message(message.chat.id, 'crumb_93@mail.ru')
		elif message.text == "📖 О себе":
			markup = types.InlineKeyboardMarkup()
			photo = open('me1.jpg', 'rb')
			bot.send_sticker(message.chat.id, photo)
			item6 = types.InlineKeyboardButton(text="📱 Мой номер телефона", callback_data='about')
			markup.add(item6)
			bot.send_message(message.chat.id, text='Мухамедьяров Роман Вадимович. \nАмбициозный, целеустремленный молодой человек 😉 \nПостоянно развиваюсь в разных направлениях. \nВсегда рад помочь в трудной ситуации, как помочь, поддержать, так и чему то научить ☝️🤓', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, '🚫К сожалению я не знаю данную команду🚫')
			bot.send_sticker(message.chat.id, sti2)
			bot.send_message(message.chat.id, '🔁Повторите ввод команды. \nВведите команду /start либо /help для того, чтобы начать заново.')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'about':
        bot.answer_callback_query(callback_query_id=call.id, text='89517794603')

bot.polling(none_stop=True)












#https://core.telegram.org/bots/api#available-methods