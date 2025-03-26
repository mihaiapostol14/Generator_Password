# Generator Password

## Overview
This repository contains a Django-based application for generating secure passwords. The application provides both a web interface and backend logic to generate and manage passwords. It allows users to specify the length and complexity of the password and provides options to export the passwords in different formats.

## Language Composition
- **Python**: 84.2%
- **HTML**: 13.5%
- **JavaScript**: 1.6%
- **CSS**: 0.7%

## Project Structure
```
Generator_Password/
├── README.md
├── requirements.txt
├── manage.py
├── Generator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── password_chars/
│   │   ├── __init__.py
│   │   └── chars.py
│   └── utils.py
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Key Components
1. **Python Scripts**
   - `manage.py`: Django's command-line utility for administrative tasks.
   - `Generator/`: Contains Django project settings and configurations.
   - `main/`: Contains the main application logic, including forms, models, views, and utilities.

2. **HTML Files**
   - Located in the `templates/` directory, used for rendering the web interface.

3. **JavaScript and CSS Files**
   - Located in the `static/` directory, used for enhancing the web interface.

## Features
- **Secure Password Generation**: Generates passwords with a combination of letters, numbers, and special characters.
- **Web Interface**: A Django-powered web interface to interact with the password generator.
- **Customizable Options**: Allows users to specify the length and complexity of the password.
- **Export Options**: Provides options to export the generated passwords in different formats (CSV, JSON, PDF).

## Installation and Usage
1. **Clone the Repository**
   ```sh
   git clone https://github.com/mihaiapostol14/Generator_Password.git
   cd Generator_Password
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```sh
   python manage.py runserver
   ```

4. **Access the Web Interface**
   Open your web browser and navigate to `http://localhost:8000`.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or suggestions, please open an issue or reach out to the repository owner.

## Existing README Content
```
# Django Generator Password

This is a simple generator password with functions of generated password and copy password
```
