import paho.mqtt.client as mqtt
from random import randint
import time
import sys


class Publisher:
    _device_name: str = "unsupported device"
    _topic: str = ""

    def __init__(self, device_name: str):
        self._device_name = device_name
        self._topic = "/devices/" + self._device_name + "/temperature"

    def _connect(self, client, userdata, flags, rc):
        print("connected " + mqtt.connack_string(rc))

    def _publish(self, client, userdata, mid):
        print("published mid='%s' on topic '%s'" % (mid, self._topic))

    def run(self):
        print("run publisher for '%s'" % self._device_name)

        client = mqtt.Client("temperature")

        client.on_publish = self._publish
        client.on_connect = self._connect

        client.connect("localhost")
        client.loop_start()

        iter: int = 1000
        while iter > 0:
            iter -= 1
            message = "%d.%d" % (randint(0, 100), randint(0, 9))

            client.publish(self._topic, message)

            time.sleep(1)
        client.loop_stop()


if __name__ == "__main__":
    p: Publisher = Publisher(sys.argv[1])
    p.run()
