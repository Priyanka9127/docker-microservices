from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    name = "PRIYANKA KUMARI"
    roll_number = "2022BCD0057"
    bio = "Passionate about technology and innovation, I enjoy building impactful solutions. Always eager to learn and explore new challenges!"
    container_id = os.uname()[1]
    current_time = datetime.datetime.now()
    return render_template('index.html', name=name, roll_number=roll_number, bio=bio, container_id=container_id, current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
