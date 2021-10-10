from typing import NewType
import pygame
import json

from pygame.event import wait

with open('settings.json', 'r') as src:
	prp = json.load(src)

class cnr(pygame.sprite.Sprite):

	def __init__(self, x,y, w,h, c) -> None:
		super(cnr, self).__init__()
		self.x = x-w/2
		self.y = y-h/2
		self.w = w
		self.h = h
		self.c = c
		self.image = pygame.Surface((self.w, self.h))
		self.image.fill(self.c)
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		
	def clear(self):
		self.image = pygame.Surface((self.w, self.h))
		self.image.fill(self.c)
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def draw(self, x,y, r, c):
		pygame.draw.circle(self.image, c, (x, y), r)

class makeLine(pygame.sprite.Sprite):

	def __init__(self, x,y, w,h, c) -> None:
		super(makeLine, self).__init__()
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.c = c
		self.image = pygame.Surface((self.w, self.h))
		self.image.fill(c)

		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	def move(self, dx: int, dy: int):
		self.rect.x += dx
		self.rect.y += dy
		# print("move x{} y{}".format(dx, dy))

