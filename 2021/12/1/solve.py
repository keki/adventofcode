import numpy as np

cave_map = np.array(np.loadtxt('input', dtype=str, delimiter='-'))

# list possible steps given the current cave and a cave map
def connections(cave, cave_map):
	retval = []
	valid_steps = [step for step in cave_map if step[0] == cave or step[1] == cave]
	for step in valid_steps:
		if (step[0] == cave):
			retval.append(step[1])
		else:
			retval.append(step[0])
	return retval

# can this step still be taken after this path?
def still_available(step, path):
	return (not (step[0].islower() and step[0] in path) and
			not (step[1].islower() and step[1] in path))

# remove steps with "used" small caves from cave_map
def valid_steps(cave_map, path):
	return [step for step in cave_map if still_available(step, path)]

#remove paths that don't end in "end"
def remove_bad_paths(paths):
	return [path for path in paths if path[-1] == "end"]

paths = [["start"]]
has_more = True
while(has_more):
	has_more = False
	new_paths = []
	for path in paths:
		last_step = path[-1]
		remaining_map = valid_steps(cave_map, path[:-1])
		if(last_step == "end"):
			new_paths += [path]
		else:
			next_steps = connections(last_step, remaining_map)
			if (next_steps):
				has_more = True
				new_paths += [path + [step] for step in next_steps]
			else:
				new_paths += [path]
	paths = new_paths

good_paths = remove_bad_paths(paths)

for path in good_paths:
	print(path)

print(len(good_paths))

