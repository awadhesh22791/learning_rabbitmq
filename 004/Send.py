import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='direct')
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello',durable=True)
    severity=sys.argv[1] if len(sys.argv)>1 else 'info'
    message=''.join(sys.argv[2:]) or 'Hello World'
    channel.basic_publish(exchange='logs',
                            routing_key=severity,
                            body=message,
                            properties=pika.BasicProperties(
                                delivery_mode=2,#Make message persistent
                            ))
    print(" [x] Sent %r: %r"%(severity,message))
    connection.close()
else:
    print("Channel not opened.")