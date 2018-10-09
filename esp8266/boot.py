import esp # disable debug output for rshell.py
esp.osdebug(None)

import device_config # contains sensitive data, scopes
import gc, webrepl, network
import utime as time

config_repl = device_config.config_repl
config_array = device_config.config_array

def write_repl_config(config):
    contents = "PASS = '{}'\n".format(config)
    f = open("webrepl_cfg.py", "w")
    f.write(contents)
    f.close()

def connect(config):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        for net_config in config:
            sta_if.connect(net_config['ssid'], net_config['psk'])
            for _ in range(6): # try for 5 cycles
                print("INFO: Connecting to {}".format(net_config['ssid']))
                if not sta_if.isconnected():
                    time.sleep(3)
                else:
                    print('INFO: Network - ', sta_if.ifconfig())
                    print("INFO: Connected to {}".format(net_config['ssid']))
                    return
            print("Could not connect to network {}".format(net_config['ssid']))
    else:
        print('INFO: Network - ', sta_if.ifconfig())

# collect garbage
gc.collect()

# setup and start webrepl
write_repl_config(config_repl) # imported from device_config
webrepl.start()

# connect to wifi in device_config.py
# TODO: don't block boot sequence
connect(config_array) # imported from device_config

# NOTE: from here, the main.py script activates
