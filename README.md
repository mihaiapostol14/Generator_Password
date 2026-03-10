## 🔐 Password Generator

A robust, full-stack web application for generating cryptographically secure passwords with granular customization.
Built on Django with a modern, responsive UI featuring glassmorphism design patterns. The application leverages Python's
`secrets` module for cryptographic randomness, ensuring high-quality entropy in generated passwords.

## 📋 Tech Stack

- **Backend:** Django (Python Web Framework)
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **UI Framework:** Bootstrap 5.3
- **Styling:** Glassmorphism design with custom CSS animations
- **Cryptography:** Python `secrets` module for secure random generation
- **Database:** SQLite3

## Installation & Setup

### Prerequisites

Ensure your system has the following installed:

- **Python 3.10+** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager - typically included with Python)
- **git** (for version control)
- **virtualenv** or **venv** (Python virtual environment)

### Step 1: Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/Generator_Password.git
cd Generator_Password/Password
```

### Step 2: Create Virtual Environment

**On Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Installed Packages:**

```
asgiref==3.11.1          # ASGI reference implementation
colorama==0.4.6          # simplify the process of adding colored text
Django==5.2.8            # Web framework
sqlparse==0.5.5          # SQL parser utility
tzdata==2025.3           # Timezone database
```

### Step 4: Navigate to Project Directory

```bash
cd Password
```

### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```

This creates the SQLite database and initializes all Django tables:

- `django_migrations`

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts:

```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

**Output:**

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## 🎯 Detailed Features

### 1. **Dynamic Password Generation**

- **Length Configuration:** Users can specify password length from 6 to 500 characters
- **Character Set Selection:** Granular control over character composition:
    - Uppercase Letters (A-Z)
    - Lowercase Letters (a-z)
    - Numeric Digits (0-9)
    - Special Symbols (!@#$%^&*)
- **Validation:** Enforces minimum selection of at least one character type
- **Cryptographic Security:** Uses Python's `secrets.choice()` for uniform random selection from the character pool

### 2. **Real-Time Clipboard Integration**

- **Copy-to-Clipboard:** Single-click password copying via Clipboard API
- **Toast Notifications:** Visual feedback on successful copy with auto-dismissing Bootstrap toast
- **Monospace Display:** Password rendered in fixed-width font for clarity

### 3. **Form Validation**

- **Client-Side:** HTML5 input constraints (min/max length)
- **Server-Side:** Django form validation ensuring at least one character type is selected
- **Error Handling:** User-friendly error messages for invalid submissions

### 4. **Responsive User Interface**

- **Glassmorphism Design:** Modern frosted-glass effect with backdrop blur
- **Dark Mode Aesthetic:** Deep space color palette (radial gradient background)
- **Mobile Optimized:** Bootstrap grid system ensures responsive layout across all devices
- **Interactive Elements:** Smooth hover transitions and visual feedback on buttons

### 5. **Session Management**

- **Password Persistence:** Generated passwords stored in Django session variables
- **Multi-Request State:** Maintains generated password across form submissions

### 6. **User Interface Components**

- **Navigation Bar:** Dynamic navbar with authentication-aware components
- **Message System:** Django messages framework for notifications
- **Card-Based Layout:** Centered card design with shadow effects
- **Custom Styling:** Poppins Google Font throughout for modern typography

## 📁 Architecture

```
Password/
├── generator/                      # Django app
│   ├── forms.py                   # GeneratorForm with validation logic
│   ├── views.py                   # PasswordGeneratorView (FormView)
│   ├── utils.py                   # GeneratorMixin for context
│   ├── urls.py                    # URL routing
│   └── models.py                  # Data models
├── templates/
│   ├── base.html                  # Base template
│   ├── generator/
│   │   └── generator.html         # Main password generator interface
│   └── includes/
│       ├── default_navbar.html
│       ├── auth_user_navbar.html
│       └── message.html
├── static/
│   └── generator/
│       ├── css/
│       │   └── generator.css      # Glassmorphism styling
│       └── js/
│           └── generator.js       # Clipboard functionality
├── manage.py                      # Django management script
├── db.sqlite3                     # Database
└── requirements.txt               # Python dependencies
```

## 💻 Core Logic Explanation

### Password Generation Algorithm

The backend implements a multi-step character pool construction:

1. User selects desired character types (uppercase, lowercase, numbers, symbols)
2. Backend constructs character pool by concatenating selected character sets
3. `secrets.choice()` randomly selects characters uniformly from pool
4. Process repeats for specified password length

```python
char_pool = ''
if use_uppercase: char_pool += string.ascii_uppercase
if use_lowercase: char_pool += string.ascii_lowercase
if use_numbers: char_pool += string.digits
if use_symbols: char_pool += string.punctuation

password = ''.join(secrets.choice(char_pool) for _ in range(length))
```

### Frontend Interactivity

JavaScript enables seamless copy functionality without page reload:

- Event listener on copy button captures password text
- Clipboard API writes to system clipboard
- Bootstrap Toast displays confirmation message

## 📊 Language Composition

| Language   | Percentage |
|------------|------------|
| Python     | 53.8%      |
| HTML       | 33.5%      |
| CSS        | 11.4%      |
| JavaScript | 1.3%       |

## 📝 Author

[Mihai Apostol](https://github.com/mihaiapostol14)
