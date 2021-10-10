import pygame
import json
import asset
import random

with open('settings.json', 'r') as src:
	prp = json.load(src)

pygame.init()
screen_size = screen_width, screen_height = prp['window']['screen']['width'], prp['window']['screen']['height']
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(prp['window']['caption'])
# Objects
container = asset.cnr(screen_width/2, screen_height/2, screen_width, screen_height, 'black')
pointer = asset.makeLine(container.x, container.y, 3, container.h, 'red')
# pointY = asset.makeLine(container.x, container.y, container.w, 3, 'green')
if prp['graph']['debug']:
	pointY = asset.makeLine(container.x, container.y, container.w, 3, 'green')
else:
	pointY = asset.makeLine(container.x, container.y, container.w, 0, container.c)
# Groups
objects = pygame.sprite.Group()

objects.add(container)
objects.add(pointer)
objects.add(pointY)
# Add Objects ^There

lx = pointer.rect.x-container.x+pointer.w/2
ly = pointY.rect.y-container.y+pointY.h/2

steps = container.w/prp['graph']['steps']

colorList = prp['graph']['colors']
cc = random.choice(colorList)
ticker = prp['graph']['TPS']
running = True

while running:

	screen.fill(prp['window']['screen']['color'])
	objects.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	if pointer.rect.x >= container.x + container.w-pointer.w:
		pointer.rect.x -= container.w
		cc = random.choice(colorList)
		container.clear()
		lx = 0
		ly = random.randint(container.y, container.y+container.h)

	if ticker <= 1:
		pointY.rect.y = random.randint(container.y, container.y+container.h)

		pygame.draw.circle(container.image, cc, (pointer.rect.x-container.x+26, pointY.rect.y-container.y+pointY.h/2), 3)
		pygame.draw.line(container.image, cc, (lx, ly), (pointer.rect.x-container.x+26, pointY.rect.y-container.y+pointY.h/2), prp['graph']['lineWidth'])
		lx = pointer.rect.x-container.x+26
		ly = pointY.rect.y-container.y+pointY.h/2
		
		pointer.move(steps, 0)
		pygame.display.set_caption(f"Value: {pointY.rect.y-container.y+pointY.h/2}")
		ticker = prp['graph']['TPS']
	else:
		ticker -= 1

	pygame.display.flip()

pygame.quit()
exit()