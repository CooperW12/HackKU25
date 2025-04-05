from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('mainpage.html')

if __name__ == "__main__":
    app.run(debug=True)