#	Date: 		22/06/2015
#	Author: 	TarCode
#	File:		memoryPuzzle.py
#	Ref:		tutorial on http://inventwithpython.com/pygame/
import random, pygame, sys
from pygame.locals import *

FPS = 50 		# frames per second - program speed
WINDOWWIDTH = 800 	# width in pixels
WINDOWHEIGHT = 600 	# height in pixels
REVEALSPEED = 8 	# speed boxes get revealed
BOXSIZE = 100 		# box height and width in pixels
GAPSIZE = 25 		# gap size between boxes in pixels
BOARDWIDTH = 4 		# number of columns of icons
BOARDHEIGHT = 4 	# number of rows of icons
