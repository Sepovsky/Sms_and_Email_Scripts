from melipayamak.melipayamak import Api


#SMS details
USERNAME = ''
PASSWORD = ''
kabootar = Api(USERNAME, PASSWORD)
sms = kabootar.sms()
_FROM = 'phone_number'
TO = 'phone_number'
TEXT = 'message body'
##################################

response = sms.send(TO, _FROM, text)
print(response)
