#!/usr/bin/env python2.6.6
#coding:utf-8
import logging
import os

from rq.redis import Redis
from rq import Connection, Queue, Worker
from rq.utils import ColorizingStreamHandler

# Setup logging for RQWorker if not already configured
dirname = os.path.dirname
base_dir = os.path.abspath(dirname(__file__))
config_path = os.path.join(base_dir, "config")
logging.config.fileConfig(config_path + '/logging.conf')

Redis_Properties={
      'REDIS_HOST':'10.150.146.175',
      'REDIS_PORT': 6379,
      'QUEUE_NAME':'webportal_get'
}

def worker_exc_handler(job, exc_type, exc_value, traceback):
    logging.info("%s-%s-%s" %(exc_type, exc_value, traceback))
    
if __name__ == '__main__':
    
    __host = Redis_Properties.get('REDIS_HOST')
    __port = Redis_Properties.get('REDIS_PORT')
    __queue_name = Redis_Properties.get('QUEUE_NAME')

    with Connection(Redis(__host, __port)):
        q = Queue(__queue_name)
        w = Worker(q, exc_handler=worker_exc_handler)
        w.work()