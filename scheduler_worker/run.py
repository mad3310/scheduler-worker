#!/usr/bin/env python
#coding:utf-8
import logging
import logging.config
import os

from redis import Redis
from rq import Connection, Queue, Worker
from scheduler_worker.job.push_opers.message_push import MessageConsumer

# Setup logging for RQWorker if not already configured
dirname = os.path.dirname
base_dir = os.path.abspath(dirname(__file__))
config_path = os.path.join(base_dir, "config")
logging.config.fileConfig(config_path + '/logging.conf')

Redis_Properties = {
      'REDIS_HOST': '127.0.0.1',
      'REDIS_PORT': 6379,
      'QUEUE_NAME': 'task_http'
}

def worker_exc_handler(job, exc_type, exc_value, traceback):
    logging.info("%s-%s-%s" % (exc_type, exc_value, traceback))
    print("%s-%s-%s" % (exc_type, exc_value, traceback))


def main():

    mc = MessageConsumer()
    mc.start()

    __host = Redis_Properties.get('REDIS_HOST')
    __port = Redis_Properties.get('REDIS_PORT')
    __queue_name = Redis_Properties.get('QUEUE_NAME')

    with Connection(Redis(__host, __port)):
        q = Queue(__queue_name)
        w = Worker(q, exc_handler=worker_exc_handler)
        w.work()


    
if __name__  ==  '__main__':
    main()