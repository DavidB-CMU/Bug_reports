#!/usr/bin/env python

#
# Test #1
#

import openravepy
import prpy
import herbpy

import os # path


def CheckAdjacentLinks(robot):
    """
    Check the link adjacency for an OpenRAVE robot.

    For a robot with N links, the number of adjacent link pairs + the
    number of non-adjacent pairs should equal N x (N-1)/2

    @param robot: An OpenRAVE robot object.
    """
    robot_links = robot.GetLinks()
    num_robot_links = len(robot_links)
    expected_num_link_pairs = num_robot_links * (num_robot_links - 1.0)/2.0

    adjacent_links = robot.GetAdjacentLinks()
    non_adjacent_links = robot.GetNonAdjacentLinks()
    num_adjacent_links = len(adjacent_links)
    num_non_adjacent_links = len(non_adjacent_links)
    actual_num_link_pairs = num_adjacent_links + num_non_adjacent_links

    print "robot.GetAdjacentLinks() = ", robot.GetAdjacentLinks()
    print "robot.GetNonAdjacentLinks() = ", robot.GetNonAdjacentLinks()

    if expected_num_link_pairs == actual_num_link_pairs:
        print("\nLink pairs are correct\n")
    else:
        print("\nERROR: some link pairs are missing\n")


# Initialize OpenRAVE.
openravepy.RaveInitialize(True)
openravepy.misc.InitOpenRAVELogging()
openravepy.RaveSetDebugLevel(openravepy.DebugLevel.Fatal)

env = openravepy.Environment()
env.SetViewer('qtcoin') # attach viewer

# Load the robot
current_dir = os.path.dirname(os.path.abspath(__file__))
robot_file = os.path.join(current_dir, 'test1_robot.robot.xml')
env.Load(robot_file)
testrobot = env.GetKinBody('testrobot')

# Run test
CheckAdjacentLinks(testrobot)

# Load interactive python console
#import IPython;
#IPython.embed()
