import pika
import time

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.exchange_declare(exchange="logs",exchange_type="fanout")
if channel.is_open:
    print("Channel opened.")
    result=channel.queue_declare(queue='',exclusive=True)
    queue_name=result.method.queue
    channel.queue_bind(exchange="logs",queue=queue_name)
    def callback(ch,method,properties,body):
        print("[x] Recie4ved %r"%body)

    channel.basic_consume(queue=queue_name,
                            on_message_callback=callback,auto_ack=True)
    print('[*] Waiting for messages. To exist CTRL+C')
    channel.start_consuming()
else:
    print("Channel not opened.")