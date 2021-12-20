import json
import os

import django
import pika  # to send messages

# https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters(
    "amqps://zqcciwfx:Lhx-gBIsDPY7eNfYbBKV5UBOhNOx1mu4@puffin.rmq2.cloudamqp.com/zqcciwfx"
)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    id = json.loads(body)
    print(f"Admin received {id}")
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()
    print("Product likes incremented")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
