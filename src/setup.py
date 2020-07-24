from exceptions import *
from globals import *
import pygame
import sys
from setup import *

def argParse():
	try:
	#TODO: ARG PARSE
		if(len(sys.argv) != 2):
			raise invalidArgCount
		else:
			background = pygame.image.load("assets/{}".format(sys.argv[1]))
			#threadCount = sys.argv[2]


	except invalidArgCount:
		print("\n Error, correct usage is: python3 main.py fileName threadCount")
		exit(0)

	return background

def pygameSetup():

	canvasWidth = 1000

	canvasHeight = 1000

	pygame.init()

	canvas = pygame.display.set_mode((canvasWidth, canvasHeight))

	return canvas, canvasWidth, canvasHeight

def populateCanvas(canvas, canvasWidth, canvasHeight):
	circleList = []

	circle1 = pygame.draw.circle(canvas, (0, 0, 255), (canvasWidth//4, canvasHeight//4), canvasWidth//4)

	circle2 = pygame.draw.circle(canvas, (0, 0, 255), (3 * canvasWidth//4, canvasHeight//4), canvasWidth//4)

	circle3 = pygame.draw.circle(canvas, (0, 0, 255), (canvasWidth//4, 3 * canvasHeight//4), canvasWidth//4)

	circle4 = pygame.draw.circle(canvas, (0, 0, 255), (3 * canvasWidth//4, 3 * canvasHeight//4), canvasWidth//4)

	circleList.append(circle1)
	circleList.append(circle2)
	circleList.append(circle3)
	circleList.append(circle4)


	return circleList