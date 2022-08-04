currentLongestWord = ''

def displayInitialHtml():
    with open('templates/index.html', 'r') as file:
        html = file.read()
    return html


def buildFullHtml(sizeI=None, sizeJ=None, isSolution=False, solutionSet=None, board=None):
    html = displayInitialHtml()
    if sizeI is not None and sizeJ is not None:
        html += buildHtmlTable(sizeI, sizeJ, isSolution, solutionSet, board)
        html += '</tbody>\n</table>\n ' \
                '<p></p>\n' \
                '<label>\n' \
                '<input type="submit" value="Solve">\n' \
                '</label>\n' \
                '</form>\n' \
                '</div>\n'

        if currentLongestWord != '':
            html += f'<p>Longest word is:{currentLongestWord}</p>'

    end = '</body>\n</html>'
    html += end
    return html


def buildHtmlTable(sizeI, sizeJ, isSolution, solutionSet, board):
    html = '<div id="board">\n' \
           '<form action="/temp" name="wordBoard" method="post">\n' \
           '<table class="word-board">\n' \
           '<tbody>\n'
    html += buildHtmlTableHeader(sizeJ)
    html += buildHtmlTableRows(sizeI, sizeJ, isSolution, solutionSet, board)
    return html


def buildHtmlTableHeader(sizeJ):
    th = '<tr>\n<th></th>\n'
    for i in range(sizeJ):
        th += f'<th>{i}</th>\n'
    th += '</tr>\n'
    return th


def buildHtmlTableRows(sizeI, sizeJ, isSolution, solutionSet, board):
    if isSolution:
        return ''.join(buildHtmlTableRowWithSolution(i, sizeJ, solutionSet, board)for i in range(sizeI))

    else:
        return ''.join(buildHtmlTableRow(i, sizeJ) for i in range(sizeI))


def buildHtmlTableRow(currentI, sizeJ):
    htmlTableRow = '<tr>\n'
    htmlTableRow += f'<th>{currentI}' + '</th>\n'
    for j in range(sizeJ):
        if j == sizeJ - 1:
            htmlTableRow += '<td class="light"><label>\n' \
                            '<input type="text" maxlength="1" name="i' + str(currentI) + "j" + str(j) + '" onkeyup' \
                                                                                                        '="autotab(this, ' \
                                                                                                        'document.wordBoard.' + 'i' + str(
                currentI + 1) + 'j' + '0' + ')">\n' \
                                            '</label></td>\n'
        else:
            htmlTableRow += '<td class="light"><label>\n' \
                            '<input type="text" maxlength="1" name="i' + str(currentI) + "j" + str(j) + '" onkeyup' \
                                                                                                        '="autotab(this, ' \
                                                                                                        'document.wordBoard.' + 'i' + str(
                currentI) + 'j' + str(j + 1) + ')">\n' \
                                               '</label></td>\n'
    htmlTableRow += '</tr>\n'
    return htmlTableRow


def buildHtmlTableRowWithSolution(currentI, sizeJ, solutionSet, board):
    htmlTableRow = '<tr>\n'
    htmlTableRow += f'<th>{currentI}' + '</th>\n'
    global currentLongestWord
    for j in range(sizeJ):
        for word, coords in solutionSet:
            color = 'dark' if (currentI, j) in coords else 'light'

            if j == sizeJ - 1:
                htmlTableRow += '<td class="' + color + '"><label>\n' \
                                                        '<input type="text"' + 'value="' + board[currentI][j] + '"maxlength="1" name="i' + str(
                    currentI) + "j" + str(j) + '" onkeyup' \
                                               '="autotab(this, ' \
                                               'document.wordBoard.' + 'i' + str(
                    currentI + 1) + 'j' + '0' + ')">\n' \
                                                '</label></td>\n'
            else:
                htmlTableRow += '<td class="' + color + '"><label>\n' \
                                                        '<input type="text"' + 'value="' + board[currentI][j] + '"maxlength="1" name="i' + str(
                    currentI) + "j" + str(j) + '" onkeyup' \
                                               '="autotab(this, ' \
                                               'document.wordBoard.' + 'i' + str(
                    currentI) + 'j' + str(j + 1) + ')">\n' \
                                                   '</label></td>\n'
            currentLongestWord = word
            break
    htmlTableRow += '</tr>\n'
    return htmlTableRow
