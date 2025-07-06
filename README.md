# MyFirstProject: Fun Django Survey App

Welcome to **MyFirstProject**, a simple Django web app where users can fill out a fun survey form and see a creative results page!

---

## Features
- Collects user details like name, age, favorite color, and hobby.
- Calculates the user’s birth year based on their age.
- Displays the favorite color in its actual color.
- Simple, clean, and beginner-friendly Django setup.

---

## How to Run Locally

### 1. Clone this repo
git clone https://github.com/your-username/MyFirstProject.git
cd MyFirstProject

### 2. Create and activate a virtual environment (Optional but recommended)
python -m venv venv
source venv/Scripts/activate

### 3. Install Django
pip install django

### 4. Run the development server
python manage.py runserver

### 5. Open the app in your browser
Go to: http://127.0.0.1:8000/

How to Push Your Code to GitHub
If you made changes and want to push them to GitHub:

git add .
git commit -m "Describe your changes here"
git push

📁 Project Structure

MyFirstProject/
├── MyFirstProject/    # Django project settings
├── formsapp/          # Your Django app
│   ├── templates/
│   │   ├── home.html
│   │   └── success.html
├── manage.py
└── venv/              # Your virtual environment (not pushed to GitHub)

Future Ideas
Save survey responses to a database.

Add more creative survey questions.

Style the form using Bootstrap or Tailwind CSS.
---

