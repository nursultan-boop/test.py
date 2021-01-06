import telebot

bot = telebot.TeleBot('1442481924:AAE_u0JPQVepbIwWhAkUHGc1Abj7MVpmGnI')


@bot.message_handler(content_types=['text'])
def echo_msg(message):
    if message.text.lower() == 'билолбек хуйло':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBt3lf5c-o-z1WAdi4x_63XKt2srcoMgACGQADKQGoGxPayO5_aobEHgQ',
                         reply_to_message_id=message.id)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, "пидора ответ")
    elif message.text.lower() == 'да':
        bot.send_message(message.chat.id, "пизда")
    elif message.text.lower() == 'а':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBt3tf5da7Mb6-wDlGQkyMUDXKoNamygACigADPeGrF81bEXT9MYesHgQ',
                         reply_to_message_id=message.id)
    elif "bot" in message.text:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBt31f5dcmByD2-gFLXqUkldJc8f9emgAC_gADKQGoGxfbXeebb7mgHgQ")
        for _ in range(15):
            bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, 'К такой хуйне я не был готов')


if __name__ == '__main__':
    bot.polling(none_stop=True)
