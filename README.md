# My Django Application

This is a Django application that allows the storage of user records and has a small system.

## How to run

To run this application, follow these steps:

```python

# Enter the folder where the project is

$ cd projecttst
$ cd project_cad_users

# Run the commands to run the app

$ pip3 install

# Install Djonga if you don't have it

$ pip3 install django

# Creating the started migrations

$ python3 manager.py makemigrations

# Checking our beautiful database

$python3 manager.py migrate

# Starting our NASA server

$ python3 manager.py execution server

```
You can now access the application at `http://localhost:8000`.

## How to use

To use this app, follow these steps:

1. Access the home page at `http://localhost:8000`.
2. Click on the link to create a new account.
3. Fill in the fields with user information and click "Save".
4. The user will be added to the system and you will be able to see him in the user list.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request.

## License

This project is licensed under the MIT license.