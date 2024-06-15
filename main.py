from flask import Flask,render_template
import random
import time
import requests

# name= input("input a name")
app = Flask(__name__)

# print(formatted_time)
@app.route('/')
def home():
    current_time = time.localtime()
    formatted_time = time.strftime("%d/%m/%y", current_time)
    random_number = random.randint(1,9)
    return render_template("index.html", num = random_number, num2 = formatted_time)

@app.route('/<username>')
def guess(username):
    API = f"https://api.agify.io?name={username}&country_id=US"
    response = requests.get(API)
    data = response.json()
    age = data.get('age')
    return f"Hello {username}, I think you are {age} years old "

if __name__ == ("__main__"):
    app.run(debug=True)
