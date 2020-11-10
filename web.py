 #Grupo pablo
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "webchicles"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///carrito.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#Base de datos
class carrito(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    price = db.Column("price", db.Float)
    description = db.Column("description", db.String(100))
    image_url = db.Column("image_url", db.String(100))
    def __init__(self, name, price, description, image_url):
        self.name = name
        self.price = price
        self.description = description
        self.image_url = image_url

#Mis variables
productos=[
    ["Chicle de menta", 0.1, "Descripción", "images/logo.png"],
    ["Chicle de fresa", 0.1, "Descripción", "images/logo.png"],
    ["Chicle de sandía", 0.1, "Descripción", "images/logo.png"] 
    ]
lc=[]

@app.route("/")
def home():
    lc=[]
    for i in carrito.query.all():
        lc.append(i)
    return render_template("index.html", page="home", items=len(lc))

@app.route("/About_Us/")
def aboutus():
    lc=[]
    for i in carrito.query.all():
        lc.append(i)
    return render_template("aboutus.html", page="aboutus", items=len(lc))

@app.route("/Carrito/")
def carritopg():
    lc=[]
    for i in carrito.query.all():
        lc.append(i)
    print(lc)
    return render_template("carrito.html", page="carrito", listacarrito=lc, items=len(lc))

@app.route("/Add_to_cart_<product_index>/")
def add_to_cart(product_index):
    item= carrito(productos[int(product_index)][0],productos[int(product_index)][1],productos[int(product_index)][2],productos[int(product_index)][3])
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("carritopg"))

@app.route("/Remove_from_cart_<product_index>/")
def rm_from_cart(product_index):
    db.session.delete(carrito.query.filter_by(name=product_index).first())
    db.session.commit()
    return redirect(url_for("carritopg"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)