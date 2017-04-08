from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC6fe24de8c93050c52080c945dd8bc219"
# Your Auth Token from twilio.com/console
auth_token  = "145a0e5b1aa237e83ef83b74b5115927"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="3108803320", 
    from_="+12403926969",
    body="Hello from Python!")

print(message.sid)