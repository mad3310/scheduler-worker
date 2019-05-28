#!/usr/bin/env python
# encoding: utf-8

import requests
import time
import logging

from schedulerworker.job.job_opers.abstract_job_handler import AbstractJobHandler
from schedulerworker.job.utils.file_opers import FileOpers

class HttpRequestAccessInterfaceJobHandler(AbstractJobHandler):


    def __init__(self):
        '''
        constrcutor
        '''

        
    def run(self, **kwargs):
        url = kwargs.get('url')
        http_method = kwargs.get('http_method')
        project_code = kwargs.get('project_code')
        task_name = kwargs.get('task_name')
        assert url
        assert http_method
        assert project_code
        assert task_name
        
        if 'get' == http_method:
            resp = requests.get(url, timeout=2)
        elif 'post' == http_method:
            resp = requests.post(url, timeout=2)
        elif 'delete' == http_method:
            resp = requests.delete(url, timeout=2)
        else:
            resp = requests.put(url, timeout=2)

#        print resp.text
        resp_dict = resp.json()
        result_type = resp_dict.get('resultType')

        value = 0
        if result_type == 'SUCCESS':
            value = 1

        ts = int(time.time())
        metric = ("%s-%s") % (project_code, task_name)
        tags = "project_code:%s,monitor_item:%s" % (project_code, task_name)

        mesg_dict = {
                    "endpoint": "scm-monitor",
                    "metric": metric,
                    "timestamp": ts,
                    "step": 60,
                    "value": value,
                    "counterType": "GAUGE",
                    "tags": tags,
                }

        fo = FileOpers()
        fo.appendJsonToFile('/tmp/scheduler-work-result', mesg_dict)

        logging.debug('message has added to queue.')

        return 'access request has finished and send result to queue'