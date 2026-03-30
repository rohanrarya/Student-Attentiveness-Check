from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('application'))

@app.route('/application')
def application():

    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)