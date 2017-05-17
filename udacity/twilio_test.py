from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC567d1cb37b88b4ae408164232c4a0f9d"
# Your Auth Token from twilio.com/console
auth_token  = "88041aae8a8b8541992e1a6429717d44"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16024101814",
    from_="+16237380645",
    body="u r a qt3.14. <3 Alex!")

print message.sid
