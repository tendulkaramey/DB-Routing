# DB Router: Route DB Requests

Project demonstrates how we can implement database routing in  Django framework,  to route read requests to replicas and write requests to primary database.

## Project Brief

Suppose we are a globalmart and our main job is a marketplace where people can search, compare and buy things online. we expect a lot of search/read queries during peak time, to handle this we decided to create read replicas and route read requests to those replicas and write requests to primary database. <br><br>

This is a POC (proof of concept) project aimed to learn and implement system design concepts from real life problem statements.

## Setting up

We are using docker to setup and run the project, so it should not take time to setup and make this project running on your machine.