import threading
import time
import requests
import json

from scheduler_worker.job.utils.message_queue import MessageQueue

class MessageConsumer(threading.Thread):

    payload = None

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        payload = []
        while True:
            qsize = MessageQueue.instance().queue.qsize()
            print(qsize)
            if qsize != 0:
                for i in range(qsize):
                    mesg_dict = MessageQueue.instance().queue.get(True)
                    payload.append(mesg_dict)
                print(payload)
                r = requests.post("http://10.58.47.66:1987/v1/push", data=json.dumps(payload))
                print r.text
                payload =[]

            time.sleep(10)