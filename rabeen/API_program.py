import requests
response = requests.get(f"http://worldtimeapi.org/api/timezone/Asia/Kolkata")
print(response.status_code)
print(response.json())
