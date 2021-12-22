import json
import os

import pika  # to send messages

if "RABBITMQ_URL" not in os.environ:
    # Put RabbitMQ URLParameters in an env variable called RABBITMQ_URL
    raise ValueError("Please set RABBITMQ_URL environment variable")

rabbitmq_url = os.environ["RABBITMQ_URL"]

params = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )
