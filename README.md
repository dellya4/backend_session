# WishMe

**WishMe** is a Flask-based web application that allows users to manage their personal wishlists and view or reserve items from other users' wishlists.

---

## Features

* User registration and login (with "remember me" support)
* Secure authentication via Flask-Login
* Create, edit, delete personal wishes
* Upload images for wishes
* View and search other users' wishlists
* Reserve and unreserve other users' wishes (with restrictions)
* Color-coded UI based on reservation status

---

## Technologies Used

* Python 3
* Flask
* Flask-Login
* Jinja2
* SQLite (via SQLAlchemy)
* Bootstrap 5 (frontend styling)

---

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dellya4/backend_session
   cd wishMe
   ```

2. **Create virtual environment and install dependencies**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the app**:

   ```bash
   flask run
   ```

4. **Access in browser**:

   Navigate to `http://127.0.0.1:5000`

---

## Project Structure

```
wishMe/
├── backend_session/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── auth_routes.py
│   └── wishlist_routes.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── wishlist/
│       ├── index.html
│       ├── add.html
│       ├── edit.html
│       ├── search.html
│       └── user_wishlist.html
├── static/
│   ├── uploads/
│   └── placeholder.png
└── app.py
```

---

## Notes

* Users cannot reserve their own wishes.
* A wish can only be reserved by one user at a time.
* Reserved wishes are shown with a different style.
* Image uploads are saved in the `static/uploads/` folder.

---

## Author

Created by Adel Abdrakhmanova
