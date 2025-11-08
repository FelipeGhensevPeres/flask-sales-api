import requests

id_produto = int(input('Digite o ID do produto que voce quer excluir da lista: '))

url = f"http://127.0.0.1:5000/produtos/{id_produto}"

resposta = requests.delete(url)

print(f'Status: {resposta.status_code}')
print(f'Resposta: {resposta.json()}')