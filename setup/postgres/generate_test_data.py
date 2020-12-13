from time import *
from random import randint
from datetime import datetime

if __name__ == "__main__":
    current_time = int(str(time()).split(".")[0])

    temperature = randint(-350, 350)
    pressure = randint(740, 780)
    moisture = randint(20, 70)
    luminosity = randint(30, 60)

    for i in range(0, 5999):
        current_time -= 60
        template = "INSERT INTO telemetry (device_id, temperature, pressure, moisture, luminosity, tmstamp) " \
                   "VALUES (%d, %d, %d, %d, %d, '%s');"
        t = datetime.fromtimestamp(current_time)

        temperature += pow(-1, randint(0, 1)) * randint(0, 30)
        if temperature < -350:
            temperature = -350
        elif temperature > 350:
            temperature = 350

        pressure += pow(-1, randint(0, 1)) * randint(0, 30)
        if pressure < 740:
            pressure = 740
        elif pressure > 780:
            pressure = 780

        moisture += pow(-1, randint(0, 1)) * randint(0, 30)
        if moisture < 20:
            moisture = 20
        elif moisture > 70:
            moisture = 70

        luminosity += pow(-1, randint(0, 1)) * randint(0, 30)
        if luminosity < 30:
            luminosity = 30
        elif luminosity > 60:
            luminosity = 60

        print(template % (i / 2000 + 1, temperature, pressure, moisture, luminosity, t))