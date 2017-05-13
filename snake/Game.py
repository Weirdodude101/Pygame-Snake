import pygame
import pygame._view
from pygame.locals import *
from snake.Window import Window
from snake import Globals


class Game():
	def __init__(self):
		self.window = Window(Globals.windowTitle, Globals.dispWidth, Globals.dispHeight, Globals.white)
		self.load()

	def load(self):
		self.gameLoaded = True
		while self.gameLoaded:
			self.window.clock.tick(60)
			events = pygame.event.get()
			for event in events:
				if event.type == QUIT:
					self.gameLoaded = False

			self.window.gameDisplay.fill(self.window.bgColor)
			pygame.display.flip()