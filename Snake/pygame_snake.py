import os
import sys
import pygame
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

border_width = 30
dis_width = 800
dis_height = 600

display = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake game by DashJC')

clock = pygame.time.Clock()

snake_block = 10
snakehead = pygame.image.load(resource_path('img/pixilart-drawing.png'))
snaketail = pygame.image.load(resource_path('img/pixil-frame-0_2.png'))
pointblock = pygame.image.load(resource_path('img/pixil-frame-0_3.png'))

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)


def your_score(score):
	score_surface = score_font.render("Score: " + str(score), True, yellow)
	display.blit(score_surface, (dis_width/2.3, 0))


def our_snake(snake_block, snake_list, snake_direction):
	head = snakehead
	if snake_direction == "right":
		head = pygame.transform.rotate(snakehead, 360)

	if snake_direction == "left":
		head = pygame.transform.rotate(snakehead, 180)

	if snake_direction == "up":
		head = pygame.transform.rotate(snakehead, 90)

	if snake_direction == "down":
		head = pygame.transform.rotate(snakehead, 270)

	display.blit(head, (snake_list[-1][0], snake_list[-1][1]))

	for x in snake_list[:-1]:
		display.blit(snaketail, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
	mesg = font_style.render(msg, True, color)
	display.blit(mesg, [dis_width / 5, dis_height / 3])


def gameLoop():  # creating a function
	game_over = False
	game_close = False

	snake_speed = 5
	snake_direction = ""

	x1 = dis_width / 2
	y1 = dis_height / 2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0 + snake_block, dis_width - snake_block) / 10.0) * 10.0
	foody = round(random.randrange((0 + border_width) + snake_block, dis_height - snake_block) / 10.0) * 10.0

	snake_Head = []
	snake_Head.append(x1)
	snake_Head.append(y1)
	snake_List.append(snake_Head)

	our_snake(snake_block, snake_List, "up")

	while not game_over:

		while game_close:
			display.fill(blue)
			message("You Lost! Press Q-Quit or C-Play Again", red)

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if snake_direction != "right":
						snake_direction = "left"
						x1_change = -snake_block
						y1_change = 0
				elif event.key == pygame.K_RIGHT:
					if snake_direction != "left":
						snake_direction = "right"
						x1_change = snake_block
						y1_change = 0
				elif event.key == pygame.K_UP:
					if snake_direction != "down":
						snake_direction = "up"
						y1_change = -snake_block
						x1_change = 0

				elif event.key == pygame.K_DOWN:
					if snake_direction != "up":
						snake_direction = "down"
						y1_change = snake_block
						x1_change = 0

		if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < border_width:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		display.fill(blue)
		# top border
		pygame.draw.rect(display, black, [0, 0, dis_width, border_width])
		display.blit(pointblock, [foodx, foody, snake_block, snake_block])

		snake_Tail = []
		snake_Tail.append(x1)
		snake_Tail.append(y1)
		snake_List.append(snake_Tail)

		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Tail:
				game_close = True

		our_snake(snake_block, snake_List, snake_direction)
		your_score(Length_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			Length_of_snake += 1
			snake_speed += 0.05
			while True:
				foodx = round(random.randrange(0 + snake_block, dis_width - snake_block) / 10.0) * 10.0
				foody = round(random.randrange((0 + border_width) + snake_block, dis_height - snake_block) / 10.0) * 10.0

				food_rect = display.blit(pointblock, [foodx, foody, snake_block, snake_block])
				# food_rect = pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
				if not any(food_rect.collidepoint(*pos) for pos in snake_List):
					break

		clock.tick(snake_speed)

	pygame.quit()
	quit()


gameLoop()
