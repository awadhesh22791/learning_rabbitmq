import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello',durable=True)
    message=''.join(sys.argv[1:]) or 'Hello World'
    channel.basic_publish(exchange='logs',
                            routing_key="",
                            body=message,
                            properties=pika.BasicProperties(
                                delivery_mode=2,#Make message persistent
                            ))
    print(" [x] Sent %r"%message)
    connection.close()
else:
    print("Channel not opened.")