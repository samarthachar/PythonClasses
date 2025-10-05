from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/html', methods=["POST"])
def html():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    print(fname, lname)
    return f"<h1>{fname} {lname}</h1>"

if __name__ == "__main__":
    app.run()