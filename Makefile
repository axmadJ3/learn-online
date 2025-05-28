up:
	docker-compose -f docker-compose.yml -d

down:
	docker-compose - docker-compose.yml down && docker network prune --force
