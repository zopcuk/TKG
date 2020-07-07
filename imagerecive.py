#!/usr/bin/env python

import pika

f = open("recieving.png", "wb")

credentials = pika.PlainCredentials(username='test1', password='test1')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.201', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    # print(" [x] %r" % body)

    f.write(body)

    f.close()

    print(str("image has been recieved"))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
