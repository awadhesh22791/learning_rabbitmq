import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                            routing_key="hello",
                            body="Hello world1")
    print(" [x] Sent 'Hello world'")
    connection.close()
else:
    print("Channel not opened.")