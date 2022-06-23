#!/usr/bin/python3 

##########################################
# URL Shorter: https://bitly.com/
##########################################

##########################################
# Script Execution:
##########################################
# python3 app.py https://google.com/
##########################################

import sys, signal
from flask import Flask, request, redirect 
from logging import getLogger, ERROR

# CTRL + C
def ctrl_c(sig, frame):
    print('\n[+] Exiting...!')
    sys.exit(0)
    
signal.signal(signal.SIGINT, ctrl_c)

# Main variables 
app = Flask(__name__)
log = getLogger('werkzeug')
log.setLevel(ERROR)

# Route to redirect and get data
@app.route('/', methods=["GET", "POST"])
def index():
    if request:
        if 'bitlybot' not in request.__dict__['environ']['HTTP_USER_AGENT']:
            print("-"*80)
            print("[+] Remote IP: {}".format(request.__dict__['environ']['REMOTE_ADDR']))
            print("[+] Remote Port: {}".format(request.__dict__['environ']['REMOTE_PORT']))
            print("[+] User-Agent: {}".format(request.__dict__['environ']['HTTP_USER_AGENT']))
            print("[+] HTTP Method: {}".format(request.__dict__['environ']['REQUEST_METHOD']))
            print("-"*80)
    return redirect(url)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        app.run(host='0.0.0.0', debug=False, port=80)
    else: 
        print('[+] {} <URL-to-redirect>'.format(sys.argv[0]))
        sys.exit(0)
