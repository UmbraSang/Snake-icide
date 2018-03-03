import bottle
import os
import random



@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

	#http://www.pngmart.com/image/19182 lion head
    head_url = '%s://%s/static/head.png ' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#6b33ff',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
	

    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']
    #
	#
	#
	#
	#
	Matrix = [[0 for x in range(board_width)] for y in range(board_height)]
	
	##put food in 2D array
	food = data["food"]
	
	for food in food["data"]:
		Matrix[food["x"]][food["y"]] = -1
	
	##put snakes in 2D array
	snakes = data["snakes"]
	
	for snake in snakes["data"]:
		print(snake["body"]["id"])
		for body in snake.body.data:
			Matrix[body["x"]][body["y"]] = 1
	
	##establish where we are on board
	myX = data["you"]["body"]["data"]["x"]
	myY = data["you"]["body"]["data"]["y"]
	
	Matrix[myX][myY] = 10
			
	##
	
	




	
	#direction = random.choice(directions)
	
	
	
	
	direction =
    #
	#
	#
	#
	#
	print direction
    return {
        'move': direction,
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
