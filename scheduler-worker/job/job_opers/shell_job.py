#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2015-2-4

@author: 
'''

from job.utils.invoke_command import InvokeCommand
from job.job_opers.abstract_job_handler import AbstractJobHandler

class ShellJobClientHandler(AbstractJobHandler):
    
    def __init__(self):
        pass
    
    def run(self, **kwargs):
        param_dict = kwargs.pop('param_dict')
        shell_name = param_dict.pop('shell_name')
        assert shell_name
        iv = InvokeCommand()
        iv._runSysCmd(shell_name)