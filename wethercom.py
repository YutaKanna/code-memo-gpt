# Weather.com APIを使用して、Pythonで今日の天気を取得するプログラム
import requests

def get_weather(api_key, location):
    url = f"https://api.weather.com/v3/wx/conditions/current?apiKey={api_key}&language=ja&format=json&geocode={location}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_info = data["imperial"]
        temperature = weather_info["temp"]
        condition = weather_info["phrase"]
        humidity = weather_info["rh"]
        wind_speed = weather_info["wspd"]
        
        print(f"場所: {location}")
        print(f"天気: {condition}")
        print(f"気温: {temperature}°F")
        print(f"湿度: {humidity}%")
        print(f"風速: {wind_speed} mph")
    else:
        print("天気情報の取得に失敗しました。")

# Weather.com APIのアクセスキーと場所を指定してください
api_key = "YOUR_API_KEY"
location = "35.6895,139.6917"  # 東京の緯度経度

get_weather(api_key, location)
