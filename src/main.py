from setup import *
import math
import threading

def drawCircles(canvas, background, circleList, start, step):
	# background = pygame.image.load("assets/GGB.jpeg")

	for circle in circleList:
		totalR = 0
		totalG = 0
		totalB = 0
		count = 0
		
		for i in range(circle.left, circle.right)[start::step]:
			for j in range(circle.top, circle.bottom)[start::step]:

				#check if this pixel is in the circle
				distance = math.sqrt((circle.centery - j)**2 + (circle.centerx - i)**2)
				radius = circle.width//2

				#only add the rgb values for pixels inside the circle
				if distance <= radius:

					totalR += background.get_at((i, j))[0]
					totalG += background.get_at((i, j))[1]
					totalB += background.get_at((i, j))[2]
					count += 1

		centerx = circle.centerx

		centery = circle.centery

		radius = circle.width//2

		#handle division by 0
		if count != 0:

			averageR = totalR//count

			averageG = totalG//count

			averageB = totalB//count
		else:
			averageR = 0
			averageB = 0
			averageG = 0
		
		pygame.draw.circle(canvas, (averageR, averageG, averageB), (centerx, centery), radius)


def updateCircles(canvas, background, canvasWidth, canvasHeight, circleList, mousePos):

	canvas.fill(colors["PURPLE"])


	#See if we clicked in any of the circles
	for circle in circleList:
		distance = math.sqrt((circle.centery - mousePos[1])**2 + (circle.centerx - mousePos[0])**2)
		radius = circle.width//2

		#Delete the circle and replace it with 4 smaller ones
		if distance <= radius:
			#We will just use blue for now, we change the color
			circle1 = pygame.draw.circle(canvas, colors["BLUE"], (circle.centerx - radius//2, circle.centery- radius//2), radius//2)

			circle2 = pygame.draw.circle(canvas, colors["BLUE"], (circle.centerx + radius//2, circle.centery- radius//2), radius//2)

			circle3 = pygame.draw.circle(canvas, colors["BLUE"], (circle.centerx - radius//2, circle.centery + radius//2), radius//2)

			circle4 = pygame.draw.circle(canvas, colors["BLUE"], (circle.centerx + radius//2, circle.centery + radius//2), radius//2)

			circleList.remove(circle)

			circleList.append(circle1)
			circleList.append(circle2)
			circleList.append(circle3)
			circleList.append(circle4)

			break

	#TODO: Set the thread count with commandline
	threadCount = 6

	thread1 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 0, threadCount))
	thread2 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 1, threadCount))
	thread3 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 2, threadCount))
	thread4 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 3, threadCount))
	thread5 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 4, threadCount))
	thread6 = threading.Thread(target=drawCircles, args=(canvas, background, circleList, 5, threadCount))


	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread5.start()
	thread6.start()

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	thread5.join()
	thread6.join()


def gameLoop(canvas, background, canvasWidth, canvasHeight):

	circleList = populateCanvas(canvas, canvasWidth, canvasHeight)

	done = False

	canvas.fill(colors["PURPLE"])

	drawCircles(canvas, background, circleList, 0, 1)

	while(not done):
		#canvas.blit(background, (0,0))

		for event in pygame.event.get():
		    #Enter will exit the test
		    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
		        done = True
		    elif event.type == pygame.MOUSEBUTTONUP:

		    	mousePos = pygame.mouse.get_pos()

	   		    #Check for mouse click collision within the circles and update them
	    		updateCircles(canvas, background, canvasWidth, canvasHeight, circleList, mousePos)


		

		pygame.display.update()

def main():

	background = argParse()

	canvas, canvasWidth, canvasHeight = pygameSetup()

	gameLoop(canvas, background, canvasWidth, canvasHeight)

if __name__ == '__main__':
	main()
