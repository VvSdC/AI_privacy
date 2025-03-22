from service.__init__ import *
import ipaddress
import re

class IpAddressRecognizer:

    @staticmethod
    def verify(ip_address):
        ip_address = ip_address.strip()
        try:
            ip_object = ipaddress.ip_address(ip_address)
            if ip_object.version == 4 or ip_object.version == 6:
                return True
            return False
        except ValueError:
            return False
