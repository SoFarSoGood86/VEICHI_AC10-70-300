from pymodbus.client import ModbusTcpClient

class VeichiHub:
    def __init__(self, host, port, slave):
        self.client = ModbusTcpClient(host=host, port=port)
        self.slave = slave

    def connect(self):
        return self.client.connect()

    def read(self, address):
        rr = self.client.read_holding_registers(address, 1, slave=self.slave)
        return rr.registers[0] if rr and not rr.isError() else None

    def write(self, address, value):
        return self.client.write_register(address, value, slave=self.slave)
