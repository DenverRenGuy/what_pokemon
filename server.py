from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    count = 1
    numbers = []
    while len(numbers) < 151:
        numbers.append(count)
        count = count + 1

    return render_template('index.html', numbers=numbers)

app.run(debug=True)
