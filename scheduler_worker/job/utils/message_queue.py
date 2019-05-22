#!/usr/bin/env python
# encoding: utf-8

import Queue
import threading

class MessageQueue(object):

    bucket = Queue.Queue(120)

    write_lock = threading.Lock()

    read_lock = threading.Lock()

    # Global lock for creating global IOLoop instance
    _instance_lock = threading.Lock()

    @property
    def queue(self):
        return self.bucket

    @property
    def queuesize(self):
        print(self.bucket.qsize())
        return self.bucket.qsize()

    def empty(self):
        result = False

        self.read_lock.acquire()
        try:
            result = self.bucket.empty()
        except Queue.Empty:
            pass
        finally:
            self.read_lock.release()

        return result

    def get(self, block=False):
        self.read_lock.acquire()
        try:
            if not self.bucket.empty():
                data = self.bucket.get(block)
        except Queue.Empty:
            pass
        finally:
            self.read_lock.release()

        return data

    def put(self, message):
        self.write_lock.acquire()
        try:
            self.bucket.put(message)
        finally:
            self.write_lock.release()


    @staticmethod
    def instance():
        """Returns a global `IOLoop` instance.
        Most applications have a single, global `IOLoop` running on the
        main thread.  Use this method to get this instance from
        another thread.  In most other cases, it is better to use `current()`
        to get the current thread's `IOLoop`.
        """
        if not hasattr(MessageQueue, "_instance"):
            with MessageQueue._instance_lock:
                if not hasattr(MessageQueue, "_instance"):
                    # New instance after double check
                    MessageQueue._instance = MessageQueue()
        return MessageQueue._instance