#
#
#Code referenced from https://github.com/noahspriggs/battlesnake-python/blob/master/app/main.py
from AStar import *
import bottle
import os
import random
import math
import copy

OURID
SNAKE = 1
FOOD = 2
SAFENODE = 3


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'battlesnake-python'
    }


#prints grid
def printg(grid):
	for x in grid:
		print x

#initialize grid data
#map fill
def init(data):
	grid = [[0 for col in xrange(data['height'])] for row in xrange(data['width'])]
	
	for s in data['snakes']:
		if s['id'] == OURID:
			mysnake = s
		for coord in s['coords']:
			grid[coord[0]][coord[1]] = SNAKE

	
	for foods in data['food']:
		grid[foods[0]][f[1]] = FOOD

	return grid, mysnake

def direction(start, dest):
	dx = start[0] - dest[0]
	dy = start[0] - dest[0]

	if dx == 1:
		return 'east'
	
	elif dx == -1:
		return 'west'

	elif dy == -1:
		return 'north'
	
	elif dy == 1:
		return 'south'
	


def getID(data):
	id = data['you']
	return id

def distance(p, q):
	dx = abs(p[0] - q[0])
	dy = abs(p[1] - q[1])
	ans = dx + dy
	return ans

@bottle.post('/move')
def move():

	print "Hello world"
	data = bottle.request.json
	OURID = getID(data)
	
	grid, mysnake = init(data)
	
	printg(grid)
	sys.stdout.flush()

	mynakeHead = data['coords'[0]
	mysnakeCoords = mysnake['coords']

	foodList = sorted(data['food'], key = lambda p: distance(p, mysnakeHead))
	
	path = None
	for food in foodList:
		print food
		sys.stdout.flush()
		path = a_star(mysnake, food, grid, mysnakeCoords)	
		if path:
			print food
			sys.stdout.flush()
			break

			
	print "PATH"
	print path
	sys.stdout.flush()
	dir = direction(path[0], path[1])
	

	print dir
	sys.stdout.flush()
    return {
        'move': dir,
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
