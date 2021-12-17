# INPUT
target_area = {
	'x_min': 137,
	'x_max': 171,
	'y_min': -98,
	'y_max': -73
}

# TEST INPUT
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

on_target_launches = 0

# brute force v_x range: min:1, max:x_max + 1, any larger will overshoot in one step
# smarter range is where (v_x * (v_x + 1)) / 2 > x_min, but that doesn't shave off a lot of steps so who cares
for v_x in range(1, target_area['x_max'] + 1):
	# brute force v_y range: +- y_min -- anything bigger will overshoot in one step
	for v_y in range(-abs(target_area['y_min'])-1,abs(target_area['y_min'])+1):
		probe = {
			'v_x': v_x,
			'v_y': v_y,
			'x': 0,
			'y': 0
		}
		target_hit = False
		while (not already_missed(probe, target_area)):
			if (in_target_area(probe, target_area)):
				target_hit = True
				break
			probe = step(probe)
		if (target_hit):
			on_target_launches += 1
			print("TARGET HIT at (", probe['x'], ",", probe['y'], "), launched: (",v_x, ",", v_y, ")")

print("ON TARGET LAUNCHES: ", on_target_launches)

