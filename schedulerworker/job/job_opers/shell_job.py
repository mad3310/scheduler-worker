#!/usr/bin/env python
# encoding: utf-8

from schedulerworker.job.utils.invoke_command import InvokeCommand
from schedulerworker.job.job_opers.abstract_job_handler import AbstractJobHandler

class ShellJobClientHandler(AbstractJobHandler):
    
    def __init__(self):
        pass
    
    def run(self, **kwargs):
        param_dict = kwargs.pop('param_dict')
        shell_name = param_dict.pop('shell_name')
        assert shell_name
        iv = InvokeCommand()
        iv._runSysCmd(shell_name)