import requests
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, '6RRBKJLD4TFIC4HAZKF0Z756Z5GBWAO3', 'IOGCH17AKBMCBZ1M', 'stage', '8787729063', 'IPSITA', 'Hello Rajdeep Deb\r\nWelcome to Hospital Managment System\r\n\r\nYOU HAVE REGISTERED AS PATIENT\r\n\r\n\r\nThanks for visiting our Hospital\r\n\r\n\r\n\r\n-Regards Ipsita')
