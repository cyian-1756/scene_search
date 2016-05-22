#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description='Get useful porn search terms')
parser.add_argument("-n", help="Name of the porn star you're searching for")
parser.add_argument("-s", help="Name of the scene you're searching for")
args = parser.parse_args()

name_list = args.n.split()

scene_list = args.s.split()

name_first = name_list[0]
name_last = name_list[1]
name_whole = args.n

def get_scene_short():
    name = ''
    for i in scene_list:
        name = name + i[0]
    return name

scene_long = args.s
scene_short = get_scene_short()

print('{0} {1}'.format(name_whole, scene_long))
print('{0} {1}'.format(name_first, scene_long))
print('{0} {1}'.format(name_last, scene_long))
print('{0} {1}'.format(name_whole, scene_short))
print('{0} {1}'.format(name_first, scene_short))
print('{0} {1}'.format(name_last, scene_short))
