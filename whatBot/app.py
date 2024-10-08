from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# from bot import BlenderBot

app = Flask(__name__)

# chat_bot = BlenderBot()

@app.route("/sms", methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    try:   
        message_body = request.form['Body'].lower()
        print(message_body)
        if message_body == "hi" or message_body == "hello":
            resp.message("Hello, how can I help you?")
        elif message_body == 'bye':
            resp.message("See u later!")    
        else:      
            resp.message("Sorry, I didn't undertand.")
    except Exception as e:
        resp.message(f"Oh no, I'm sorry! Error:{e}")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)