import telebot
from Config import currency, TOKEN, correct1, correct2, correct3
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, f"Чтобы начать работу, введите сообщение типа:\n"
                                      f"<валюта, цену которой вы хотите узнать>"
                                      f"<валюта, в которой надо узнать цену первой валюты>"
                                      f"<кол-во первой валюты>"
                                      f"\nУвидеть список всех доступных валют: /values")


@bot.message_handler(commands=['values'])
def values(message):
    text = "Доступные валюты:"
    for key in currency.keys():
        text = "\n".join((text, key))
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=["text"])
def convert_(message):
    try:
        values_ = message.text.split(" ")
        if len(values_) != 3:
            raise APIException("Некорректное кол-во данных.")
        base, quote, amount = values_
        total_prise = CurrencyConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неудалось обработать команду.\n{e}")
    else:
        if int(amount) == 1:
            bot.send_message(message.chat.id, f"Цена {amount} {correct1[base]} в {correct3[quote]} = {total_prise}")
        else:
            bot.send_message(message.chat.id, f"Цена {amount} {correct2[base]} в {correct3[quote]} = {total_prise}")


bot.polling(none_stop=True)
