from flask import Flask, render_template
from database import *
from playhouse.shortcuts import model_to_dict
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    db.connect()
    query = Drug.select().order_by(Drug.price.desc()).limit(4)
    most_valuable = [model_to_dict(i) for i in query]
    db.close()
    return render_template('index.html', most_valuable=most_valuable)


@app.route('/catalog', methods=['GET'])
def catalog():
    db.connect()
    query = Drug.select()
    all_drugs = [model_to_dict(i) for i in query]
    db.close()
    return render_template('catalog.html', list_of_drugs=all_drugs)


@app.route('/about-us', methods=['GET'])
def about_us():
    return render_template('about_us.html')


@app.route('/catalog/<int:ident>', methods=['GET'])
def item(ident: int):
    drug = Drug.get_drug(ident)
    if drug:
        return render_template('page.html', drug=drug)
    else:
        return "Not Found", 404


if __name__ == '__main__':
    app.run()
