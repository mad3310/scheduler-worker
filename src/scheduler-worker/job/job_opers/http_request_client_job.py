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
        
    def run(self, url):
        assert url
        resp = requests.get(url,timeout=10)
        logging.info(resp.text)
        return resp.text
    