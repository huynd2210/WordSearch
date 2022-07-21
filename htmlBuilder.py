def displayInitialHtml():
    with open('templates/index.html', 'r') as file:
        html = file.read()
    return html

def buildFullHtml(sizeI=None, sizeJ=None):
    html = displayInitialHtml()

    if sizeI is not None and sizeJ is not None:
        html += buildHtmlTable(sizeI, sizeJ)
        html += '</tbody>\n</table>\n ' \
              '<p></p>\n' \
              '<label>\n' \
              '<input type="submit" value="Solve"\n' \
              '</label>' \
              '</form>\n</div>'

    end = '</body>\n</html>'
    html += end
    return html


def buildHtmlTable(sizeI, sizeJ):
    html = '<div id="board">\n' \
           '<form action="#" name="wordBoard" method="post">\n' \
           '<table class="word-board">\n' \
           '<tbody>\n'
    html += buildHtmlTableHeader(sizeJ)
    html += buildHtmlTableRows(sizeI, sizeJ)
    return html


def buildHtmlTableHeader(sizeJ):
    th = '<tr>\n<th></th>\n'
    for i in range(sizeJ):
        th += f'<th>{i}</th>\n'
    th += '</tr>\n'
    return th


def buildHtmlTableRows(sizeI, sizeJ):
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
