#!/usr/bin/env python2.6.6
#coding:utf-8
import logging

from rq.redis import Redis
from rq import Connection, Queue, Worker
from rq.utils import ColorizingStreamHandler

# Setup logging for RQWorker if not already configured
logger = logging.getLogger('rq.worker')
if not logger.handlers:
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s %(message)s',
    datefmt='%H:%M:%S')
    handler = ColorizingStreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

Redis_Properties={
      'REDIS_HOST':'10.150.146.175',
      'REDIS_PORT': 6379,
      'QUEUE_NAME':'webportal_get'
}

def my_handler(job, exc_type, exc_value, traceback):
    logging.info("%s-%s-%s" %(exc_type, exc_value, traceback))
    
if __name__ == '__main__':
    
    __host = Redis_Properties.get('REDIS_HOST')
    __port = Redis_Properties.get('REDIS_PORT')
    __queue_name = Redis_Properties.get('QUEUE_NAME')

    with Connection(Redis(__host, __port)):
        q = Queue(__queue_name)
        w = Worker(q, exc_handler=my_handler)
        w.work()