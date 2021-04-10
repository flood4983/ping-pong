import requests
import vk_api
from vk_api import VkUpload
import wikipedia
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi( token = '952d116801c69f233c3d133b24802fbd6e9b3db18a8a5e13f7243e880353655aa241ff371637c116bda84')
try:
    vk_session.auth
    print('Успешно!')
except vk_api.AuthError as error_msg:
    print(error_msg)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text.lower() == "wiki" or event.text == "Привет":
            if event.from_user: #Если написали в лс
                vk.messages.send(
                    user_id = event.user_id, 
                    random_id = 0,
                    message = "Введите ваш запрос:")

        elif event.from_chat: #Для беседы
            vk_messages.send(  
                user_id = event.user_id, 
                random_id = 0,
                message = "Ваш текст:")   

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                
                if event.from_user: #Если написали в лс
                    upload = VkUpload(vk_session)
                    url_pict = "https://klike.net/uploads/posts/2019-01/1547366815_1.jpg"
                    session = requests.Session()
                    image = session.get(url_pict, stream = True)
                    photo = upload.photo_messages(photos = image.raw)[0]
                    attachment = []
                    attachment.append("photo{}_{}". format(photo["owner_id"], photo["id"]))
                    vk.messages.send(
                        user_id = event.user_id, 
                        random_id = 0,
                        attachment = ",".join(attachment),
                        message = "Вот что я нашёл\n" + str(wikipedia.search(event.text)))
        
        

    