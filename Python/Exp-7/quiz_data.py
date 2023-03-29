import requests

parameters = {
    "amount": 5,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple", params=parameters)
question_data = response.json()["results"]
