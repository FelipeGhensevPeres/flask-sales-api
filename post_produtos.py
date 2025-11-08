import requests

#PARA VER UM PRODUTO ESPECIFICO, O ID DELE DEVE SER ADICIONADO AO LADO DE PRODUTOS COM UM (/) -- /produtos/1 ou /produtos/2
url = "http://127.0.0.1:5000/produtos"

novo_produto = {"id":4,
                "nome":"notebook",
                "preco":2000}

resposta = requests.post(url,json=novo_produto)

print(f'Status: {resposta.status_code}')
print(f'Resposta: {resposta.json()}') 