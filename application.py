from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"   #URI to make connection to database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# how model are created  and db.Model is provided by flask_sqlalchemy
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route("/")
def hello():
    return "hello"


@app.route("/drinks")
def get_drink():
    drinks = Drink.query.all()
    output = []
    for d in drinks:
        drink_data = {'name':d.name,'description':d.description}
        output.append(drink_data)
        # it return json format of data
    return {"drink":output}


if __name__ == "__main__":
    with app.app_context():    #is used to  which app you are reffering to
        
        db.create_all()  # used to create connection to database using (app.config URI)

        result=get_drink()
        print(result)
    

    app.run(debug=True)


