dev:
	docker build --network=host -t ekoi-api .
	docker compose up

down:
	docker compose down	
