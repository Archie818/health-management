# Sports Recommendation Website

## Overview

This Django-powered web application provides personalized training recommendations based on user profiles. The primary goal is to offer customized fitness guidance that aligns with individual health metrics. Users can register by providing basic information such as gender, age, height, and weight. The platform then offers tailored health and training advice. Additionally, the website features an open API to deliver custom training videos to developers in real-time.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)

## Getting Started

To begin using this project, ensure you have Python and Django installed on your system. The latest version of Python can be downloaded from the [official Python website](https://www.python.org/).

### Installation Steps

1. **Create the Project Folder**

```bash
mkdir sports-recommendation-website
```

2. **Install Virtualenv**

```bash
sudo pip3 install virtualenv
```

3. **Create a Virtual Environment**

```bash
python3 -m venv venv
```

4. **Activate the Virtual Environment**

- On macOS / Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

5. **Install Required Packages**

   Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

6. **Database Migrations**

   Configure the database by running the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Run the Development Server**

   Start the Django development server using:

```bash
python manage.py runserver
```

## Project Structure

The project follows Django's recommended project structure, composed of the following directories and files:

```
sports-recommendation-website/
    ├── health/               # Contains the main application code
    ├── api/                  # Contains the project API code
    ├── user/                 # Contains the project user-related code
    ├── manage.py             # Django command-line utility
    └── requirements.txt      # Project dependencies
```

## Dependencies

All project dependencies are listed in the `requirements.txt` file. To install them, use:

```bash
pip install -r requirements.txt
```

## Running the Application

After activating your virtual environment and installing necessary packages, run the development server with:

```bash
python manage.py runserver
```

## API Documentation

The API interface provides customized training videos to developers. Comprehensive API documentation is available within the `api/` directory of the project.

### Example Endpoint

1. **Get Training Recommendations**

   - **URL:** `/api/training-recommendations/`
   - **Method:** `GET`
   - **Description:** Returns a list of training recommendations based on user's profile data.

For detailed information on each endpoint, refer to the API documentation files contained within the `api/` directory.

---

For any further questions or contributions, feel free to open an issue or submit a pull request.
