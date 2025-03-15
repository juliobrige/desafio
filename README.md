# Cadastro de Usuários - Django e Python

Este projeto é uma aplicação web para **Cadastro de Usuários** desenvolvida com **Django** e **Python**. O objetivo da aplicação é permitir que os usuários se cadastrem em dois grupos distintos: **Vingadores** ou **Liga da Justiça**, fornecendo informações como **nome**, **e-mail**, **telefone** e **codinome**.

## Funcionalidades

- **Cadastro de Usuários:** Permite o cadastro de informações como nome, e-mail, telefone, codinome e grupo.
- **Validação de Dados:** Valida o número de telefone no formato correto (ex: (xx) xxxx-xxxx) utilizando expressões regulares.
- **Integração com APIs Externas:** Ao escolher um grupo (Vingadores ou Liga da Justiça), a aplicação acessa APIs externas para buscar codinomes disponíveis para os usuários.
- **Interface de Usuário:** Formulários com máscara para o campo de telefone utilizando **jQuery**, tornando a experiência de preenchimento mais amigável.
- **Evitar Repetição de Codinomes:** A aplicação verifica se o codinome já foi utilizado, garantindo que o novo usuário tenha um codinome único.

## Tecnologias Utilizadas

- **Django** - Framework utilizado para o desenvolvimento do back-end e controle do banco de dados.
- **Python** - Linguagem de programação utilizada para o desenvolvimento da aplicação.
- **jQuery** - Biblioteca JavaScript para a aplicação de máscaras de entrada no formulário, como no campo de telefone.
- **Requests** - Biblioteca para fazer requisições HTTP às APIs externas que fornecem os codinomes dos grupos.
- **HTML/CSS** - Para a estruturação e estilização do front-end da aplicação.

## Como Rodar o Projeto

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/juliobrige/cadastro-usuarios.git
