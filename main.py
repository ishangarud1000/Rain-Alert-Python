import requests
import smtplib as st

endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="b72eb3406e0db1837e384d9253af02c9"

my_email="trinetrateam04@gmail.com"
password = "hqah rtwz ebop xykw"

weather_params={
    "lat":44.4323,
    "lon":26.1063,
    "appid":api_key,
    "cnt":4
}
will_rain=False

response=requests.get(url=endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code<700:
        will_rain=True

if will_rain:
    with st.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(my_email, password)
        smtp.sendmail(from_addr=my_email, to_addrs="ishangarud1000@gmail.com", msg="Subject:Its Going to Rain,\n\n Don't "
                                                                                   "forget to bring your umbrella")
