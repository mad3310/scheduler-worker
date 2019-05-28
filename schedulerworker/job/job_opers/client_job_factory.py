#!/usr/bin/env python
# encoding: utf-8

'''
Created on Feb 23, 2015

@author: root
'''
import logging

from schedulerworker.job.job_opers.http_request_job import HttpRequestJobClientHandler
from schedulerworker.job.job_opers.shell_job import ShellJobClientHandler
from schedulerworker.job.job_opers.http_request_access_interface_job import HttpRequestAccessInterfaceJobHandler



job_handler_dict = {
    'httpRequest': HttpRequestJobClientHandler(),
    'shellRequest': ShellJobClientHandler(),
    'httpRequestAccessInterface' : HttpRequestAccessInterfaceJobHandler()
}

def client_job_run (**kwargs):

    job_type = kwargs.get('job_type')
    
    if job_type is None:
        raise Exception("job_model should be not null!")
    
    if job_type not in ['httpRequest', 'shellRequest', 'httpRequestAccessInterface']:
        raise Exception("job type is error,please specify the right type.\
                            [httpRequest,shellRequest]")
    
    _job_handler = job_handler_dict.get(job_type)
    result = _job_handler.run(**kwargs)

    logging.debug(result)