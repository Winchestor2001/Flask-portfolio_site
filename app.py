from flask import Flask, render_template
from database.models import db, About
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    about = About.select()
    result = [model_to_dict(item) for item in about]
    return render_template('index.html', about=result)


if __name__ == '__main__':
    db.create_tables([About])
    app.run(debug=True)
