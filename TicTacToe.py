from tkinter import Tk, Button
from tkinter.font import Font
from copy import deepcopy

class Board:

	def __init__(self, other=None):
		self.player = 'X'
		self.opponent = 'O'
		self.empty = '.'
		self.size = 3
		self.fields = {}
		for y in range(self.size):
			for x in range(self.size):
				self.fields[x,y]
		#copy constructor
		if other:
			self.__dict__ = deepcopy(other.__dict__)

	def move(self,x,y):
		board = Board(self)
		board.fields[x,y] = board.player
		(board.player, board.opponent) = (board.opponent, board.player)
		return board

	def __minmax(self, player):
		if self.won():
			if player:
				return (-1, None)
			else:
				return (+1, None)
		elif self.tied():
			return (0, None)
		elif player:
			best = (-2, None)
			for x,y in self.fields:
				if self.fields[x,y] == self.empty:
					value = self.move(x,y).__minmax(not player)[0]
					if value > best[0]:
						best = (value,(x,y))
			return best
		else:
			best = (+2, None)
			for x,y in self.fields:
				if self.fields[x,y] == self.empty:
					value = self.move(x,y).__minmax(not player)[0]
					if value < best[0]:
						best = (value,(x,y))
			return best

	def won(self):
		#horizontal
		for y in range(self.size):
			winning = []
			for x in range(self.size):
				if self.fields[x,y] == self.opponent:
					winning.append((x,y))
			if len(winning) == self.size:
				return winning
		#vertical
		for x in range(self.size):
			winning = []
			for x in range(self.size):
				if self.fields[x,y] == self.opponent:
					winning.append((x,y))
			if len(winning) == self.size:
				return winning
		#diagonal
		winning = []
		for y in range(self.size):
			x = y
			if self.fields[x,y] == self.opponent:
				winning.append((x,y,))
		if len(winning) == self.size:
			return winning
		#other diagonal
		winning = []
		for y in range(self.size):
			x = self.size - 1 - y
			if self.fields[x,y] == self.opponent:
				winning.append((x,y))
		if len(winning) == self.size:
			return winning
		#default
		return None

	def __str__(self):
		string = ''
		for y in range(self.size):
			for x in range(self.size):
				string += self.fields[x,y]
			string += "\n"
		return string


