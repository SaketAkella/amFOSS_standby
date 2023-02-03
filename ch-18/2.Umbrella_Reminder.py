from twilio.rest import Client
import bs4,requests
res=requests.get('https://forecast.weather.gov/MapClick.php?lat=38.91706000000005&lon=-77.00024999999994')
print(res.raise_for_status)
soup=bs4.BeautifulSoup(res.text,'html.parser')

weather=soup.select('#detailed-forecast-body > div:nth-child(1)')

for i in weather:
    prediction=i.text

if 'rain' in str(prediction):
    content='Carry an umbrella since it will rain'
elif 'cloudy' in str(prediction):
    content='Carry an umbrella, it may be cloudy'
elif 'drizzly' in str(prediction):
    content='Carry an umbrella since it will rain lightly'
else:
    content="Have a nice day"


accountSID='AC102e02c2759168aefe2b1c1afa109aa2'
authToken='268d4a928a572358fc14bc7eebb2d484'

twilioCli = Client(accountSID, authToken)

myTwilioNumber='+13856449551'
myCellPhone='+91 6282533179'

message=twilioCli.messages.create(body=content,from_=myTwilioNumber,to=myCellPhone)