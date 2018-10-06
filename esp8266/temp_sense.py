import time
import machine
import onewire, ds18x20

# the device is on GPIO12
dat = machine.Pin(4)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

def get_temps():
    ds.convert_temp()
    time.sleep_ms(750)

    temps = []
    for rom in roms:
        temp = ds.read_temp(rom)
        temp = (temp * 9 / 5) + 32
        temps.append(temp)
    return temps
