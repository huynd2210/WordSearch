import pickle
import cProfile
from copy import deepcopy
from functools import lru_cache
from typing import List, Dict

class TrieNode:
    def __init__(self) -> None:
        self.nodes: Dict[str, TrieNode] = {}
        self.is_leaf = False

    def insert_many(self, words: List[str]) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def isSubstringInTrie(self, string: str) -> bool:
        curr = self
        for char in string:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True

def buildEnglishTrie():
    file = open("wordList", 'r')
    data = file.read().split('\n')
    root = TrieNode()
    root.insert_many(data)
    with open('englishTrie', 'wb') as fh:
        pickle.dump(root, fh)
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

@lru_cache(maxsize=None)
def retrieveEnglishTrie():
    englishTrieFile = open('englishTrie', 'rb')
    return pickle.load(englishTrieFile, encoding='bytes')

def wordSearch(board):
    trie = retrieveEnglishTrie()
    words = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            findAllWordsAtCoordinateWrapper(board, i, j, words, trie)
    # print(words)
    print(dict(sorted(words.items(), key=lambda ele: len(ele[0]), reverse=True)))

def isInBound(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def inputBoard():
    print("Input board, use '-' to indicate obstacle and '/' for newline")
    inputBoard = input()
    print(inputBoard.split('/'))
    return inputBoard.split('/')

# if __name__ == "__main__":
#     # board = inputBoard()
#     board = [
#         list('inr---e-'),
#         list('ngt-sneu'),
#         list('fkccsdco'),
#         list('rdspehtr'),
#         list('b-cuzoxs'),
#         list('lyn-iil-'),
#     ]
#     # cProfile.run("wordSearch(board)")
#     wordSearch(board)
