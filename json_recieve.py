#!/usr/bin/env python
import pika
import json
credentials = pika.PlainCredentials(username='test', password='test')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.34', credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    # print(" [x] %r" % body)
    data = json.loads(body)
    for p in data['user']:
        id_number = p['id']
    with open('users/{}.json'.format(id_number), 'w') as outfile:
        json.dump(data, outfile)
    print("Veri alındı")
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
