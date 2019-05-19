#!/usr/bin/env python
# encoding: utf-8

'''
Created on 2015-2-4

@author: 
'''

from abc import abstractmethod

class AbstractJobHandler (object) :

    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError, "Cannot call abstract method"

    @abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError, "Cannot call abstract method"

    @abstractmethod
    def stop(self, **kwargs):
        raise NotImplementedError, "Cannot call abstract method"

    @abstractmethod
    def destroy(self, **kwargs):
        raise NotImplementedError, "Cannot call abstract method"

