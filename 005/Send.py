import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.exchange_declare(exchange='topic_logs',exchange_type='topic')
if channel.is_open:
    print("Channel opened.")
    routing_key=sys.argv[1] if len(sys.argv)>1 else 'anonymous.info'
    message=''.join(sys.argv[2:]) or 'Hello World'
    channel.basic_publish(exchange='topic_logs',
                            routing_key=routing_key,
                            body=message)
    print(" [x] Sent %r: %r"%(routing_key,message))
    connection.close()
else:
    print("Channel not opened.")