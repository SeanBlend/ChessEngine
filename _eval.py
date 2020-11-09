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

def Eval(board: chess.Board):
    fen = board.fen().split(" ")[0]
    material = fen.count("P") - fen.count("p")
    material += 3 * (fen.count("N") - fen.count("n"))
    material += 3 * (fen.count("B") - fen.count("b"))
    material += 5 * (fen.count("R") - fen.count("r"))
    material += 9 * (fen.count("Q") - fen.count("q"))

    return material