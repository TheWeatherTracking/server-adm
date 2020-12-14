import os
import time

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

publishers = {}

@app.route("/mqtt_emulating_helper")
def index():
    ct = time.time()

    rem = []
    for pk in publishers.keys():
        p = publishers[pk]
        if p["timestamp"] + p["lifetime"] < ct:
            rem.append(pk)

    for pk in rem:
        del publishers[pk]

    return render_template('index.html', p=publishers, i=len(publishers)+1)


@app.route("/mqtt_emulating_helper/create-publisher", methods=['POST'])
def create_publisher():
    try:
        lifetime = request.form['lifetime']
        if lifetime is None or lifetime == "" or int(lifetime) <= 0:
            lifetime = 30

        period = request.form['period']
        if period is None or period == "" or int(period) <= 0:
            period = 5

        dev_name = request.form['device_signature']
        if dev_name is None or dev_name == "":
            dev_name = "default_dev"

        ct = time.time()

        if dev_name not in publishers:
            publishers[dev_name] = {"timestamp": ct, "lifetime": int(lifetime), "period": int(period)}
            os.system("python3 /home/developer/server-adm/mqtt/publisher.py %s %s %s >> /home/developer/publisher.log 2>&1 &" % (dev_name, lifetime, period))

        return redirect("/mqtt_emulating_helper")
    except Exception as e:
        print(e)
        return redirect("/mqtt_emulating_helper")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
