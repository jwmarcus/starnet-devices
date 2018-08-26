Commands for using rshell:

`rshell --port /ttyUSB0`

... will connect you to the board. From there, the filesystem for the ESP8266 Huzzah is mounted at /pyboard/

`rsync esp8266 /pyboard -v`

... will sync contents of your device folder to the chip.


