import pickle
from copy import deepcopy
from typing import List, Dict

class TrieNode:
    def __init__(self) -> None:
        self.nodes: Dict[str, TrieNode] = {}
        self.is_leaf = False

    def insert_many(self, words: List[str]) -> None:
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def isCharInTrie(self, char: str) -> bool:
        return char in self.nodes

    def isSubstringInTrie(self, string: str) -> bool:
        curr = self
        for char in string:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True

    def delete(self, word: str) -> None:
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """

        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str) -> None:
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)

def buildEnglishTrie():
    file = open("wordList", 'r')
    data = file.read().split('\n')
    root = TrieNode()
    root.insert_many(data)
    return root


def manualTest():
    root = TrieNode()
    root.insert_many("pea peanuts ship tree tee try".split())
    while True:
        string = input()
        if not root.isSubstringInTrie(string):
            print(f'{string} not found')
        else:
            print(f'{string} found')


def findAllWordsAtCoordinateWrapper(board, i, j, wordList, trie):
    return findAllWordsAtCoordinate(board, i, j, wordList, trie, '', set(), None)


def findAllWordsAtCoordinate(board, i, j, wordSet, trie, currentWord, solutionCoordinates, visited=None, ):
    if visited is None:
        visited = []
        for a in range(len(board)):
            tmp = [0 for _ in range(len(board[a]))]
            visited.append(tmp)

    if not isInBound(board, i, j):
        return currentWord

    if visited[i][j] == 1:
        return currentWord

    if trie.isSubstringInTrie(currentWord + board[i][j]):
        if trie.find(currentWord + board[i][j]):
            # wordSet.add(currentWord + board[i][j])
            solutionCoordinates.add((i, j))
            wordSet[(currentWord + board[i][j])] = solutionCoordinates

        currentWord += board[i][j]
        solutionCoordinates.add((i, j))
        visited[i][j] = 1
        findAllWordsAtCoordinate(board, i + 1, j, wordSet, trie, currentWord, deepcopy(solutionCoordinates) ,deepcopy(visited))
        findAllWordsAtCoordinate(board, i - 1, j, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i, j + 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i, j - 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i - 1, j - 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i + 1, j - 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i - 1, j + 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))
        findAllWordsAtCoordinate(board, i + 1, j + 1, wordSet, trie, currentWord, deepcopy(solutionCoordinates),deepcopy(visited))

    else:
        visited[i][j] = 1
        return currentWord

def wordSearch(board):
    englishTrieFile = open('englishTrie', 'rb')
    trie = pickle.load(englishTrieFile, encoding='bytes')
    words = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            findAllWordsAtCoordinateWrapper(board, i, j, words, trie)
    print(dict(sorted(words.items(), key=lambda ele: len(ele[0]), reverse=True)))

def isInBound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

if __name__ == "__main__":
    board = [
        list('inr---e-'),
        list('ngt-sneu'),
        list('fkccsdco'),
        list('rdspehtr'),
        list('b-cuzoxs'),
        list('lyn-iil-'),
    ]
    wordSearch(board)