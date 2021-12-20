# amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx

import pika  # to send messages

params = pika.URLParameters(
    "amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx"
)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()


def publish(method, body):
    channel.basic_publish(exchange="", routing_key="admin", body="hello")
