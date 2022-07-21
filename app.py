from flask import Flask, render_template, request

import htmlBuilder

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    sizeI, sizeJ = None, None
    if request.method == "POST":
        sizeI = int(request.form["i"])
        sizeJ = int(request.form["j"])
        print(sizeI, sizeJ)
    return htmlBuilder.buildFullHtml(sizeI, sizeJ)


if __name__ == '__main__':
    app.run()
