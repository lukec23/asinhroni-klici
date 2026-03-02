from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/coinflip")
def coinflip():
    return render_template("coinflip.html")

@app.route("/coinData")
def coinData():
    #print(request.form) v primeru POST
    #print(request.args["vrednost"])
    status = random.choice(["HEADS","TAILS"])
    imgSource={"HEADS" : "https://i.postimg.cc/CBNJNfDJ/head.png", "TAILS" : "https://i.postimg.cc/zysdXN8w/tail.png"}

    return {"status" : status, "slika": imgSource[status]}

@app.route("/quote")
def quote():
    return render_template("quote.html")

@app.route("/quoteData")
def quoteData():
    quotes=["Biti drugačen ni napaka, ampak moč.",
            "Sreča ni nekaj, kar je pripravljeno. Sreča prihaja iz vaših dejanj.",
            "Za vse, kar potrebujemo, je ljubezen. Vse ostalo je odveč.",
            "Ne čakajte, da priložnosti pridejo k vam. Ustvarite jih sami.",
            "Tisti, ki si upajo sanjati, so tisti, ki lahko spremenijo svet.",
            "Edini način, da narediš dobro delo, je, da ljubiš to, kar počneš.",
            "Ne glej na uro; počni, kar počne ura.",
            "Učimo se iz preteklosti, a živimo v sedanjosti.",
            "Sreča ni cilj, temveč pot.",
            "Pomembno je, da si upamo. Da se postavimo, ko je treba."
            ]
    rnd_quote=random.choice(quotes)
    return {"quote":rnd_quote}


@app.route("/randomŠt")
def randomŠt():
    return render_template("randomŠt.html")

@app.route("/randomŠtData")
def randomŠtData():
    

    return 



app.run(debug=True)