import requests
import json
# Авторизация на сервисе
token = ''
headers = {'Authorization': 'OAuth ' + token}
# Запрос к API
url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
params = {'path': '/test.txt', 'overwrite': 'true'}
response = requests.get(url, headers=headers, params=params)
# Обработка ответа
if response.status_code == 200:
    print('Файл успешно загружен на Яндекс.Диск')
else:
    print('Ошибка загрузки файла на Яндекс.Диск')
