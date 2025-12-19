#import the requied things to be use
from flask import Flask, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://backend:9000'

# Flask app
app = Flask(__name__)

# Home route with form
@app.route('/')
def home():
    
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return 'Data submitted successfully' 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)
