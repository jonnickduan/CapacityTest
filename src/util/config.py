#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import with_statement
import configparser

config = configparser.ConfigParser()
with open("env_cfg.ini", "rw") as config_file:
    config.read_file(config_file)
