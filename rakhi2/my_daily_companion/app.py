from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mood_tracker')
def mood_tracker():
    return render_template('mood_tracker.html')

@app.route('/habit_tracker')
def habit_tracker():
    return render_template('habit_tracker.html')

@app.route('/historical_data')
def historical_data():
    return render_template('historical_data.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/reminder')
def reminder():
    return render_template('reminder.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')

if __name__ == '__main__':
    app.run(debug=True)