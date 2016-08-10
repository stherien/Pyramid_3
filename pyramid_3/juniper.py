from jnpr.junos import Device
from lxml import etree

class MyDevice():
    def __init__(self, host):
        self.host = host
        self.device = Device(host=self.host)

    def open(self):
        self.device.open()

    def close(self):
        self.device.close()

    def get_software_information(self):
        self.sw = self.device.rpc.get_software_information()

    def print_software_information(self):
        print(etree.tostring(self.sw))


