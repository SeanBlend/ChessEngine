#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import chess
from copy import deepcopy
from _eval import Eval


class Tree:
    def __init__(self, board, depth):
        self.board = board
        self.depth = depth

    def Go(self):
        pass


class Node:
    def __init__(self, tree, board: chess.Board, depth):
        self.tree = tree
        self.board = board
        self.depth = depth

    def Eval(self, maxPlayer):
        if self.depth == self.tree.depth:
            return (Eval(self.board), self.board.peek())

        if maxPlayer:
            maxEval = float("-inf")
            bestMove = None
            for move in self.board.generate_legal_moves():
                newBoard = deepcopy(self.board)
                newBoard.push(move)
                newNode = Node(self.tree, newBoard, self.depth+1)

                evaluation = newNode.Eval(False)[0]
                if evaluation > maxEval:
                    maxEval = evaluation
                    bestMove = move

            return (maxEval, bestMove)

        else:
            minEval = float("inf")
            bestMove = None
            for move in self.board.generate_legal_moves():
                newBoard = deepcopy(self.board)
                newBoard.push(move)
                newNode = Node(self.tree, newBoard, self.depth+1)

                evaluation = newNode.Eval(True)[0]
                if evaluation < minEval:
                    minEval = evaluation
                    bestMove = move

            return (minEval, bestMove)