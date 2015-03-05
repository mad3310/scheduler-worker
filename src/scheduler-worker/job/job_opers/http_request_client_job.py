#!/usr/bin/env python 2.6.6
#-*- coding: utf-8 -*-

'''
Created on 2015-2-4

@author: 
'''
import requests
import logging

from job.job_opers.abstract_job_handler import AbstractJobHandler

class HttpRequestJobClientHandler(AbstractJobHandler):
    
    def __init__(self):
        '''
        constrcutor
        '''
        
    def run(self, param):
        url = param.get('url')
        http_method = param.get('http_method')
        assert url
        assert http_method
        
        if 'get' == http_method:
            resp = requests.get(url,timeout=2)
        elif 'post' == http_method:
            resp = requests.post(url, timeout=2)
        elif 'delete' == http_method:
            resp = requests.delete(url, timeout=2)
        else:
            resp = requests.put(url, timeout=2)
        
        return resp.text
    