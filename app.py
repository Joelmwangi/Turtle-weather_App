from http.client import responses

from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# API_KEY = "https://api.openweathermap.org/data/2.5/weather?lat=-0.5796436&lon=34.9578269&appid=234114e3dd08fd2131b12160a98a65af&units=metric"
API_KEY = "234114e3dd08fd2131b12160a98a65af"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed']
            }
        else:
            weather_data = {'error': 'City not found or API failed'}

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)