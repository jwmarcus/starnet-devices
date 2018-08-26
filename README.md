To flash a new chip, do the following:

```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20999999-v9.9.9.bin
```

You can find images here: http://micropython.org/download

Commands for using rshell:

`rshell --port /dev/ttyUSB0`

... will connect you to the board. From there, the filesystem for the ESP8266 Huzzah is mounted at /pyboard/

`rsync esp8266 /pyboard -v`

... will sync contents of your device sub-folder to the chip.
