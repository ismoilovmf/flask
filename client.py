import requests


# data = requests.post('http://127.0.0.1:5000/user/',
#                      json={'email': 'test@mail.ru',
#                            'password': 'qwerty123'
#                            })
#
# data = requests.get('http://127.0.0.1:5000/user/1/')
#
# data = requests.post('http://127.0.0.1:5000/advertisement/',
#                      json={'title': 'adv_1',
#                            'description': 'qwerty123',
#                            'user_id': 1
#                            })
#
# data = requests.delete('http://127.0.0.1:5000/advertisement/1/')
#
# data = requests.delete('http://127.0.0.1:5000/user/1/')
#
#
data = requests.get('http://127.0.0.1:5000/advertisement/1/')


print(data.status_code,
      data.text, sep='\n')
