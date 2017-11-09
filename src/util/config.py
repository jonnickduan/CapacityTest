#!/usr/bin/python
# -*- coding:utf-8 -*-
import codecs
import configparser
import os


os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath("config.py")))) + "/cfg")
config = configparser.ConfigParser()
#cfg_file = open("env_cfg.ini", "r", encoding='utf8')
cfg_file = codecs.open("env_cfg.ini", "r", "utf-8-sig")
config.read_file(cfg_file)
cfg_file.close()

def get_home():
    return config.get('homes', 'jvm_location'), config.get('homes', 'websrv'), config.get('homes', 'utils')

def get_excel_path():
    return config.get('excels', 'excel_location')

def get_scheme():
    return config.get('scheme', 'device_num'), config.get('scheme', 'trans_times')

def get_jar_name():
    return config.get('jar_name', 'websrv'), config.get('jar_name', 'utils')
