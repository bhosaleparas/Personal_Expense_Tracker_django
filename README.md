# 📊 Personal Expense Tracker

A comprehensive, user-friendly expense tracking web application built with Django and Bootstrap. Manage your personal finances efficiently with intuitive features for tracking, categorizing, and analyzing your expenses.

![Django](https://img.shields.io/badge/Django-4.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Python](https://img.shields.io/badge/Python-3.9+-yellow)

## ✨ Features

### 🔐 Authentication & Security
- User registration and login system
- Secure password handling with validation
- Session-based authentication
- User-specific data isolation

### 💰 Core Expense Management
- **Add Expenses**: Record expenses with amount, date, note, and category
- **View Expenses**: Browse all expenses with filtering capabilities
- **Edit Expenses**: Update expense details easily
- **Delete Expenses**: Remove expenses with confirmation dialog

### 📊 Smart Categorization
- Pre-defined default categories (Food, Transport, Bills, Entertainment, Healthcare, Shopping, Other)
- Category-based expense organization
- Filter expenses by category
- Uncategorized expenses support

### 📈 Advanced Analytics & Reports
- **Dashboard**: Monthly overview with quick stats
- **Monthly Breakdown**: Track spending month by month
- **Category Analysis**: Visual spending patterns
- **Yearly Reports**: Comprehensive year-wise analysis
- **Interactive Charts**: Visual data representation with Chart.js

### 🔍 Smart Filtering
- Filter by category
- Filter by month and year
- Clear filters functionality
- Real-time filtering

### 📱 Responsive Design
- Mobile-first approach
- Fully responsive on all devices
- Bootstrap 5 components
- Intuitive user interface

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/bhosaleparas/Personal_Expense_Tracker.git
cd Personal_Expense_Tracker
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install - r requirements.txt
```
3. **Go into Project**
```bash
cd expense_tracker
```

4. **Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

7. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`
   - Register a new account or use admin credentials

## 📁 Project Structure

```
expense_tracker/
├── manage.py
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── expenses/
│   ├── models.py          # Database models
│   ├── views.py           # Application logic
│   ├── forms.py           # Django forms
│   ├── urls.py            # App URLs
│   └── templates/         # HTML templates
├── templates/
│   ├── base.html          # Base template
│   ├── registration/      # Auth templates
│   └── expenses/          # App templates
└── db.sqlite3             # Database file
```

## 🎯 Usage Guide

### 1. Registration & Login
- Navigate to the homepage and click "Register"
- Fill in username, email, and password
- After registration, log in with your credentials

### 2. Adding Expenses
- Click "Add Expense" in the sidebar
- Enter amount, date, category, and optional note
- Click "Save Expense" to record

### 3. Managing Expenses
- View all expenses in the "All Expenses" section
- Use filters to find specific expenses
- Click edit/delete icons to modify records

### 4. Viewing Reports
- Visit "Reports" for detailed analytics
- Select different years for historical data
- View monthly breakdowns and category analysis

### 5. Dashboard Overview
- Quick stats on monthly spending
- Recent expenses list
- Category-wise spending breakdown

## 🛠️ Technology Stack

### Backend
- **Django 4.2**: High-level Python web framework
- **SQLite**: Lightweight database for development
- **Python 3.9+**: Programming language

### Frontend
- **Bootstrap 5**: Responsive CSS framework
- **Chart.js**: Interactive data visualization
- **Font Awesome**: Icon library
- **HTML5/CSS3**: Modern web standards

### Development Tools
- Django ORM for database operations
- Django Template Engine for rendering
- Django Forms for data validation
- Django Authentication System

## 🔧 Configuration

### Environment Setup
The project uses Django's built-in settings. Key configurations:

```python
# Database (SQLite by default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Authentication URLs
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'
```

### Customization Options
1. **Change Database**: Update settings.py for PostgreSQL/MySQL
2. **Add Categories**: Modify `create_default_categories()` in views.py
3. **Currency Format**: Update templates for different currencies
4. **Date Format**: Modify date display in templates

## 📊 Database Schema

### Models
1. **User** (Django built-in)
2. **Category**
   - name (CharField)
   - user (ForeignKey to User)
   - is_default (BooleanField)
3. **Expense**
   - user (ForeignKey to User)
   - amount (DecimalField)
   - date (DateField)
   - note (TextField)
   - category (ForeignKey to Category)
   - created_at/updated_at (DateTimeField)





## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team for the amazing framework
- Chart.js for visualization library
- Font Awesome for icons
- All contributors and users

**Made with ❤️ using Django & Bootstrap**

⭐ Star this repo if you found it useful!