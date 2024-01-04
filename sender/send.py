import pika
import time
import sys

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=pika.PlainCredentials('koast', 'koast')))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    message = "Hello, RabbitMQ!"
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")

    connection.close()

while True:
    send_message()
    time.sleep(5)  # 5초마다 메시지 전송
