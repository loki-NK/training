# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
import requests


app = Flask(__name__)

@app.route('/send_sms/', methods=['GET','POST'])
def outbound_sms():
    client = plivo.RestClient("Auth_ID","Auth_token")
    response = client.messages.create(
                                  src='11111111111',
                                  dst='To_number',
                                  text='You are receiving a call')
    print(response)

@app.route('/send_sms2/', methods=['GET','POST'])
def outbound_sms1():
    client = plivo.RestClient("Auth_ID","Auth_token")
    response1 = client.messages.create(
                                  src='11111111111',
                                  dst='To_number',
                                  text='You missed a call please check logs')
    print(response1)

if __name__ == "__main__":
    app.run(debug=True)

