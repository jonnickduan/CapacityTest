#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import ctime
import jpype
import threading
from src.util.config import *
from src.util import const

jvmPath, websrv, utils = get_home()
excel_path = get_excel_path()
device_num, trans_times = get_scheme()


def start_jvm():
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=%s" % websrv + ';' + utils)


def load_service():
    ff = jpype.JClass(const.SERVICEFACTORY)
    ff.SERVICE_BASE_URL = const.SERVICE_BASE_URL
    print(ff.SERVICE_BASE_URL)
    cc = jpype.JClass(const.ACCOUNTSERVICE)
    account_service = ff.getInstance().getService(cc)
    jd = jpype.JClass(const.DEVICEINFODTO)
    device_info_dto = jd()
    device_info_dto.setClientType(jpype.java.lang.Byte(1))
    device_info_dto.setClientVer("1.0")
    device_info_dto.setDeviceName("Lao Duan\'s iphone")
    device_info_dto.setDeviceId("xxx001")
    device_info_dto.setLastLat(None)
    device_info_dto.setLastLng(None)
    device_info_dto.setRelativeId1("channel")
    device_info_dto.setRelativeId2("user_id")

    try:
        customer_dto = account_service.sellerLogin(None, "15727326906", "000000", device_info_dto)
        print(customer_dto.getPhoneNumber())
    except jpype.JException(jpype.java.lang.Exception) as ex:
        print(ex.stacktrace())
   #finally:
    #    jpype.shutdownJVM()


def shutdowm_jvm():
    jpype.shutdownJVM()


if __name__ == '__main__':
    start_jvm()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=load_service))
    for t in threads:
        t.setDaemon(True)
        t.start()
        print("STARTING!!!...")
    t.join()
    shutdowm_jvm()
    print("all over %s" % ctime())

