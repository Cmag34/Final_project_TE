from flask import Flask, render_template, request
from sense_hat import SenseHat 

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['message']


    if message == 'red':


        X = [255, 0, 0]  # Red
        O = [255, 255, 255]  # White

        red_greeting = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O
        ]

        sense.set_pixels(red_greeting)

    elif message == 'blue':


        X = [0, 0, 255]  # blue
        O = [255, 255, 255]  # White

        blue_greeting = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, X, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, X, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, X, O, O, O, O
        ]

        sense.set_pixels(blue_greeting)
    
    return "Mery Christmas!"
    # name = request.form['name']
    # display = f'{message}  Love, {name}'
    # sense.show_message(display, text_colour=[0, 0, 255])
    # return render_template('received.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
