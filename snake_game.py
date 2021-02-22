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
import random
from text_input import InputBox
main_clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (74, 145, 35)
YELLOW = (242, 209, 17)
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
		self.font = pygame.font.SysFont(None, 22)
		self.font_big = pygame.font.SysFont(None, 48)

		icon = pygame.image.load("images/icon.png")
		pygame.display.set_icon(icon)

		self.main_menu()

	def main_menu(self):
		pygame.display.set_caption('SNAKE (MAIN MENU)')
		click = False
		while True:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/background.png")
			self.screen.blit(bg, (0, 0))
			draw_text('MAIN MENU', self.font, WHITE, self.screen, (20, 20))
			button_game = button(self.screen, 'GAME', self.font, (20, 140), (160, 40), YELLOW, BLACK, 3, ORANGE)
			button_hs = button(self.screen, 'HIGH SCORES', self.font, (20, 200), (160, 40), YELLOW, BLACK, 3, ORANGE)
			button_options = button(self.screen, 'OPTIONS', self.font, (20, 260), (160, 40), YELLOW, BLACK, 3, ORANGE)
			button_exit = button(self.screen, 'EXIT', self.font, (20, 320), (160, 40), YELLOW, BLACK, 3, ORANGE)
			draw_text('GAME DEVELOPED BY SULE', self.font, WHITE, self.screen, (20, self.height-20))
			
			mx, my = pygame.mouse.get_pos()
			if button_game.collidepoint((mx, my)):
				if click:
					self.game()

			if button_hs.collidepoint((mx, my)):
				if click:
					self.high_scores()

			if button_options.collidepoint((mx, my)):
				if click:
					self.options()

			if button_exit.collidepoint((mx, my)):
				if click:
					pygame.quit()
					sys.exit()

			click = False
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
						click = True

			pygame.display.update()
			main_clock.tick(60)

	def draw_game_hud(self, score, bg_included = True):
		if bg_included:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/game_bg.png")
			self.screen.blit(bg, (0, 0))

		draw_text('GAME', self.font, WHITE, self.screen, (15, 20))
		draw_text(f'SCORE: {score}', self.font, WHITE, self.screen, (15, 40))
		pygame.draw.line(self.screen, BLACK, (1, 1), (self.width, 1), 4) # up
		pygame.draw.line(self.screen, BLACK, (0, self.height-3), (self.width, self.height-3), 4) # down

		pygame.draw.line(self.screen, BLACK, (1, 0), (1, self.height), 4) # left
		pygame.draw.line(self.screen, BLACK, (self.width-3, 0), (self.width-3, self.height), 4) # right

		pygame.draw.line(self.screen, BLACK, (0, 60), (self.width, 60), 4) # up2

	def get_food_pos(self, size):
		food_x = round(random.randrange(10, self.width - size) // float(size)) * float(size)
		food_y = round(random.randrange(70, self.height - size) // float(size)) * float(size)
		return food_x, food_y

	def game(self):
		pygame.display.set_caption('SNAKE (GAME)')
		snake_block = 13
		snake_speed = 15
	 
		x1 = round((self.width / 2) // snake_block) * snake_block
		y1 = round((self.height / 2) // snake_block) * snake_block
		food_x, food_y = self.get_food_pos(snake_block)
	 
		x1_change = 0
		y1_change = 0
		snake_list = []
		score = 1

		game_on = True
		while game_on:
			self.draw_game_hud(score)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						game_on = False
					if event.key == pygame.K_LEFT and x1_change != snake_block:
						x1_change = -snake_block
						y1_change = 0
					elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
						x1_change = snake_block
						y1_change = 0
					elif event.key == pygame.K_UP and y1_change != snake_block:
						y1_change = -snake_block
						x1_change = 0
					elif event.key == pygame.K_DOWN and y1_change != -snake_block:
						y1_change = snake_block
						x1_change = 0

			# Check if snake went out of screen
			if x1 >= self.width or x1 < 0 or y1 >= self.height or y1 < 65:
				self.finish_screen(score)

			# Move snake
			x1 += x1_change
			y1 += y1_change

			snake_head = []
			snake_head.append(x1)
			snake_head.append(y1)
			snake_list.append(snake_head)
			if len(snake_list) > score:
				del snake_list[0]

			# Check if snake collides with itself
			for x in snake_list[:-1]:
				if x == snake_head:
					self.finish_screen(score)

			# Draw snake
			for idx, x in enumerate(snake_list):
				if idx == len(snake_list) - 1:
					head = pygame.draw.rect(self.screen, ORANGE, (x[0], x[1], snake_block, snake_block))
				else:
					pygame.draw.rect(self.screen, BLACK, (x[0], x[1], snake_block, snake_block))

			# Food drawing and check
			food_rect = pygame.draw.rect(self.screen, RED, [food_x, food_y, snake_block, snake_block])
			food_img = pygame.image.load("images/apple.png")
			picture = pygame.transform.scale(food_img, (20, 20))
			self.screen.blit(picture, (food_x-5, food_y-5))

			if food_rect.collidepoint((x1, y1)):
				food_x, food_y = self.get_food_pos(snake_block)
				score += 1

			pygame.display.update()
			main_clock.tick(snake_speed)

	def finish_screen(self, score):
		click = False
		running = True
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/finish_bg.jpg")
			self.screen.blit(bg, (0, 0))
			self.draw_game_hud(score, False)

			draw_text('GAME OVER', self.font_big, WHITE, self.screen, (self.width / 2, 32), True)
			button_restart = button(self.screen, 'RESTART', self.font, (15, 120), (180, 40), GREEN, WHITE, 3, BLACK)
			button_save = button(self.screen, 'SAVE HIGH SCORE', self.font, (15, 180), (180, 40), GREEN, WHITE, 3, BLACK)
			button_hs = button(self.screen, 'HIGH SCORE', self.font, (15, 240), (180, 40), GREEN, WHITE, 3, BLACK)
			button_options = button(self.screen, 'OPTIONS', self.font, (15, 300), (180, 40), GREEN, WHITE, 3, BLACK)
			button_exit = button(self.screen, 'EXIT', self.font, (15, 360), (180, 40), GREEN, WHITE, 3, BLACK)
			
			mx, my = pygame.mouse.get_pos()
			if button_restart.collidepoint((mx, my)):
				if click:
					self.game()

			if button_save.collidepoint((mx, my)):
				if click:
					self.save_hs(score)

			if button_hs.collidepoint((mx, my)):
				if click:
					self.high_scores()

			if button_options.collidepoint((mx, my)):
				if click:
					self.options()

			if button_exit.collidepoint((mx, my)):
				if click:
					pygame.quit()
					sys.exit()

			click = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.main_menu()
						running = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						click = True

			pygame.display.update()
			main_clock.tick(60)

	def save_hs(self, score):
		pygame.display.set_caption('SNAKE (SAVE HIGH SCORE)')
		running = True
		input_name = InputBox(280, 200, 320, 40, '', BLACK, WHITE)
		click = False
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/finish_bg.jpg")
			self.screen.blit(bg, (0, 0))
			self.draw_game_hud(score, False)

			draw_text('SAVE HIGH SCORE', self.font_big, WHITE, self.screen, (self.width / 2, 32), True)
			draw_text(f'Your score is: {score}', self.font, WHITE, self.screen, (self.width / 2, 120), True)
			draw_text('Are you sure you want to save it?', self.font, WHITE, self.screen, (self.width / 2, 140), True)
			draw_text('Please enter your name below', self.font, WHITE, self.screen, (self.width / 2, 160), True)
			draw_text('If you dont want to save your score, press ESC', self.font, WHITE, self.screen, (self.width / 2, 180), True)
			button_save = button(self.screen, 'SAVE SCORE', self.font, (280, 380), (320, 40), GREEN, WHITE, 3, BLACK)
			input_name.draw(self.screen)
			
			mx, my = pygame.mouse.get_pos()
			if button_save.collidepoint((mx, my)):
				if click:
					input_name.text.replace(',', '.')
					save_hs(input_name.text, score)
					input_name.text = ''
					running = False

			click = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						click = True

				input_name.handle_event(event)
			input_name.update()

			pygame.display.update()
			main_clock.tick(60)


	def high_scores(self):
		pygame.display.set_caption('SNAKE (HIGH SCORES)')
		running = True
		while running:
			self.screen.fill(BLACK)
			bg = pygame.image.load("images/finish_bg.jpg")
			self.screen.blit(bg, (0, 0))
			draw_text('HIGH SCORES', self.font, WHITE, self.screen, (20, 20))

			tmp_y = 60
			recorders = load_hs_file(20)
			for count, recorder in enumerate(recorders, 1):
				draw_text(f'{count}. {recorder} // {recorders[recorder]}', self.font, BLACK, self.screen, (20, tmp_y))
				tmp_y += 20

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


def draw_text(text, font, color, surface, pos, center=False, big=False):
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

def save_hs(name, score):
	recorders = {}
	# Load old recorders from file
	with open('highscores.txt') as file:
		for line in file.readlines():
			line = line.strip()
			line = line.split(',')
			recorders[line[0]] = int(line[-1])
	# Add new recorder to dictionary
	recorders[name] = score

	# Sort them and save them to file
	with open('highscores.txt', 'w') as file:
		for item in sorted(recorders, key=recorders.get, reverse=True):
			file.write(f'{item}, {recorders[item]}\n')

def load_hs_file(max = 10):
	recorders = {}
	count = 0
	with open('highscores.txt') as file:
		for line in file.readlines():
			line = line.strip()
			line = line.split(',')
			recorders[line[0]] = int(line[-1])
			count += 1

			if count == max:
				break
	return recorders


if __name__ == '__main__':
	# load_hs_file(5)
	app = App(870, 480)