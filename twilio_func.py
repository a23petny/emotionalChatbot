# from twilio.rest import Client

# account_sid = '---'
# auth_token = '---'
# client = Client(account_sid, auth_token)
# def send_whatsapp_message(body,to):
#     # Send a WhatsApp message
#     message = client.messages.create(
#       from_='whatsapp:+14155238886',
#       body=body,
#       to=to
#     )
#     print(message.sid)



from twilio.rest import Client
account_sid = '---'
auth_token = '---'
client = Client(account_sid, auth_token)
def send_whatsapp_message(body,to):
    message = client.messages.create(
        from_="+12096712613",
        body=body,
        to=to
    )
    print(message.sid)
