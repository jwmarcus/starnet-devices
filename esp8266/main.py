import temp_sense
import blink_light

import urequests as requests

temps = temp_sense.get_temps()
print(temps)


url = "http://starnet.jwmarcus.com/records/add/"
data="device_key=12345&field=chill&data={}".format(temps[0])
headers={'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, data=data, headers=headers)
print(r.text)


# for _ in range(300):
#     blink_light.demo(blink_light.np)
