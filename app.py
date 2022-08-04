from flask import Flask, render_template, request, redirect, url_for

import htmlBuilder
# since TrieNode isnt its own class (its 'subclass' of wordSearch.py therefore it is required to explicitly import it.
from wordSearch import TrieNode
import wordSearch

app = Flask(__name__)
sizeI = 0
sizeJ = 0


# this code is crappy, built in as little time as possible and built in purpose of learning how to use flask.

@app.route("/", methods=["POST", "GET"])
def index():
    global sizeI
    global sizeJ
    if (
            request.method == "POST"
            and request.form["i"] != ''
            and request.form["j"] != ''
    ):
        sizeI = int(request.form["i"])
        sizeJ = int(request.form["j"])

    return htmlBuilder.buildFullHtml(sizeI, sizeJ)


@app.route("/temp", methods=["POST", "GET"])
def temp():
    board = []
    for i in range(sizeI):
        tmp = [request.form[f'i{str(i)}j{str(j)}'] for j in range(sizeJ)]
        board.append(tmp)
    # print(board)
    # print(wordSearch.search(board))
    solutionDict = wordSearch.search(board)

    return htmlBuilder.buildFullHtml(sizeI, sizeJ, True, solutionDict.values(), board)


# @app.route("/board", methods=["POST"])
# def boardSolve():
#     # if request.method == 'GET':
#     #     return redirect(url_for("index"))
#     print("here")
#     if request.method == 'POST':
#         board = []
#         for i in range(sizeI):
#             tmp = [request.form[f'i{str(i)}j{str(j)}'] for j in range(sizeJ)]
#             board.append(tmp)
#         print(board)
#     return htmlBuilder.buildFullHtml(sizeI, sizeJ)

if __name__ == '__main__':
    app.run()
