from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=["GET", "POST"])
def hello_world():
    resp = MessagingResponse()

    resp.message("Message received.") 

    return str(resp)
if __name__ == "__main__":
        app.run(debug=True)
