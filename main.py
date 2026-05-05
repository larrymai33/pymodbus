from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# temperature array
test_temps = [20, 25, 28, 30, 26, 24, 22, 26, 30, 15]

for temp in test_temps:
    # write temp value to initial address
    client.write_register(address=0, value=temp)
    
    time.sleep(0.5)  # let PLC scan a few cycles
    
    # Read fan state from initial address
    result = client.read_coils(address=0, count=1)
    fan_on = result.bits[0] #read first bit returned by coil
    
    print(f"Temp = {temp} degrees  →  Fan = {'ON' if fan_on else 'OFF'}")

client.close()