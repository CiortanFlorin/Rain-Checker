import requests
from twilio.rest import Client

account_sid = "AC9d6bca31502a693036b215eced7b0fce"
auth_token =  "e9fe288fc16dc3b8383cc67dea79e336"
parameters={
    "lat":44.417276,
    "lon":26.042676,
    "appid":"b0e89ccbc77f3c56be5c792c6414a8d0",
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
                     from_='+19724417141',
                     to='+40751518506'
                 )
    print(message.status)