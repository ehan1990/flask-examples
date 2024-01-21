health:
	@curl -s localhost:8080/healthcheck | jq

db-up:
	docker run --name db -p 27017:27017 -v persistence:/data/db -d mongo mongod

