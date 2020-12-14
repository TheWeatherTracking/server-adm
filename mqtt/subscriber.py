import sys

import paho.mqtt.client as mqtt


class Subscriber:
    _device_name: str = "unsupported device"
    _topic: str = ""

    def __init__(self, device_name: str):
        self._device_name = device_name
        self._topic = "/devices/" + self._device_name

    def run(self):
        client = mqtt.Client("subscriber")
        client.on_connect = self._on_connect
        client.on_message = self._on_message
        client.on_subscribe = self._on_subscribe
        client.connect("localhost")
        client.loop_forever()

    def _on_message(self, client, userdata, msg):
        print("on_message: " + msg.topic + " " + str(msg.payload))

    def _on_connect(self, client, userdata, flags, rc):
        print("on_connect: rc='%s' client='%s' flags='%s' topic='%s'" % (
        mqtt.connack_string(rc), client, flags, self._topic))
        client.subscribe(self._topic, 2)

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        print("on_subscribe: mid='%s'" % (mid))


if __name__ == "__main__":
    s: Subscriber = Subscriber(sys.argv[1])
    s.run()
