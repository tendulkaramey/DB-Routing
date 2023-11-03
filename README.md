# DB Router: Route DB Requests

Project demonstrates how we can implement database routing in  Django framework,  to route read requests to replicas and write requests to primary database.

## Project Brief

Suppose we are a globalmart and our main job is a marketplace where people can search, compare and buy things online. we expect a lot of search/read queries during peak time, to handle this we decided to create read replicas and route read requests to those replicas and write requests to primary database. <br><br>

This is a POC (proof of concept) project aimed to learn and implement system design concepts from real life problem statements.

## Setting up

### setup log: create directory 'logs' before running

1. docker-compose up 
2. run migrations on primary db:docker-compose exec webserver python manage.py migrate --database=primary
3. populate data into database: docker-compose exec webserver python manage.py populatedb
4. generate backups of primary database and restore into replicas (still learning how to setup auto sync from master to replicas)
5. generate backup sql file: docker-compose exec db pg_dump -U postgres -d globalmart -f /backup.sql
6. copy into ur machine: docker cp db-master-globalmart:/backup.sql "your machine path"
7. copy this file into replicas: docker cp "machine path" db-replica1-globalmart:/backup.sql
8. restore sql file into replicas:docker-compose exec db-replica1 psql -U postgres -d globalmart -a -f /backup.sql
9. you can use pgadmin tool to login and view your databases. username and password is in docker-compose file. it works on port 5051.

## Running

Hit the following GET Api: http://localhost:8000/api/products-by-category?category=4&page=1
<br>
you can change the paramters.

<p>Observe the results in the terminal or in the log file, you can check which db the query went: replica1 or replica2.</p>

<p>I have created a small test file which runs 'N' nos of api requests, so we can see the queries going to replicas under load.
file: dbroutertest.py, run this file outside the container</p>

## Results

[Shows Queries going to database in Round Robin Manner](https://drive.google.com/file/d/1mo1XB-78h3uNtLVO8EQeAgL1QPtoriZD/view?usp=sharing)
