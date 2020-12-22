import time
import datetime
import os
import sys

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

log_file_name = "mqtt_tester.log"
jar_file_name = "server-tester.jar"

process = -1

def read_log():
    rows = {}
    with open(log_file_name, "r") as log_file:
        line = log_file.readline()
        while(line):
            if line[0] == "!":
                if line[1] == "D":
                    line = line[3:].replace("\n", "").split("#")
                    rows[line[0]] = {
                        "period": line[1]
                    }
                elif line[1] == "A":
                    line = line[3:].replace("\n", "").split("#")
                    rows[line[0]] = {
                        "period": rows[line[0]]["period"],
                        "message": (line[1] + ": " + line[3] + " '" + line[4] + "'"),
                        "iterations": line[2]
                    }    
                elif line[1] == "R":
                    line = line[3:].replace("\n", "").split("#")
                    if line[0] in rows:
                        del rows[line[0]]
            
            line = log_file.readline()
        
    return rows


@app.route("/")
def index():
    global process
    return render_template('index.html', p=process)

@app.route("/frame")
def frame():
    global process
    rows = read_log()
    print(rows)
    if len(rows) == 0:
        process = -1
    return render_template('frame.html', rows=rows, uptime=datetime.datetime.now())


@app.route("/run", methods=['POST'])
def run():
    global process
    try:
        clean()
        
        min_period = request.form['dev_min_period']
        if min_period is None or min_period == "" or int(min_period) <= 0:
            min_period = 3000
            
        max_period = request.form['dev_max_period']
        if max_period is None or max_period == "" or int(max_period) <= 0:
            max_period = 15000
            
        iterations = request.form['dev_iterations']
        if iterations is None or iterations == "" or int(iterations) <= 0:
            iterations = 3600
            
        amount = request.form['dev_amount']
        if amount is None or amount == "" or int(amount) <= 0:
            amount = 3
            
        
        cmd = "java -jar %s amount=%s iterations=%s max_period=%s min_period=%s >> %s" % (jar_file_name, amount, iterations, max_period, min_period, log_file_name)
              
        os.system(cmd)
        process = 1
            
        return redirect("/")
    except Exception as e:
        print(e)
        return redirect("/")
       
       
@app.route("/stop") 
def stop():
    global process
    pids = os.popen("ps -aux | grep -e \"-jar /home/developer/server-tester.jar\" | awk '{print $2}'").read().split("\n")
    for pid in pids:
        os.system("kill %s" % pid)
    process = -1

    
    return redirect("/")
    
def clean():
    with open(log_file_name, "w") as log_file:
        log_file.write("")

@app.route("/clean_log")
def clean_logs():
    clean()
    return redirect("/")


def main(log_file_name_param, jar_path):
    global log_file_name
    global jar_file_name
    
    log_file_name = log_file_name_param
    jar_file_name = jar_path
    app.run(host="0.0.0.0", debug=True)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
    

    
    
