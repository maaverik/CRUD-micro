import pika  # to send messages

params = pika.URLParameters(
    "amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx"
)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received message in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
