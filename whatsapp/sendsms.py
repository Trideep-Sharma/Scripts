from twilio.rest import Client
from PyDictionary import PyDictionary
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'sid'
auth_token = 'token'
client = Client(account_sid, auth_token)
dictionary=PyDictionary()

def send(sender,msg):
	a = dictionary.meaning(msg)
	a = a[list(a.keys())[0]][0]
	message = client.messages.create( body=a, from_='whatsapp:+number', to=sender )
	return
