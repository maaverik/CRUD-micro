# CRUD items

This is a very simple application that consists of two microservices (admin and main) with a UI and a RabbitMQ instance for communication that allows CRUD operations and adding likes for items.

1. admin app - This app takes care of CRUD operations on products, something that admins normally do. It is a microservice built with Django with a MySQL db and a RabbitMQ channel for communication with the main app.

1. main app - This app allows non-admin users to like specific items that are created by admins. It is microservice built with Flask with a MySQL db and a RabbitMQ instance similar to the admin app.

<https://cloudamqp.com> can be used to easily run a RabbitMQ instance to work with this app.
