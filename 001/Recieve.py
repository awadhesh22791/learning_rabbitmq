import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
if channel.is_open:
    print("Channel opened.")
    channel.queue_declare(queue='hello')
    def callback(ch,method,properties,body):
        print("[x] Recie4ved %r"%body)

    channel.basic_consume(queue="hello",
                            on_message_callback=callback,
                            auto_ack=True)
    print('[*] Waiting for messages. To exist CTRL+C')
    channel.start_consuming()
else:
    print("Channel not opened.")