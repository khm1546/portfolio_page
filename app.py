from flask import Flask, render_template
from models import Members
from database import db_session
from models import Members
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/yujin_m')
def yujin_m():
    return render_template('/yujin/main.html')


@app.route('/all')
def select_all():
    me = Members.query.filter(Members.name == '김형민').first()
    me.name = "성공"
    me.question = "자자"
    db_session.add(me)
    db_session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
