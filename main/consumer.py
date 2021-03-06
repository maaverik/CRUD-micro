
import json
import os

import pika  # to send messages

from main import Product, db

if "RABBITMQ_URL" not in os.environ:
    # Put RabbitMQ URLParameters in an env variable called RABBITMQ_URL
    raise ValueError("Please set RABBITMQ_URL environment variable")

rabbitmq_url = os.environ["RABBITMQ_URL"]

params = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(params)  # connection with RabbitMQ
channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Main received {data}")

    match properties.content_type:
        case "product_created":
            product = Product(
                id=data["id"],
                title=data["title"],
                image=data["image"],
                likes=data["likes"],
            )
            db.session.add(product)
            db.session.commit()
            print('Product created')
        case "product_updated":
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
            print('Product updated')
        case "product_deleted":
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product deleted')


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
