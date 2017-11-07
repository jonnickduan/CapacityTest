#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import with_statement
import configparser
import os


class Config(object):
    def __init__(self):
        os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("config.py")))) + "/cfg")
        self.config = configparser.ConfigParser()
        self.file = open("env_cfg.ini", "r")
        self.config.read_file(open("env_cfg.ini", "r"))

    def get_java_location(self):
        return self.config.get('homes', 'jvm_location')

    def get_lib_location(self):
        return self.config.get('homes', 'lib_location')

if __name__ == '__main__':
    config = Config()
    jvm_location = config.get_java_location()
    lib_location = config.get_lib_location()
    print(jvm_location)
    print(lib_location)
