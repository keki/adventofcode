from os import system
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

def has_double_small_cave(path):
	lc_only = [cave for cave in path if cave.islower() and cave != "start" and cave != "end"]
	num_of_lc = len(lc_only)
	num_of_distinct_lc = len(set(lc_only))
	return num_of_lc != num_of_distinct_lc

# can this step still be taken after this path?
def still_available(step, path):
	# everything goes until a small cave was touched twice
	if (has_double_small_cave(path)):
		return (not (step[0].islower() and step[0] in path) and
				not (step[1].islower() and step[1] in path))

	# end not reached and haven't touched any small caves twice yet, anything goes except start
	return not ("start" in step and "start" in path)

# remove steps with "used" small caves from cave_map
def valid_steps(cave_map, path):
	return [step for step in cave_map if still_available(step, path)]

#remove paths that don't end in "end"
def keep_good_paths(paths):
	return [path for path in paths if path[-1] == "end"]

def print_update(new_paths):
	system('clear')
	print(len(new_paths))
	for path in new_paths[-50:]:
		print(path)

paths = [["start"]]
done_paths = []
while(paths):
	new_paths = []
	for path in paths:
		# should store calculated next steps with paths to speed this up, but it's a nice Sunday outside, bye
		for ns in connections(path[-1], valid_steps(cave_map, path[:-1])):
			if (ns == "end"):
				done_paths.append(path + [ns])
			else:
				new_paths.append(path + [ns])
	print_update(new_paths)
	paths = new_paths

print("NUMBER OF PATHS: ", len(done_paths))

