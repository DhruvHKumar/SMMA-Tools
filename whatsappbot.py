from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'Your Account SID'
auth_token = 'Your Auth Token'
client = Client(account_sid, auth_token)

def send_message(to, message):
    message = client.messages.create(
        to=to,
        from_="whatsapp:+14155238886",
        body=message)

# To send a message
send_message("whatsapp:phone_number", "Hello from Python! This is a test message.")

#please make sure to add your details in places suggested on call
