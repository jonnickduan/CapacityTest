#!/usr/bin/python
# -*- coding:utf-8 -*-


class Seller(object):
    def __init__(self, phone_number, device_info_dto, hessian_proxy):
        self.phone_number = phone_number
        self.device_info_dto = device_info_dto
        self.hessian_proxy = hessian_proxy

    def test_login(self):
        from mustaine.client import HessianProxy
        service = HessianProxy(self.hessian_proxy)
        device_info_dto = {
            'clientType': 1,
            'clientVer': '1.0',
            'deviceName': 'LaoDuan\'s iphone',
            'deviceId': 'xxx001',
            'lastLat': 0.00,
            'lastLng': 0.00,
            'relativeId1': 'channel',
            'relativeId2': 'user_id'
        }
        try:
            service.sellerLogin(None, self.phone_number, "000000", device_info_dto)
        except Exception, ex:
            print('Input: ' + self.phone_number + 'Error:' + ex.message)
