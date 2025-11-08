# Flask Sales API — Minha primeira API com Flask

Uma API REST desenvolvida em Python + Flask, que permite cadastrar, listar e excluir produtos de uma forma bem simples.
Os dados são armazenados em um arquivo JSON local, servindo como um pequeno banco de dados.

# Funcionalidades

✅ GET /produtos — Lista todos os produtos   
✅ GET /produtos/<id> — Busca um produto específico pelo ID  
✅ POST /produtos — Adiciona um novo produto  
✅ DELETE /produtos/<id> — Remove um produto existente  
✅ Todos os produtos são salvos automaticamente no arquivo Produtos.json  
✅ Em uso do DELETE e GET e não existir o produto procurado, o app retorna que não encontrou o produto
✅ No método POST ele sempre avisará que foi criado um novo produto caso ele tenha sido cadastrado com sucesso
