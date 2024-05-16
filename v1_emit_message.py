"""
    This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to v1_emit_message.pyvdeclare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body="Check it out on RabbitMQ Management!")

# print a message to the console for the user
print(" Sent [x] body")

# close the connection to the server
conn.close()
