import pika


class Pub:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.queue = None

    def create_connection(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

    def create_queue(self):
        self.queue = self.channel.queue_declare(queue='order')

    def close_connection(self):
        self.connection.close()

    def pub(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            self.create_connection()
            self.create_queue()
            func(*args, **kwargs)
            self.close_connection()
        return wrapper

    @pub
    def create_order(self, order_id):
        self.channel.basic_publish(exchange='', routing_key='order', body=str(order_id))
