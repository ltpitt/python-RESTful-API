#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, jsonify
import time
import subprocess
import os

telldus = '/usr/bin/python /home/osmc/Scripts/telldus_controller.py'
on = ' --on '
off = ' --off '

functions = {'light_stairs': '7', 'light_bedroom': '6'}

def change_power_status(status, id):
    try:
        int(id)
        is_id_integer = True
    except ValueError:
        is_id_integer = False
    if is_id_integer:
        p = subprocess.Popen(telldus + status + id, shell=True)
        p.wait()
    else:
        p = subprocess.Popen(telldus + status + functions[id], shell=True)
        p.wait()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print "post"
    else:
        return 'get'

@app.route('/buonanotte')
@app.route('/shutdown')
def shutdown_pwd_request():
    return 'What about using a password?!'

@app.route('/shutdown/<password>')
def shutdown(password):
    if password == 'unreal':
        logoff_and_shutdown()
    else:
        return 'Wrong password, lamer!'

@app.route('/buonanotte/<password>')
def buonanotte(password):
    if password == 'unreal':
        all_lights_off()
        logoff_and_shutdown()
        return '<h1>Sleep well :)</h1>'
    else:
        return '<h1>Wrong password, lamer!</h1>'

@app.route('/turn_off/<id>/<password>')
def turn_off(id, password):
    if password == 'unreal':
        change_power_status(off, id)
        return 'done'
    else:
        return '<h1>Wrong password, lamer!</h1>'

@app.route('/turn_on/<id>/<password>')
def turn_on(id, password):
    if password == 'unreal':
        change_power_status(on, id)
        return 'done'
    else:
        return '<h1>Wrong password, lamer!</h1>'


@app.route('/all_lights_on/<password>')
def all_lights_on_now(password):
    if password == 'unreal':
        all_lights_on()
        return 'done'
    else:
        return '<h1>Wrong password, lamer!</h1>'

@app.route('/all_lights_off/<password>')
def all_lights_off_now(password):
    if password == 'unreal':
        all_lights_off()
        return 'done'
    else:
        return '<h1>Wrong password, lamer!</h1>'

@app.route('/raspi_reboot/<password>')
def reboot(password):
    if password == 'unreal':
        p = subprocess.Popen(r'/sbin/reboot', shell=True)
        p.wait()
    else:
        return '<h1>Wrong password, lamer!</h1>'


def logoff_and_shutdown():
    pass
    #os.system('shutdown /s /f')

def all_lights_off():
    change_power_status(off, 'light_stairs')
    change_power_status(off, 'light_bedroom')

def all_lights_on():
    change_power_status(on, 'light_stairs')
    change_power_status(on, 'light_bedroom')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
