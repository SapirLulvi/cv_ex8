from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def show_cv_template():  # put application's code here
    return render_template('cv.html')

@app.route('/assignment8')
def call_hobbies_template():
    #DB
    user=True
    if user:
        return render_template('assignment8.html', fullName={'firstN': 'sapir', 'lastN': 'lulvi'}, HobbiesList=('music','surfing','family trips','design','reading'))
    else:
        return redirect(url_for('show_cv_template'))

if __name__ == '__main__':
    app.run()
