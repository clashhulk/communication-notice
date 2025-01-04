# Communication Notice System

A scalable microservices-based system for managing notices, organizations, and multi-channel communication. This project supports modular microservices with a single PostgreSQL database (for now) and a React.js frontend.

## **Project Overview**

This project handles the creation, management, and communication of notices through multiple channels (Email, SMS, WhatsApp, RPAD). It is built using the following architecture:

- **Microservices**: Separate Django services for Users, Notices, Communication, and Reporting.
- **Database**: A single shared PostgreSQL instance for all services.
- **Frontend**: React.js for UI, interacting with backend REST APIs.
- **Containerization**: Docker and Docker Compose for orchestrating services.

---

## **Features**

- **User Management**: Manage users, roles, and organizations.
- **Notice Management**: Create, update, and track notices with dynamic data fields.
- **Communication Service**: Queue-based communication logs for Email, WhatsApp, SMS, and RPAD.
- **Reporting**: Track delivery statuses, user actions, and system audits.
- **Scalability**: Modular services that can transition to independent databases in the future.

---

## **Tech Stack**

### Backend:

- **Django**: Backend framework for each microservice.
- **Django REST Framework (DRF)**: To expose REST APIs.
- **PostgreSQL**: Database for persistent storage.

### Frontend:

- **React.js**: Frontend UI consuming the REST APIs.

### Deployment:

- **Docker & Docker Compose**: Containerization and orchestration.

---

## **Directory Structure**

```plaintext
communication-notice/
├── docker-compose.yml         # Orchestrates all services
├── Makefile                   # Automates common tasks
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

### Prerequisites

- Python 3.9+
- Node.js (for React.js frontend)
- PostgreSQL
- Docker & Docker Compose

---

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/clashhulk/communication-notice.git
cd communication-notice
```

---

### **Step 2: Set Up Environment Variables**

Create a `.env` file in the project root and add the following:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=communication_notice
DB_USER=your_user
DB_PASSWORD=your_password
```

---

### **Step 3: Build and Start Services**

Build and start all services using Docker Compose:

```bash
docker-compose up --build
```

---

### **Step 4: Apply Migrations**

Run migrations for all services:

```bash
make migrate-user
make migrate-notice
make migrate-communication
make migrate-reporting
```

---

### **Step 5: Access Services**

Each service is exposed on different ports:

- **User Service**: `http://localhost:8000`
- **Notice Service**: `http://localhost:8001`
- **Communication Service**: `http://localhost:8002`
- **Reporting Service**: `http://localhost:8003`

---

### **Step 6: Frontend Setup**

Navigate to the React frontend directory (if available) and start the development server:

```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000`.

---

## **How to Use**

### API Endpoints

#### **User Service**

- `GET /api/users/`: List all users.
- `POST /api/users/`: Create a new user.

#### **Notice Service**

- `GET /api/notices/`: List all notices.
- `POST /api/notices/`: Create a new notice.

#### **Communication Service**

- `POST /api/communications/`: Queue a communication log.

#### **Reporting Service**

- `GET /api/reports/`: Generate reports.

---

## **Development Workflow**

### Common Commands (Using Makefile)

- **Start all services**:
  ```bash
  make up
  ```
- **Stop all services**:
  ```bash
  make down
  ```
- **View logs**:
  ```bash
  make logs
  ```
- **Clean Docker environment**:
  ```bash
  make clean
  ```

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

This project is licensed under the [MIT License](LICENSE).

```

---

This file is now fully copy-paste ready. Let me know if you’d like to make any further adjustments!
```

# Communication Notice System

A scalable microservices-based system for managing notices, organizations, and multi-channel communication. This project supports modular microservices with a single PostgreSQL database (for now) and a React.js frontend.

## **Project Overview**

This project handles the creation, management, and communication of notices through multiple channels (Email, SMS, WhatsApp, RPAD). It is built using the following architecture:

- **Microservices**: Separate Django services for Users, Notices, Communication, and Reporting.
- **Database**: A single shared PostgreSQL instance for all services.
- **Frontend**: React.js for UI, interacting with backend REST APIs.
- **Containerization**: Docker and Docker Compose for orchestrating services.

---

## **Features**

- **User Management**: Manage users, roles, and organizations.
- **Notice Management**: Create, update, and track notices with dynamic data fields.
- **Communication Service**: Queue-based communication logs for Email, WhatsApp, SMS, and RPAD.
- **Reporting**: Track delivery statuses, user actions, and system audits.
- **Scalability**: Modular services that can transition to independent databases in the future.

---

## **Tech Stack**

### Backend:

- **Django**: Backend framework for each microservice.
- **Django REST Framework (DRF)**: To expose REST APIs.
- **PostgreSQL**: Database for persistent storage.

### Frontend:

- **React.js**: Frontend UI consuming the REST APIs.

### Deployment:

- **Docker & Docker Compose**: Containerization and orchestration.

---

## **Directory Structure**

```plaintext
communication-notice/
├── docker-compose.yml         # Orchestrates all services
├── Makefile                   # Automates common tasks
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
