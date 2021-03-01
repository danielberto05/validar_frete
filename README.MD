# Validar frete

---
Esta aplicação API REST é uma demonstração usando Flask, cujo objetivo é realizar a consulta de tranportadoras e cotação do frete do produto conforme especificações de dimensões e peso.

### Funcionalidade

---
- Validar dimensões do produto e calcular frete para cada uma das opções de transportadoras.


### Tecnologias

---
- [Python (3.8.7)](https://www.python.org)
- [Flask (1.1.2)](https://flask.palletsprojects.com/en/1.1.x/)

### Melhorias futuras

---
- Aplicação de validação de token para segurança usando JWT;
- Armazenar opções de transportadoras em um banco de dado.

### Exemplo do uso da API

___
Endpoint: <b>/consultar_frete</b>
<br />
Método: <b>POST</b>
<br />
#### Input:
```json
{
  "dimensao": {
    "altura": 102,
    "largura": 40
  },
  "peso": 400
}
```
#### Output:
```json
[
  {
    "nome":"Entrega Ninja",
    "valor_frete": 12.00,
    "prazo_dias": 6
  },
  {
    "nome":"Entrega KaBuM",
    "valor_frete": 8.00,
    "prazo_dias": 4
  }
]
```



### Autor

---
<a href="https://github.com/danielberto05">
<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/40204831?s=400&u=5836d64c2412ad45edafa86550499eee3a572194&v=4" width="100px;" alt=""/>
<br />
<sub><b>Daniel Berto Farias</b></sub></a>

Feito com ❤️ por Daniel Farias!

[![Linkedin Badge](https://img.shields.io/badge/-Daniel-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/daniel-berto-94776867/)](https://www.linkedin.com/in/daniel-berto-94776867/) 
[![Gmail Badge](https://img.shields.io/badge/-danielberto05@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:danielberto05@gmail.com)](mailto:danielberto05@gmail.com)
