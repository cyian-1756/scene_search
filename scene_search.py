#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser(description='Get useful porn search terms')
parser.add_argument("-n", help="Name of the porn star you're searching for")
parser.add_argument("-s", help="Name of the scene you're searching for")
args = parser.parse_args()

if args.n and args.s:
    name_whole = args.n
    scene_long = args.s
    name_list = args.n.split()
    scene_list = args.s.split()
else:
    import easygui
    name_whole = easygui.enterbox('Pornstar name', 'Scene Search')
    scene_long = easygui.enterbox('Scene name', 'Scene Search')
    name_list = name_whole.split()
    scene_list = scene_long.split()

name_first = name_list[0]
name_last = name_list[1]


def get_scene_short():
    name = ''
    for i in scene_list:
        name = name + i[0]
    return name


scene_short = get_scene_short()

if args.s and args.n:
    print('{0} {1}'.format(name_whole, scene_long))
    print('{0} {1}'.format(name_first, scene_long))
    print('{0} {1}'.format(name_last, scene_long))
    print('{0} {1}'.format(name_whole, scene_short))
    print('{0} {1}'.format(name_first, scene_short))
    print('{0} {1}'.format(name_last, scene_short))
else:
    easygui.msgbox('{0} {1}\n{2} {3}\n{4} {5}\n{6} {7}\n{8} {9}\n{10} {11}'.format(name_whole, scene_long, name_first, scene_long, name_last, scene_long, name_whole, scene_short, name_first, scene_short, name_last, scene_short), 'Scene Search')
