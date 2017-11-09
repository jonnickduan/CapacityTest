#!/usr/bin/python
# -*- coding: UTF-8 -*-

class _const:
    class ConstError(TypeError):pass
    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name]=value
import sys
sys.modules[__name__] = _const()

_const.SERVICEFACTORY = 'com.x.mymall.andrclient.ServiceFactory'
_const.SERVICE_BASE_URL = 'https://dev.188yd.com/services/'
_const.ACCOUNTSERVICE = 'com.x.mymall.account.contract.service.AccountService'
_const.DEVICEINFODTO = 'com.x.mymall.account.contract.dto.DeviceInfoDTO'
_const.CUSTOMERDTO = 'com.x.mymall.account.contract.dto.CustomerDTO'
