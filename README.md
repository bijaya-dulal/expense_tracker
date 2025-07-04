# expense_tracker

A RESTful API for tracking personal expenses and income with automatic tax calculations and JWT authentication.

## Tech Stack:

-Python 3.10.12
-Django and REST Framework
-SQLite
-Simple JWT for authentication

## Features
-JWT-based authentication
-Register & Login
-Personal expense/income tracking
-Automatic tax calculation (flat or percentage)
-Superuser access to all records
-Paginated API responses

##  API Endpoints

### Auth
- `POST /api/auth/register/`  Register
- `POST /api/auth/login/`  Get token
- `POST /api/auth/refresh/`  Refresh token

### Expenses
- `GET /api/expenses/`  List expenses (paginated)
- `POST /api/expenses/`  Create a new record
- `GET /api/expenses/{id}/`  Retrieve record
- `PUT /api/expenses/{id}/`  Update record
- `DELETE /api/expenses/{id}/`  Delete record

##  Setup

```bash
git clone https://github.com/bijaya-dulal/expense_tracker
cd expense_tracker
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

