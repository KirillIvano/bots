# -*- coding: utf-8 -*-
import vk_api
from bs4 import BeautifulSoup
import requests
import json
import random
import time
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from keys import tokenbot
def bot():
    vk = vk_api.VkApi(token=tokenbot)
    vk._auth_token()
    
    longpoll = VkBotLongPoll(vk, 171465322)
    
    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboardBegin = {
        "one_time": False,
        "buttons": [
        [get_button(label="Начать", color="primary")],
        ]

    }
    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboard = {
        "one_time": False,
        "buttons": 
        [
        [get_button(label="⛅Погода", color="positive")],
        [get_button(label="📋О нас", color="positive"),
        get_button(label="📫Точки продаж", color="positive")],
        [get_button(label="💰Акции", color="negative")],
        [get_button(label="💵Прайс-лист", color="positive")],
        [get_button(label="💳Ввести промокод", color="negative")],
        [get_button(label="Наш Instagram", color="negative"),
        get_button(label="Отзывы", color="negative")],
        [get_button(label="🖊Сделать заказ", color="primary")]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboard00000 = {
        "one_time": False,
        "buttons": [ ]
    }
    keyboard00000 = json.dumps(keyboard00000, ensure_ascii=False).encode('utf-8')
    keyboard00000 = str(keyboard00000.decode('utf-8'))
    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboard_2 = {
        "one_time": False,
        "buttons": [
        [get_button(label="Тула", color="default")],
        [get_button(label="Prague", color="default")],
        [get_button(label="Самара", color="default")],
        [get_button(label="Ижевск", color="default")],
        [get_button(label="Москва", color="default")],
        [get_button(label="Казахстан", color="default")],
        [get_button(label="Екатеринбург", color="default")],
        [get_button(label="🔙В главное меню", color="negative")]
        ]
    }
    keyboard_2 = json.dumps(keyboard_2, ensure_ascii=False).encode('utf-8')
    keyboard_2 = str(keyboard_2.decode('utf-8'))



    def get_button(label, color, payload=""):
        return {
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color
        }
    keyboard_back = {
        "one_time": False,
        "buttons": [
        [get_button(label="Назад", color="negative")],
        ]
    }
    keyboard_back = json.dumps(keyboard_back, ensure_ascii=False).encode('utf-8')
    keyboard_back = str(keyboard_back.decode('utf-8'))



    print('Hello, Gregory!')
    time.sleep(0.5)
    print('I am starting the bot.py')
	
    a = month = userfrom1 = userfrom2 = userfrom3 = userfromweather1 = userfromweather2 = userfromweather3 = promo1 = promo2 = promo3 = 0
    vk.method("messages.send", {"peer_id": 169871363, "message": "Бот запущен!", "keyboard": keyboard00000 , "keyboard": keyboard, "random_id":0})
    for event in longpoll.listen():
        try:
           if (event.type == VkBotEventType.MESSAGE_NEW):
                id = event.object.from_id
                toid = event.object.peer_id
                body = event.object.text.lower()
                if (userfrom1 == id):
                    if (body != 'назад'):
                        telo1 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        vk.method("messages.send", {"peer_id": 169871363, "message": str(telo1) + "\nОтправитель vk.com/id" + str(id), "random_id": 0})
                        vk.method("messages.send", {"peer_id": toid, "message": "Ваше сообщение отправлено! Ожидайте ответа.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfrom1 = 0
                    else:
                        userfrom1 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (userfrom2 == id):
                    if (body != 'назад'):
                        telo2 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        vk.method("messages.send", {"peer_id": 169871363, "message": str(telo2) + "\nОтправитель vk.com/id" + str(id), "random_id": 0})
                        vk.method("messages.send", {"peer_id": toid, "message": "Ваше сообщение отправлено! Ожидайте ответа.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfrom2 = 0
                    else:
                        userfrom2 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (userfrom3 == id):
                    if (body != 'назад'):
                        telo3 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        vk.method("messages.send", {"peer_id": 169871363, "message": str(telo3) + "\nОтправитель vk.com/id" + str(id), "random_id": 0})
                        vk.method("messages.send", {"peer_id": toid, "message": "Ваше сообщение отправлено! Ожидайте ответа.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfrom3 = 0
                    else:
                        userfrom3 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (userfromweather1 == id):
                    if (body != 'назад'):
                        city1 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        url = 'https://yandex.ru/yandsearch?clid=1923018&text=погода в ' + city1
                        page1 = requests.get(url)
                        new_news1 = []
                        news1 = 0
                        soup1 = BeautifulSoup(page1.text, "html.parser")
                        news1 = soup1.findAll('div', class_='weather-forecast__current-temp')
                        if len(news1) > 0:
                            for i in range(len(news1)):
                                vk.method("messages.send", {"peer_id": toid, "message": "Сейчас в городе " + city1 + " " + news1[i].text, "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Город не найден", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfromweather1 = 0
                    else:
                        userfromweather1 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (userfromweather2 == id):
                    if (body != 'назад'):
                        city2 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        url = 'https://yandex.ru/yandsearch?clid=1923018&text=погода в ' + city2
                        page2 = requests.get(url)
                        new_news2 = []
                        news2 = 0
                        soup2 = BeautifulSoup(page2.text, "html.parser")
                        news2 = soup2.findAll('div', class_='weather-forecast__current-temp')
                        if len(news2) > 0:
                            for i in range(len(news2)):
                                vk.method("messages.send", {"peer_id": toid, "message": "Сейчас в городе " + city2 + " " + news2[i].text, "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Город не найден", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfromweather2 = 0
                    else:
                        userfromweather2 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (userfromweather3 == id):
                    if (body != 'назад'):
                        city3 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["text"]
                        url3 = 'https://yandex.ru/yandsearch?clid=1923018&text=погода в ' + city3
                        page3 = requests.get(url3)
                        new_news3 = []
                        news3 = 0
                        soup3 = BeautifulSoup(page3.text, "html.parser")
                        news3 = soup3.findAll('div', class_='weather-forecast__current-temp')
                        if len(news3) > 0:
                            for i in range(len(news3)):
                                vk.method("messages.send", {"peer_id": toid, "message": "Сейчас в городе " + city3 + " " + news3[i].text, "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        else:
                            vk.method("messages.send", {"peer_id": toid, "message": "Неверное имя города", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                        userfromweather3 = 0
                    else:
                        userfromweather3 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (promo1 == id):
                    if (body != 'назад'):
                        if (body  == 'amicus'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo1 = 0
                        elif (body == 'frater'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) +" активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo1 = 0
                        else:
                            promo1 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!", "keyboard":keyboard, "random_id": 0})
                    else:
                        promo1 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (promo2 == id):
                    if (body != 'назад'):
                        if (body  == 'amicus'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo2 = 0
                        elif (body == 'frater'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) +" активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo2 = 0
                        else:
                            promo2 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!", "keyboard":keyboard, "random_id": 0})
                    else:
                        promo2 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif (promo3 == id):
                    if (body != 'назад'):
                        if (body  == 'amicus'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) + " активировал скидку 5% по промокоду.", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 5% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo3 = 0
                        elif (body == 'frater'):
                            vk.method("messages.send", {"peer_id": 169871363, "message": "Пользователь vk.com/id" + str(id) +" активировал скидку 10% по промокоду. ", "random_id": 0})
                            vk.method("messages.send", {"peer_id": toid, "message": "Промокод на 10% активирован.", "random_id": 0, "keyboard":keyboard00000 , "keyboard":keyboard})
                            promo3 = 0
                        else:
                            promo3 = 0
                            vk.method("messages.send", {"peer_id": toid, "message": "Такого промокода не существует!", "keyboard":keyboard, "random_id": 0})
                    else:
                        promo3 = 0
                        vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "keyboard":keyboard00000 , "keyboard":keyboard, "random_id": 0})
                elif body.find('погода') != -1:
                    if (userfromweather1 == 0):
                        userfromweather1 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите название города", "keyboard": keyboard_back, "random_id": 0})
                    elif (userfromweather2 == 0):
                        userfromweather2 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите название города", "keyboard": keyboard_back, "random_id": 0})
                    elif (userfromweather3 == 0):
                        userfromweather3 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите название города", "keyboard": keyboard_back, "random_id": 0})
                elif body.find('сделать заказ') != -1:
                    if (userfrom1 == 0):
                        userfrom1 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите сообщение", "keyboard": keyboard_back, "random_id": 0})
                    elif (userfrom2 == 0):
                        userfrom2 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите сообщение", "keyboard": keyboard_back, "random_id": 0})
                    elif (userfrom3 == 0):
                        userfrom3 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите сообщение", "keyboard": keyboard_back, "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Система перегружена, повторите попытку через 10 секунд", "random_id": 0})
                elif body.find('точки продаж') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Выберите город", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard_2})
                elif body.find('акции') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "⭐Подпишитесь на наш аккаунт Instagram и получите скидку 5%\ninstagram.com/hookah.mason\n\n📦Спецпредложение на первую оптовую закупку\napi.whatsapp.com/send?phone=79854474442", "random_id": 0})
                elif body.find('главное меню') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Выберите кнопку!", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard})
                elif body.find('prague') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬iSmoke Store Karlín\n🗺Křižíkova 489/66, Praha 8 - Karlín\n\n🏬iSmoke Store Dejvice\n🗺Evropská 1727/53, Praha 6 - Dejvice\n\n🏬iSmoke Garage Outlet\n🗺Mirovická 520/1, Praha 8 - Kobylisy\n\n🏬iSmoke Store Brno\n🗺Husova 8a, Brno-město\n\n📱Тел: +420 774 40 00 40\n\n💻ismoke.cz\n📷facebook.com/ismoke.cz", "random_id": 0, "attachment":"photo-169871449_456239102"})
                elif body.find('тула') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬ТЦ Тройка\n🗺ул. Каминского, 24В\n📱Тел:  +7 (999) 775-10-63\n\n💻vk.com/bambuk_tula\n📷instagram.com/bambuk_tula", "random_id": 0, "attachment":"photo-169871449_456239103"})
                elif body.find('самара') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬Магазин 'Шахта'\n🗺ул. Ново-Садовая, 271\n📱Тел: +7 (986) 950-36-00\n\n💻vk.com/shahta_63\n📷instagram.com/shahta63", "random_id": 0, "attachment":"photo-169871449_456239104"})
                elif body.find('москва') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬Кальянный магазин 'Smoke Lab'\n🗺ул. 4-я Тверская-Ямская, 7(цокольный этаж)\n📱Тел: +7 (903) 795-59-89\n📱Тел: +7 (495) 795-59-89 \n\n💻smokelab.org\n📷instagram.com/smoke_lab", "random_id": 0, "attachment":"photo-169871449_456239105"})
                elif body.find('екатеринбург') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬BAR&HOOKAHSHOP\n🗺ул. Декабристов, 20\n📱Тел: +7 (932) 122-14-60\n\n🏬HOOKAHSHOP&COFFEE\n🗺ул.Крауля, 8\n📱Тел: +7 (903) 08-61-349 \n\n💻vk.com/hzhookah\n📷instagram.com/hazehookahshop", "random_id": 0, "attachment":"photo-169871449_456239106"})
                elif body.find('ижевск') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Мы находимся по адресу:\n🏬S Club Shop\n🗺ул. Карла Маркса 177б (бц Арбат)\n📱Тел: +7 (912) 021-24-21\n\n💻vk.com/izh.smoke.club.shop\n📷instagram.com/sclubshop\n\n\n🏬Бар 'Сегодня можно'\n🗺ул. Советская, 14 \n📱Тел: 643364\n\n💻vk.com/segodnyamozhno\n💻vk.com/lounge_bsm\n📷instagram.com/segodnya_mozhno_lounge\n📷instagram.com/segodnya_mozhno\n\n\n🏬Берлога Shop&Lounge\n🗺ул. Красногеройская 63б\n📱Тел: +7 (912) 021-34-12\n\n💻vk.com/club171797380\n📷instagram.com/berloga_lounge_shop", "random_id": 0, "attachment":"photo-169871449_456239106"})
                elif (body.find('прайс') != -1) or (body.find('цены') != -1) or (body.find('цена') != -1) or (body.find('стоимость') != -1) or (body.find('чаши') != -1) or (body.find('чаша') != -1) or (body.find('чашка') != -1) or (body.find('чашки')!= -1):
                    vk.method("messages.send", {"peer_id": toid, "message": "", "random_id": 0, "attachment":"photo-169871449_457239266, photo-169871449_457239267, photo-169871449_457239268, photo-169871449_457239269, photo-169871449_457239270"})
                elif body.find('казахстан') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": """
				
Мы находимся по адресу:
🏬Rotana Shop Almaty
🗺Сейфуллина проспект, 410
📱Тел: +7 (701) 888-72-77

🏬Rotana Shop Astana
📱Тел: +7 (708) 336-44-41

💻vk.com/hookah_service_kz
💻www.hookahshop.kz
						""", "random_id": 0, "attachment":"photo-169871449_456239102"})
                elif body.find('о нас') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Основаная цель нашего производства - создавать максимально качественную продукцию, не имеющую аналогов.\nМы постарались учесть все критерии качества, которые позволяют нам смело заявить, что вскоре наша продукция займет лидирующую позицию на рынке.\n95% процентов, что после первой забивки вы забудете про все остальные чаши. \n\n◾ Максимально быстрый прогрев.\n\n◾ Усиленная вкусопередача.\n\n◾ Легко мыть, не трескаются от резких перепадов температуры.\n\n◾ Специальная техника отливки позволяет максимально контролировать жар.\n\n◾ Состав и обработка не имеющие аналогов", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard, "attachment":"photo-169871449_456239101"})
                elif body.find('чаши') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Воспользуйтесь кнопкой 'Прайс-лист' или 'сделать заказ'.", "random_id": 0})
                elif body.find('привет') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Привет! Воспользуйся клавиатурой для навигации!", "keyboard": keyboard00000, "keyboard": keyboard, "random_id": 0})
                elif body.find('начать') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "Привет! Воспользуйся клавиатурой для навигации!", "keyboard": keyboard00000, "keyboard": keyboard, "random_id": 0})
                elif body == 'назад':
                    vk.method("messages.send", {"peer_id": toid, "message": "", "keyboard":keyboard, "random_id": 0})
                elif body.find('instagram') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "instagram.com/hookah.mason", "keyboard":keyboard, "random_id": 0})
                elif body.find('отзывы') != -1:
                    vk.method("messages.send", {"peer_id": toid, "message": "vk.com/topic-169871449_39198416", "keyboard":keyboard, "random_id": 0})
                elif body.find('промокод') != -1:
                    if (promo1 == 0):
                        promo1 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back, "random_id": 0})
                    elif (promo2 == 0):
                        promo2 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back, "random_id": 0})
                    elif (promo3 == 0):
                        promo3 = vk.method("messages.getHistory", {"offset": 0, "count":200, "user_id": id})["items"][0]["from_id"]
                        vk.method("messages.send", {"peer_id": toid, "message": "Введите промокод", "keyboard": keyboard_back, "random_id": 0})
                    else:
                        vk.method("messages.send", {"peer_id": toid, "message": "Система перегружена, повторите попытку через 10 секунд", "random_id": 0})
                else:
                    vk.method("messages.send", {"peer_id": toid, "message": "Эта команда мне неизвестна.", "random_id": 0, "keyboard": keyboard00000, "keyboard": keyboard})
        except vk_api.AuthError as error_msg:
            print(error_msg)
            vk.method("messages.send", {"peer_id": 169871363, "message": 'перезагрузка', "random_id":0})
