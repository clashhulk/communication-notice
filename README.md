# Communication Notice System

A scalable microservices-based system for managing notices, organizations, and multi-channel communication. This project supports both traditional deployment and Docker-based containerized environments.

## **Project Overview**

This project handles the creation, management, and communication of notices through multiple channels (Email, SMS, WhatsApp, RPAD). It is built using the following architecture:

- **Microservices**: Separate Django services for Users, Notices, Communication, and Reporting.
- **Database**: A single shared PostgreSQL instance for all services.
- **Frontend**: React.js for the user interface, interacting with backend REST APIs.
- **Containerization (Optional)**: Docker and Docker Compose for orchestrating services.

---

## **Features**

- **User Management**: Manage users, roles, and organizations.
- **Notice Management**: Create, update, and track notices with dynamic data fields.
- **Communication Service**: Queue-based communication logs for Email, WhatsApp, SMS, and RPAD.
- **Reporting**: Track delivery statuses, user actions, and system audits.
- **Flexibility**: Run the project in a traditional or Dockerized environment.

---

## **Tech Stack**

### Backend:

- **Django**: Backend framework for each microservice.
- **Django REST Framework (DRF)**: To expose REST APIs.
- **PostgreSQL**: Database for persistent storage.

### Frontend:

- **React.js**: Frontend UI consuming the REST APIs.

### Deployment:

- **Docker & Docker Compose**: Containerization and orchestration (optional).

---

## **Directory Structure**

```plaintext
communication-notice/
├── docker-compose.yml         # Orchestrates all services (Docker setup)
├── Makefile                   # Automates common tasks (Docker setup)
├── .env                       # Environment variables
├── README.md                  # Project documentation
├── user_service/              # User management service
│   ├── manage.py
│   ├── user_service/
│   └── users/
├── notice_service/            # Notice management service
│   ├── manage.py
│   ├── notice_service/
│   └── notices/
├── communication_service/     # Communication handling service
│   ├── manage.py
│   ├── communication_service/
│   └── communications/
├── reporting_service/         # Reporting and tracking service
│   ├── manage.py
│   ├── reporting_service/
│   └── reports/
├── shared/                    # Shared utilities (if any)
├── logs/                      # Centralized logs for all services
```

---

## **Setup Instructions**

### **Option 1: Traditional Setup (Without Docker)**

#### Prerequisites

- Python 3.9+
- PostgreSQL
- Node.js (for React.js frontend)

#### **Step 1: Clone the Repository**

```bash
git clone <repository_url>
cd communication-notice
```

#### **Step 2: Set Up the Database**

1. Install PostgreSQL and create a database:
   ```bash
   createdb communication_notice
   ```
2. Configure your database connection in the `.env` file:
   ```env
   # PostgreSQL Database Configuration
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=communication_notice
   DB_USER=
   DB_PASSWORD=
   DB_HOST=localhost
   DB_PORT=5432
   ```

#### **Step 3: Set Up Each Service**

For each service (e.g., `user_service`), follow these steps:

1. Navigate to the service directory:
   ```bash
   cd user_service
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

Repeat these steps for `notice_service`, `communication_service`, and `reporting_service` using different ports (`8001`, `8002`, `8003`).

### **Option 2: Docker Setup**

#### Prerequisites

- Docker
- Docker Compose

#### **Step 1: Clone the Repository**

```bash
git clone <repository_url>
cd communication-notice
```

#### **Step 2: Set Up Environment Variables**

Create a `.env` file in the project root:

```env
# PostgreSQL Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=communication_notice
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

#### **Step 3: Build and Start Services**

Run the following command to build and start all services:

```bash
docker-compose up --build
```

#### **Step 4: Apply Migrations**

Run migrations for each service:

```bash
docker exec -it user_service python manage.py makemigrations
docker exec -it user_service python manage.py migrate
docker exec -it notice_service python manage.py makemigrations
docker exec -it notice_service python manage.py migrate
# Repeat for other services...
```

#### **Step 5: Access Services**

- **User Service** : `http://localhost:8000`
- **Notice Service** : `http://localhost:8001`
- **Communication Service** : `http://localhost:8002`
- **Reporting Service** : `http://localhost:8003`

#### **Step 6: Access Frontend**

clone and start frontend using `npm start`

The React frontend (if dockerized) will be available at `http://localhost:3000`.

---

## **Common Commands**

### Traditional (Without Docker)

- **Start a service** :

```bash
  python manage.py runserver
```

- **Run migrations** :

```bash
  python manage.py makemigrations
  python manage.py migrate
```

### Docker

- **Start all services** :

```bash
  docker-compose up --build
```

- **Stop all services** :

```bash
  docker-compose down
```

- **View logs** :

```bash
  docker-compose logs -f
```

- **Run migrations for a service** :

```bash
  docker exec -it user_service python manage.py migrate
```

---

## **API Endpoints**

### **User Service**

- `GET /api/users/`: List all users.
- `POST /api/users/`: Create a new user.

### **Notice Service**

- `GET /api/notices/`: List all notices.
- `POST /api/notices/`: Create a new notice.

### **Communication Service**

- `POST /api/communications/`: Queue a communication log.

### **Reporting Service**

- `GET /api/reports/`: Generate reports.

---

## **Future Enhancements**

- Transition to separate databases for each microservice.
- Add RabbitMQ or Kafka for asynchronous communication.
- Implement CI/CD pipelines for automated deployment.
- Introduce advanced reporting dashboards.

---

## **Contributing**

Feel free to contribute to this project. Fork the repository and submit a pull request with your changes.

---

## **License**

This project is licensed under the [MIT License]().

```

---

This `README.md` provides clear instructions for running the project traditionally and with Docker, catering to different preferences. Let me know if you need further customization!
```
