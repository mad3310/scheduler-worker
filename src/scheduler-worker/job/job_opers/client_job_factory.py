'''
Created on Feb 23, 2015

@author: root
'''
from job.job_opers.http_request_client_job import HttpRequestJobClientHandler
from job.job_opers.shell_client_job import ShellJobClientHandler

def client_job_run(job_type, param_dict):
    
    if job_type is None:
        raise Exception("job_model should be not null!")
        
    if "httpRequest" == job_type:
        url = param_dict.get('url')
        _job_handler = HttpRequestJobClientHandler()
        _job_handler.run(url)
    elif "shellRequest" == job_type:
        shell_name = param_dict.get('shell_name')
        _job_handler = ShellJobClientHandler()
        _job_handler.run(shell_name)
    else:
        raise Exception("job type is error,please specify the right type.\
                            [httpRequest,shellRequest]")
    