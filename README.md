# Employee Manager

O objetivo desse app é fornecer um meio para o gerenciamento de colaboradores de um empresa. A aplicação
é um CRUD, permitindo criar, editar, listar e remover colaboradores. Para acessar essas funcionalidades, antes é necessário se cadastrar na plataforma e em seguida realizar login. Como bônus foram adicionadas páginas de relatórios e função de pesquisa. A aplicação foi dividade em back e front, ambos hospedados no heroku.

# Backend da aplicação

A api da aplicação foi construida utilizando o framework django e django rest framework. Está hospedada no heroku e pode ser acessada <a href="https://ssys-employee-manager-test.herokuapp.com/">AQUI</a>. A página inicial conta com a documentação completa e interativa da API. Na maior parte da API é necessário estar autenticado, portanto realize login de forma interativa pelo swagger, Será retornado um token de acesso, deve ser adicionado em <strong>Available authorizations</strong> no formato <strong> Bearer [acess_token] </strong>.
Os usuários criado pelo endpoint de cadastro, documentado na api, podem fazer no Django Admin que é o painel de controle do django. Todas as tabelas do banco de dados da aplicação podem ser acessadas por lá, inclusive é possível povoar as tabelas por meio da importação de um arquivo .csv


# Frontend da aplicação

Para facilitar o teste da API desenvolvi um simples frontend que consome todos os endpoints criados. O mesmo pode ser acessado por <a href="https://frontend-dafiti-test.herokuapp.com/">AQUI</a>. O repositorio pode ser acessado nesse <a href="https://github.com/barretoMarcosPaulo/frontend">LINK</a>.


# Tecnologias
As tecnologias utilizados foram django, django rest framework, docker, SQLite, ReactJs e heroku para hospedagem. Testes automatizados da API tbm foram implementados.
