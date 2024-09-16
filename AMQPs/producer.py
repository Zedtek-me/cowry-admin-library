from kombu import Connection, Producer, Exchange, Queue
from django.conf import settings
from typing import Type
import json
import logging
logger = logging.getLogger("root")
logger.setLevel("DEBUG")


class Publisher:
    '''publishes to the user api when the admin either adds or removes books from the catalogue'''

    def __init__(self):
        self.connection = Connection(settings.BROKER_URL)
        self.connection.connect()
        # creates a default tcp channel for multiplexing
        self.channel = self.connection.channel()

    def get_exchange(self, use_default:bool=True, name=None, _type=None)->Type[Exchange]:
        '''creates and returns an exchange'''
        exchange_name = "library_default_exchange"
        exchange_type = "direct"
        if not use_default:
            exchange_name = name
            exchange_type = _type
        exchange = Exchange(name=exchange_name, type=exchange_type, channel=self.channel, durable=True)
        # explicitly declare the exchange in rabbitmq again
        exchange.declare(channel=self.channel)
        return exchange

    def get_queue(self, routing_key="library.user.api")->Type[Queue]:
        '''creates a default queue for the only remote process that needs to consume message from this producing process'''
        exchange = self.get_exchange(use_default=True)
        queue = Queue(name=routing_key, exchange=exchange, routing_key=routing_key, channel=self.channel, durable=True)
        queue.declare(channel=self.channel)
        return queue

    def get_producer(self)->Type[Producer]:
        '''returns the actual publisher object'''
        return Producer(channel=self.channel, auto_declare=True)
    
    def publish_to_remote_process(self, msg=dict, routing_key:str="library.user.api")->str:
        '''auto-publishes messages to the remote process'''
        exchange = self.get_exchange()
        publisher = self.get_producer()
        if msg is None:
            msg = {}
        logger.debug(f"message to be published...........................!!!!!!!!!!! {msg}")
        publisher.publish(
            body=json.dumps(msg),
            routing_key=routing_key,
            exchange=exchange
        )
        return "message published"
