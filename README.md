# l_notice_server

A Django-based backend project to manage notices, featuring RESTful APIs powered by Django REST Framework (DRF) and MySQL as the database.

## **Features**

- RESTful APIs for creating, retrieving, updating, and deleting notices.
- MySQL integration for scalable data storage.
- Django Admin interface for managing notices.

---

## **Setup Instructions**

Follow these steps to set up the project on a Windows laptop:

### **Prerequisites**

1. Python (>= 3.9): Download and install from [python.org](https://www.python.org/downloads/).
2. MySQL: Download and install MySQL Community Server from [mysql.com](https://dev.mysql.com/downloads/mysql/).
3. Git: Download and install from [git-scm.com](https://git-scm.com/).

---

### **Step 1: Clone the Repository**

Open a terminal and clone the repository:

```bash
git clone https://github.com/clashhulk/l_notice_server.git
cd l_notice_server
```

---

### **Step 2: Set Up Virtual Environment**

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

---

### **Step 3: Install Dependencies**

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### **Step 4: Set Up MySQL Database**

1. Open MySQL Workbench or the MySQL CLI and run:

   ```sql
   CREATE DATABASE l_notice_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   CREATE USER 'root'@'localhost' IDENTIFIED BY 'securepassword';
   GRANT ALL PRIVILEGES ON l_notice_db.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```

2. Update the `.env` file with the database credentials:

   ```
   DB_NAME=l_notice_db
   DB_USER=l_notice_user
   DB_PASSWORD=securepassword
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

---

### **Step 5: Apply Migrations**

Run the following commands to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **Step 6: Create a Superuser**

Create an admin user to access the Django Admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin account.

---

### **Step 7: Start the Development Server**

Run the server:

```bash
python manage.py runserver
```

Access the application:

- **Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **API Endpoints**: [http://127.0.0.1:8000/api/notices/](http://127.0.0.1:8000/api/notices/)

---

## **Folder Structure**

```
l_notice_server/
├── core/                  # Main application
│   ├── migrations/        # Database migrations
│   ├── models.py          # Models for the core app
│   ├── views.py           # API endpoints
│   ├── serializers.py     # DRF serializers
│   └── urls.py            # App-specific URLs
├── l_notice_server/       # Project settings
│   ├── settings.py        # Configuration
│   ├── urls.py            # Root URLs
│   └── wsgi.py            # Deployment
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables
```

---

## **Future Enhancements**

- Add user authentication with JWT.
- Implement filtering and pagination for API endpoints.
- Integrate a frontend (React or Angular).

---

## **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## **License**

This project is licensed under the MIT License.
