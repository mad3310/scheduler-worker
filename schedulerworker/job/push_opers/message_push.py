import threading
import time
import requests
import json

from schedulerworker.job.utils.file_opers import FileOpers


class MessageConsumer(threading.Thread):

    payload = None

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        fo = FileOpers()
        while True:
            payload = fo.loadFiletoJson('/tmp/scheduler-work-result')
            print payload
            if not payload == []:
                r = requests.post("http://10.58.47.66:1987/v1/push", data=json.dumps(payload))
                print r.text

            time.sleep(10)