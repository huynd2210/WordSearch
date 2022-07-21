from flask import Flask, render_template

import htmlBuilder

app = Flask(__name__)

@app.route("/")
def index():
    return htmlBuilder.buildHtml()

if __name__ == '__main__':
    app.run()
