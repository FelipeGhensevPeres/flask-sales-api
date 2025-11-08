from flask import Flask
from flask import jsonify
from flask import request
import json

#ESSA É A URL DO SITE
url = 'http://127.0.0.1:5000'

app = Flask(__name__)

#CARREGAR OS PRODUTOS DA LISTA E RETORNAR UMA LISTA VAZIA CASO NAO ENCONTRE NADA
def carregar_produtos():
    try:
        with open('Produtos.json','r',encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


#SALVA OS PRODUTOS
def salvar_produtos():
    with open('Produtos.json','w',encoding='utf-8') as arquivo:
        json.dump(produtos,arquivo,indent=4,ensure_ascii=False) 

produtos = carregar_produtos()


#INICIA A APLICACAO USANDO PYTHON APP.PY
@app.route("/")
def home():
    return "Minha API Flask ta no ar"


#METODO GET VER OS PRODUTOS DA LISTA
@app.route('/produtos',methods=['GET'])
def listar_produtos():
    return jsonify(produtos)
    

#METODO GET PRA VER ALGUM PRODUTO ESPECIFICO DE ACORDO COM O ID DO PRODUTO
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    for p in produtos:
        if p['id'] == id:
            return jsonify(p)
    return jsonify({"erro": "Produto nao encontrado"}), 404


#METODO POST PARA ADICIONAR UM NOVO PRODUTO A LISTA
@app.route('/produtos',methods=['POST'])
def adicionar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    salvar_produtos()
    return jsonify({"mensagem": "Produto adicionado com sucesso", "produto": novo_produto}), 201


#METODO DELETE PARA EXCLUIR UM PRODUTO DA LISTA DE ACORDO COM O ID DO PRODUTO
@app.route('/produtos/<int:id>',methods=['DELETE'])
def deletar_produto(id):
    for p in produtos:
        if p['id'] == id:
            produtos.remove(p)
            salvar_produtos()
            return({"mensagem": "O produto foi removido com sucesso!"})
    return jsonify({"erro": "Produto nao encontrado"}), 404
    


if __name__ == "__main__":
    app.run(debug=True)