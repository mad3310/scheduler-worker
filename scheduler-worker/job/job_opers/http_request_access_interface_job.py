#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2015-2-4

@author: 
'''

import requests
import time
import json

from scheduler-worker.job.job_opers.abstract_job_handler import AbstractJobHandler

class HttpRequestAccessInterfaceJobHandler(AbstractJobHandler):
    
    def __init__(self):
        '''
        constrcutor
        '''
        
    def run(self, **kwargs):
        param_dict = kwargs.pop('param_dict')
        url = param_dict.pop('url')
        http_method = param_dict.pop('http_method')
        assert url
        assert http_method
        
        if 'get' == http_method:
            resp = requests.get(url, timeout=2)
        elif 'post' == http_method:
            resp = requests.post(url, timeout=2)
        elif 'delete' == http_method:
            resp = requests.delete(url, timeout=2)
        else:
            resp = requests.put(url, timeout=2)

        ts = int(time.time())
        payload = [
            {
                "endpoint": "test-endpoint",
                "metric": "test-metric",
                "timestamp": ts,
                "step": 60,
                "value": 1,
                "counterType": "GAUGE",
                "tags": "idc=lg,loc=beijing",
            },
        ]

        r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

        print r.text

        return resp.text