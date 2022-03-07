from django.shortcuts import render
import requests

def check_weather(request):
	if request.POST.get("city"):
		try:
			city = request.POST.get("city")
			a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2 = "&q=" + city
			a3 = "&appid=c6e315d09197cec231495138183954bd"
			wa = a1 + a2 + a3
			res = requests.get(wa)
			data = res.json()
			a =  "Temperature in "+ city + " : " + str(data['main']['temp']) + "\u2103 | "
			b = str(data['weather'][0]['description'])
			temp = a + b
			
			return render(request, "check_weather.html", {"msg":temp})
		except Exception:
			return render(request, "check_weather.html", {"msg":"City Name not found!"})

	return render(request, "check_weather.html")