#!/usr/bin/python
# -*- coding:utf-8 -*-
import pp
import sys
import time

def test_login(phone_number):
    from pyhessian.client import HessianProxy
    service = HessianProxy("https://dev.188yd.com/services/AccountService")
    device_info_dto = {
        'clientType':1,
        'clientVer':'1.0',
        'deviceName':'Lao Duan\'s iphone',
        'deviceId':'xxx001',
        'lastLat':0.00,
        'lastLng':0.00,
        'relativeId1':'channel',
        'relativeId2':'user_id'
    }
    customerDTO = service.sellerLogin(None, phone_number, "000000", device_info_dto)
    print(customerDTO.phoneNumber)


ppservers = ()
if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)
else:
    job_server = pp.Server(ppservers=ppservers)

print("Starting pp with", job_server.get_ncpus(), "workers")

start_time = time.time()
inputs = ('13910625431','15727326906')
jobs = [(input, job_server.submit(test_login,(input,))) for input in inputs]
for input, job in jobs:
    print("test_login", input, "is", '')

print("Time elapsed: ", time.time() - start_time, "s")
#job_server.print_stats()


