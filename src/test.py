#!/usr/bin/python
# -*- coding:utf-8 -*-
import jpype


jvmPath = jpype.getDefaultJVMPath()
print("jvmPath = " + jvmPath)

ext_classpath = "D:/workspace/andrclientlib-1.0.jar;D:/workspace/account-contract-1.0.jar"
# ext_classpath = "D:/workspace"
# jvmArg = "-Djava.class.path=%s" % ext_classpath
if not jpype.isJVMStarted():
    # jpype.startJVM(jvmPath, jvmArg)
    jpype.startJVM(jvmPath, "-Xms32m", "-Xmx256m", "-mx256m", "-Djava.class.path=%s" % ext_classpath)
    print("ok")

ff = jpype.JClass("com.x.mymall.andrclient.ServiceFactory")
fc = ff.getInstance()
cc = jpype.JClass("com.x.mymall.account.contract.service.AccountService")
fs = fc.getService(cc)


'''
AccountService = jpype.JPackage(ext_classpath).com.x.mymall.account.contract.service.AccountService
aaa = jpype.JPackage("com").x.mymall.account.contract.dto
jd = jpype.JClass("com.x.mymall.account.contract.dto.DeviceInfoDTO")
dd = jd()
dd.setDeviceId("lao duan")
print(dd.getDeviceId())
'''






#dd = cc()

# jpype.JClass("AccountService")
# 获取Class的name，并执行java方法
# javaClass = jpype.JClass("com.x.mymall.account.contract.service.AccountService")
# jpype.JPackage("jpype").JpypeDemo()
# javaInstance = jav aClass()

jpype.shutdownJVM()
