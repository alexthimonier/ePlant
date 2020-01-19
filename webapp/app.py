from flask import Flask, render_template
# from led import blinkLed
from uno import start
from _thread import start_new_thread
from readSerial import read
import gpio as gpio
 


start_new_thread(read,())
start()
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/your_flask_funtion')
def get_ses():
 	gpio.turn_on(23)
 	return render_template('index.html')


# @app.route('/led')
#def led():
#     blinkLed()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
