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

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

           # R    G    B
GRAY     = (100, 100,  50)
BLACK    = ( 0,    0,   0)
WHITE    = (200, 250, 250)
RED      = (200,   0,   0)
GREEN    = (  0, 200,   0)
BLUE     = (  0,   0, 200)
YELLOW   = (255, 200,   0)
ORANGE   = (200, 120,   0)
PURPLE   = (250,   0, 200)
CYAN     = (  0, 250, 200)
