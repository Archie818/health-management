# health-management

### Introduction

This is a Django project.
Create a training recommend website that automatically recommends training recommendations based on the user's profile. This is a customised website where the user gets the information that is best for them.
Users register by entering basic information such as gender, age, height and weight. The website gives health and training recommendations based on the information entered by the user.
The website also has an open API interface to send customized training videos to developers in real time.

### Getting Started

To get started with this project, you will need to have Python and Django installed on your system. You can download the latest version of Python from the official Python website.

1. create the project folder

```bash
mkdir bandersnatch-django
```

2. install Virtualenv

```bash
sudo pip3 instas/ll virtualenv
```

3. create a virtual environment

```bash
python3 -m venv venv
```

4. activate the virtual environment

```bash
source venv/bin/activate  mac
venv\Scripts\activate  win
```

5. install Django and other app

```bash
pip install django
venv/bin/python -m pip install -r requirements.txt
```

6. Configure the database files to migrate the database

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Finally, you can run the Django development server using the following command:

```bash
python manage.py runserver
```

### Project Structure

This Django project follows the recommended project structure, with the following main components:

health-management/ - the root directory of the project
health-management/health/ - contains the main application code
health-management/api/ - contains the project api part code
health-management/user/ - contains the project user part code
health-management/manage.py - the Django command-line utility
