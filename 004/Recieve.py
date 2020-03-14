import pika
import sys

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.exchange_declare(exchange="logs",exchange_type="direct")
if channel.is_open:
    print("Channel opened.")
    result=channel.queue_declare(queue='',exclusive=True)
    queue_name=result.method.queue
    severities=sys.argv[1:]
    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n"%sys.argv[0])
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(exchange="logs",queue=queue_name,routing_key=severity)
    print('[*] Waiting for messages. To exist CTRL+C')
    def callback(ch,method,properties,body):
        print("[x] %r:%r" % (method.routing_key,body.decode("utf-8")))

    channel.basic_consume(queue=queue_name,
                            on_message_callback=callback,auto_ack=True)
    
    channel.start_consuming()
else:
    print("Channel not opened.")