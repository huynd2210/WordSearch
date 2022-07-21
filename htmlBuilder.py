def buildHtml(sizeI=8, sizeJ=8):
    with open('templates/index.html', 'r') as file:
        html = file.read()
    html += buildHtmlTable(sizeI, sizeJ)
    closingTags = '</tbody>\n</table>\n</form>\n</div>\n</body>\n</html>'
    html += closingTags
    return html

def buildHtmlTable(sizeI, sizeJ):
    html = '<div id="board">\n' \
           '<form name="wordBoard" method="post">\n' \
           '<table class="chess-board">\n' \
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
                                                                                                       'document.wordBoard.' + 'i' + str(currentI) + 'j' + str(j + 1) + ')">\n' \
                                                                                                       '</label></td>\n'
    htmlTableRow += '</tr>\n'
    return htmlTableRow
