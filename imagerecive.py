#!/usr/bin/env python

import pika



credentials = pika.PlainCredentials(username='test', password='test')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.10', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    # print(" [x] %r" % body)
    f = open("recieving.png", "wb")
    f.write(body)

    f.close()

    print(str("image has been recieved"))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
