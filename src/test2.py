#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import time
import pp




ppservers = ()
if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    job_server = pp.Server(ppservers=ppservers)

print("Starting pp with", job_server.get_ncpus(), "workers")

start_time = time.time()
inputs = ('15727326906','13910600000')
jobs = [(input, job_server.submit(test_login,(input,))) for input in inputs]
for input, job in jobs:
    print("test_login", input, "is", job())

print("Time elapsed: ", time.time() - start_time, "s")
job_server.print_stats()
