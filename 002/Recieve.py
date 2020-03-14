import pika
import time

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello',durable=True)
    def callback(ch,method,properties,body):
        print("[x] Recie4ved %r"%body)
        time.sleep(body.count(b'.'))
        print('[x] Done')
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="hello",
                            on_message_callback=callback)
    print('[*] Waiting for messages. To exist CTRL+C')
    channel.start_consuming()
else:
    print("Channel not opened.")