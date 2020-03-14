import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello')
    message=''.join(sys.argv[1:]) or 'Hello World'
    channel.basic_publish(exchange='',
                            routing_key="hello",
                            body=message)
    print(" [x] Sent %r"%message)
    connection.close()
else:
    print("Channel not opened.")