from dataclasses import dataclass

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/main"

db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    # autoincrement False because product will be created in admin app and sent here
    # from RabbitMQ, so id will be different
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


@app.route("/api/products")
def index():
    return jsonify(Product.query.all())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
