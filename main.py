from utils.channel import Channel



lofi_girl = Channel('UCSJ4gkVC6NrvII8umztf0Ow')
# # lofi_girl.print_info()
# print(lofi_girl)

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

# получаем значения атрибутов
print(vdud.title)
# вДудь
print(vdud.number_of_videos)
# 163
print(vdud.url_link)
# https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

# менять не можем
# vdud.id = 'Новое название'
# AttributeError: property 'channel_id' of 'Channel' object has no setter

# можем получить объект для работы с API вне класса
print(Channel.get_service())
# <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>


# создать файл 'vdud.json' в данными по каналу
vdud.save_to_json_file('vdud.json')

# Homework 3
print(vdud)

print(vdud < lofi_girl)
print(vdud > lofi_girl)
print(lofi_girl + vdud)
