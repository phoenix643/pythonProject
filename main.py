import requests
import datetime
import time

GENDER = "male"
WEIGHT_KG = 64
HEIGHT_CM = 160
AGE = 18

api_key = "bb75e68dbc6b5e1bfd95688a07eb936b"
api_id = "eb97e565"
api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("What exercise did you do?")

current_day = datetime.datetime.now()

parameter = {"query": query,
             "gender": GENDER,
             "weight_kg": WEIGHT_KG,
             "height_cm": HEIGHT_CM,
             "age": AGE}

header = {"x-app-id": api_id,
          "x-app-key": api_key}

response = requests.post(api_endpoint, json=parameter, headers=header)
result = response.json()
sheety_endpoint = "https://api.sheety.co/35580fe88424cf7f9ec7f9b3dd52ed03/myWorkouts/workouts"
for exercise in result["exercises"]:
    activity = {"workout":
                    {"date": f"{current_day.day}/{current_day.month}/{current_day.year}",
                     "time": str(time.strftime("%H:%M:%S", time.localtime())),
                     "exercise": exercise["name"].title(),
                     "duration": exercise["duration_min"],
                     "calories": exercise["nf_calories"]
                     }
                }
    exercise_response = requests.post(sheety_endpoint, json=activity)
print(exercise_response.text)
