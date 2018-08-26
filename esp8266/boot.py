import esp # to disable debug output
esp.osdebug(None)

import device_config # user module
import gc
import webrepl
import network
import temp_sense

def write_repl_config(config):
    contents = "PASS = '{}'\n".format(config.repl)
    f = open("webrepl_cfg.py", "w")
    f.write(contents)
    f.close()

def connect(config):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(config.ssid, config.psk)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# init tasks
write_repl_config(device_config)
webrepl.start()
gc.collect()
connect(device_config)

temps = temp_sense.get_temps()
print(temps)
