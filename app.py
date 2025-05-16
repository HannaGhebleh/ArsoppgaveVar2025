from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/kontakt')
def kontakt():
    return render_template('Kontakt.html')

@app.route("/Manualer")
def Manualer(): 
    return render_template("Manualer.html")

@app.route("/Om_oss")
def Om_oss():
    return render_template("Omoss.html")   

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")