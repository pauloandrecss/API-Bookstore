# API-Bookstore

## Projeto de API-REST em Python Utilizando o DJANGO REST FRAMEWORK ##

### O projeto consta com 3 endpoints principais ###

[Endpoint Produto](https://bookstore-api-ebac-728078bf2b07.herokuapp.com/bookstore/v1/product/)</br>
[Endpoint Category](https://bookstore-api-ebac-728078bf2b07.herokuapp.com/bookstore/v1/category/)</br>
[Endpoint Order](https://bookstore-api-ebac-728078bf2b07.herokuapp.com/bookstore/v1/order/)</br>
[Token Generator](https://bookstore-api-ebac-728078bf2b07.herokuapp.com/api-token-auth/)</br>

Todos os endpoints podem ser testados clicando em suas respectivas urls.</br></br>
Todos possuem todas as operações de CRUD sendo Create e Read efetuados pelos métodos POST e GET, e Update e Delete efetuados pelos métodos PUT, PATCH e DELETE apenas colocando ao fim da URL o ID do item em questão.</br>
ex: ...bookstore/v1/product/4/</br></br>
Todas as tabelas estão relacioniadas entre elas, por esse motivo é utilizado um banco de dados relacional, no caso o PostgreSQL.</br></br>
O endpoint Order por simular dados sensíveis está com autenticação via token.</br></br>
O endpoint Token Generator disponibiliza esse token com o método POST, enviando JSON com username e password, utilize admin e adminpass respectivamente para poder testar.</br></br>
O projeto utiliza GitHub Actions para criação da nossa pipeline, automação de testes em commits e automação de deploy assim que algum novo commit seja enviado a main branch.</br></br>
O projeto utiliza Docker para a criação de conteiners e Heroku para efetuar o seu deploy.</br></br>

