"""
Created on Sun Feb 21 19:25:30 2021

@author: Sule
@name: snake_game.py
@description: ->
	DOCSTRING:
"""
#!/usr/bin/env python3

# Importing the libraries
import pygame
import sys
main_clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (242, 209, 17)
PURPLE = (128, 0, 128)
ORANGE = (242, 118, 9)

class App():
	"""
	DOCSTRING:

	"""
	def __init__(self, width, height):
		self.width = width
		self.height = height

		pygame.init()
		self.screen = pygame.display.set_mode((width, height))
		self.font = pygame.font.SysFont(None, 20)

		self.click = False
		self.main_menu()

	def main_menu(self):
		pygame.display.set_caption('SNAKE (MAIN MENU)')
		while True:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/background.png")
			self.screen.blit(bg, (0, 0))

			mx, my = pygame.mouse.get_pos()

			draw_text('MAIN MENU', self.font, WHITE, self.screen, (30, 120))
			button_1 = button(self.screen, 'GAME', self.font, (30, 140), (150, 40), YELLOW, BLACK, 3, ORANGE)
			button_2 = button(self.screen, 'HIGH SCORES', self.font, (30, 200), (150, 40), YELLOW, BLACK, 3, ORANGE)
			button_3 = button(self.screen, 'OPTIONS', self.font, (30, 260), (150, 40), YELLOW, BLACK, 3, ORANGE)
			button_4 = button(self.screen, 'EXIT', self.font, (30, 320), (150, 40), YELLOW, BLACK, 3, ORANGE)

			if button_1.collidepoint((mx, my)):
				if self.click:
					self.game()

			if button_2.collidepoint((mx, my)):
				if self.click:
					self.high_scores()

			if button_3.collidepoint((mx, my)):
				if self.click:
					self.options()

			if button_4.collidepoint((mx, my)):
				if self.click:
					pygame.quit()
					sys.exit()

			self.click = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						self.click = True

			pygame.display.update()
			main_clock.tick(60)


	def game(self):
		pygame.display.set_caption('SNAKE (GAME)')
		running = True
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/game_Bg.png")
			self.screen.blit(bg, (0, 0))
			draw_text('GAME', self.font, WHITE, self.screen, (20, 20))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

			pygame.display.update()
			main_clock.tick(60)


	def high_scores(self):
		pygame.display.set_caption('SNAKE (HIGH SCORES)')
		running = True
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/background.png")
			self.screen.blit(bg, (0, 0))
			draw_text('HIGH SCORES', self.font, WHITE, self.screen, (20, 20))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

			pygame.display.update()
			main_clock.tick(60)


	def options(self):
		pygame.display.set_caption('SNAKE (OPTIONS)')
		running = True
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/background.png")
			self.screen.blit(bg, (0, 0))
			draw_text('OPTIONS', self.font, WHITE, self.screen, (20, 20))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

			pygame.display.update()
			main_clock.tick(60)


def draw_text(text, font, color, surface, pos, center=False):
	x, y = pos
	text = font.render(text, True, color)
	if center:
		text_rect = text.get_rect(center=(x, y))
	else:
		text_rect = text.get_rect(midleft=(x, y))
	surface.blit(text, text_rect)

def button(surface, text, font, pos, size, bg_color, text_color, border, border_color):
	x, y = pos
	width, height = size
	if border > 0:
		bg = pygame.Rect(x, y, width, height)
		pygame.draw.rect(surface, border_color, bg)

	btn = pygame.Rect(x+border, y+border, width-border*2, height-border*2)
	pygame.draw.rect(surface, bg_color, btn)
	draw_text(text, font, text_color, surface, (x + width/2, y + height/2), True)
	return btn

if __name__ == '__main__':
	app = App(874, 480)