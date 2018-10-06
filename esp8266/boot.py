import esp # disable debug output for rshell.py
esp.osdebug(None)

import device_config # contains sensitive data
import gc, webrepl, network

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
    print('INFO: Network - ', sta_if.ifconfig())

# collect garbage
gc.collect()

# setup and start webrepl
write_repl_config(device_config)
webrepl.start()

# connect to wifi in device_config.py
# TODO: don't block boot sequence
connect(device_config)

# NOTE: from here, the main.py script activates
