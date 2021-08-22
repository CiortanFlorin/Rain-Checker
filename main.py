import requests
from twilio.rest import Client

account_sid = "YOUR TWILLIO SID"
auth_token =  "YOUR TWILLIO TOKEN"
parameters={
    "lat":"YOUR LAT",
    "lon":"YOUR LONG",
    "appid":"YOUR WEATHER API key",
    "exclude": "current,minutely,daily"
}
r=requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
r.raise_for_status()
data=r.json()

will_rain = False


weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 900:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today",
                     from_='YOUR TWILLIO ACCOUNT NUMBER',
                     to='YOUR NUMBER'
                 )
    print(message.status)