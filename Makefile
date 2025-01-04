# Define variables
COMPOSE = docker-compose

# Commands
up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

build:
	$(COMPOSE) build

restart:
	$(COMPOSE) down
	$(COMPOSE) up -d

logs:
	$(COMPOSE) logs -f

ps:
	$(COMPOSE) ps

clean:
	$(COMPOSE) down --volumes --remove-orphans

migrate-user:
	docker exec -it user_service python manage.py makemigrations
	docker exec -it user_service python manage.py migrate

migrate-notice:
	docker exec -it notice_service python manage.py makemigrations
	docker exec -it notice_service python manage.py migrate

migrate-communication:
	docker exec -it communication_service python manage.py makemigrations
	docker exec -it communication_service python manage.py migrate

migrate-reporting:
	docker exec -it reporting_service python manage.py makemigrations
	docker exec -it reporting_service python manage.py migrate
