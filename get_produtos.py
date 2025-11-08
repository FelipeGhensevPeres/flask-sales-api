import requests

url = "http://127.0.0.1:5000/produtos"


resposta = requests.get(url)

print(f'Status:{resposta.status_code}')
print(f'Resposta:{resposta.json()}')