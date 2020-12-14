import sys
import time
from random import randint

import paho.mqtt.client as mqtt


class Publisher:
    _device_name = "unsupported device"
    _topic = ""
    _lifetime = 30
    _period = 5
    _logfile = "publisher.log"

    def __init__(self, device_name, lifetime, period, logfile):
        self._device_name = device_name
        self._topic = "/devices/" + self._device_name
        self._lifetime = lifetime
        self._period = period
        self._logfile = logfile

    def _connect(self, client, userdata, flags, rc):
        print("connected " + mqtt.connack_string(rc))

    def _publish(self, client, userdata, mid):
        print("published mid='%s' on topic '%s'" % (mid, self._topic))

    def run(self):
        print("run publisher for '%s'" % self._device_name)

        client = mqtt.Client("abssdsd")

        client.on_publish = self._publish
        client.on_connect = self._connect

        client.connect("localhost")
        client.loop_start()

        iter = self._lifetime
        while iter > 0:
            iter -= self._period
            message = "t=%d.%d;p=%d;m=%d;l=%d" % (
                randint(0, 100), randint(0, 9), randint(740, 780), randint(30, 70), randint(30, 60))

            client.publish(self._topic, message)
            
            with open(self._logfile, "a") as f:
                f.write(self._topic + ": " + message)

            time.sleep(self._period)
        client.loop_stop()


if __name__ == "__main__":
    p = Publisher(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    p.run()
