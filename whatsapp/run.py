# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio import twiml
from sendsms import *

app = Flask(__name__)
 
@app.route("/sms", methods=['GET','POST'])
def sms_ahoy_reply():
	sender = request.values['From']
	msg = request.values['Body']
	send(sender,msg)
	return 'Success'
	
if __name__ == "__main__":
    app.run(debug=True)
