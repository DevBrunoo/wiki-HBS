# Meu Aplicativo Django

Este é um aplicativo Django que permite o armazenamento de cadastros de usuários e possui um pequeno sistema.

## Como executar

Para executar este aplicativo, siga os seguintes passos:

1. Clone este repositório para o seu computador.
2. Navegue até a pasta do repositório clonado.
3. Crie um ambiente virtual com o comando `python -m venv venv`.
4. Ative o ambiente virtual com o comando `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows).
5. Instale as dependências com o comando `pip install -r requirements.txt`.
6. Execute as migrações do banco de dados com o comando `python manage.py migrate`.
7. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.

Agora você pode acessar o aplicativo em `http://localhost:8000`.

## Como usar

Para usar este aplicativo, siga os seguintes passos:

1. Acesse a página inicial em `http://localhost:8000`.
2. Clique no link para criar uma nova conta.
3. Preencha os campos com as informações do usuário e clique em "Salvar".
4. O usuário será adicionado ao sistema e você poderá visualizá-lo na lista de usuários.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT.
