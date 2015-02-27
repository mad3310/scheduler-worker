#!/usr/bin/env python 2.6.6
#-*- coding: utf-8 -*-

'''
Created on 2015-2-4

@author: 
'''
import requests

from job.job_opers.abstract_job_handler import AbstractJobHandler

class HttpRequestJobClientHandler(AbstractJobHandler):
    
    def __init__(self):
        '''
        constrcutor
        '''
        
    def run(self, url):
        assert url
        resp = requests.get(url)
        '''
        @todo: logging
        '''
        print resp.text
        return resp.text
    