"""
Derek Graves
05/16/2024
Error Corrections and Refactoring

Message sender / emitter 

Description:
This script sends one message on a named queue.
It will execute and finish. 
You can change the message and run it again in the same terminal.

Remember:
- Use the up arrow to recall the last command executed in the terminal.
"""

# Import from Standard Library
import sys

# Import External packages used
import pika

# Configure logging
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

# ---------------------------------------------------------------------------
# Define program functions (bits of reusable code)
# ---------------------------------------------------------------------------


def send_message(host: str, queue_name: str, message: str):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue

    """

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

        # use the connection to create a communication channel
        ch = conn.channel()

        # use the channel to declare a queue
        ch.queue_declare(queue=queue_name)

        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)

        # log a message for the user
        logger.info(f" [x] Sent {message}")

    except pika.exceptions.AMQPConnectionError as e:
        logger.error(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        if conn.is_open:
            conn.close()


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":

    #Define our variables for ease of use in changing parameters andmessages
    host = "localhost"
    queue_name = "hello"
    message = "Great job on correcting v2!"
    send_message(host, queue_name, message) #Use variables to send message

