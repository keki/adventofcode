# INPUT
target_area = {
	'x_min': 137,
	'x_max': 171,
	'y_min': -98,
	'y_max': -73
}

# test input
# target_area = {
# 	'x_min': 20,
# 	'x_max': 30,
# 	'y_min': -10,
# 	'y_max': -5
# }

print(target_area);

def step(probe):
	new_probe = {}
	new_probe['x'] = probe['x'] + probe['v_x']
	new_probe['y'] = probe['y'] + probe['v_y']
	if (probe['v_x'] > 0):
		new_probe['v_x'] = probe['v_x'] - 1
	elif (probe['v_x'] < 0):
		new_probe['v_x'] = probe['v_x'] + 1
	else:
		new_probe['v_x'] = 0
	new_probe['v_y'] = probe['v_y'] - 1
	return new_probe

def in_target_area(probe, target_area):
	return (probe['x'] >= target_area['x_min'] and
		probe['x'] <= target_area['x_max'] and
		probe['y'] >= target_area['y_min'] and
		probe['y'] <= target_area['y_max'])

def already_missed(probe, target_area):
	return (probe['x'] > target_area['x_max'] or probe['y'] < target_area['y_min'])

max_height = 0
# v_x will work if (v_x * (v_x+1)) / 2 is between x_min and x_max
# this gives the most number of steps available for flying up
# but I'm not doing the math here
for v_x in range(1, 100):
	# v_y can only work if v_y <= abs(y_min)
	# because after v_y steps it will peak, after 2 * v_y it will reach y = 0 again with the same v_y speed
	# then if original v_y was too big it will simply overshoot in one step
	for v_y in range(1,abs(target_area['y_min'])+1):
		target_hit = False
		launch_max_height = 0
		probe = {
			'v_x': v_x,
			'v_y': v_y,
			'x': 0,
			'y': 0
		}
		while (not already_missed(probe, target_area)):
			if (launch_max_height < probe['y']):
				launch_max_height = probe['y']
			if (in_target_area(probe, target_area)):
				target_hit = True
				break
			probe = step(probe)
		if(target_hit):
			if (max_height < launch_max_height):
				max_height = launch_max_height
			print("TARGET HIT at (", probe['x'], ",", probe['y'], "), launched: (",v_x, ",", v_y, "), max_height: ", launch_max_height)

print("MAX HEIGHT: ", max_height);

