#!/usr/bin/env python
import pika
import sys
import logging

f=open("sending.png","rb")
i=f.read()

credentials = pika.PlainCredentials(username='test', password='test')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: image has been send!"
channel.basic_publish(exchange='logs', routing_key='', body=i)
channel.basic_publish(exchange='logs', routing_key='', body=i)
print(" [x] Sent %r" % message)
connection.close()