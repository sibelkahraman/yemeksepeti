import pika
import json


class Sub:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.order_list = []

    def create_connection(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def create_queue(self):
        self.channel.queue_declare(queue='order', durable=True, passive=True)

    def close_connection(self):
        self.connection.close()

    def sub(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            self.create_connection()
            self.create_queue()
            return func(*args, **kwargs)
        return wrapper

    @sub
    def consumer(self):
        orders = []
        for method, properties, body in self.channel.consume('order', inactivity_timeout=5):
            if body:
                orders.append(json.loads(body))
                self.channel.basic_ack(delivery_tag=method.delivery_tag)
            elif not body:
                self.close_connection()
                return orders
