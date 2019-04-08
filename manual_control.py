from flask import Flask, render_template, request
# from car_controls import Controls

app = Flask(__name__)
# controls = Controls()


@app.route('/')
def root():
   return render_template('manual-control.html')


@app.route('/coords')
def coords():
    speed = request.args.get('speed')
    angle = request.args.get('angle')
    # controls.move(speed)
    # controls.turn(angle)
    return 'success'


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=False)
