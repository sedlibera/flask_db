from app import db, Message, app
from flask import request, render_template

db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        query = Message(name, email, message)
        db.session.add(query)
        db.session.commit()
        return render_template("greetings.html", vardas=name)
    elif request.method == "GET":
        return render_template("login.html")

@app.route("/vartotoju_sarasas/")
def vartotoju_sarasas():
    all_messages = Message.query.all()
    vartotojai = []
    [vartotojai.append(item) for item in all_messages]
    return render_template("vartotoju_sarasas.html", vartotojai=vartotojai)

@app.route("/paieska_pagal_email/", methods=["GET", "POST"])
def paieska_pagal_email():
    if request.method == "POST":
        ieskom = request.form["paieska"]
        paieskos_rez = Message.query.filter(Message.email.ilike(f"%{ieskom}%")).all()
        return render_template("paieska_pagal_email_rezult.html", vardas=ieskom, rez=paieskos_rez)
    elif request.method == "GET":
        return render_template("paieska.html")

if __name__ == "__main__":
    app.run(debug=True)
