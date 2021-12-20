# amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx

import pika  # to send messages

params = pika.URLParameters(
    "amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx"
)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Received message in main")
    print(body)


channel.basic_consume(queue="main", on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()
