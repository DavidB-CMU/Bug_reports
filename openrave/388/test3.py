#!/usr/bin/env python

#
# Test #3
# The default configuration of the robot
# has two links in self-collision,
# the number of adjacent links and non-adjacent links
# does not sum to the correct number.
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
robot_file = os.path.join(current_dir, 'test3_robot.robot.xml')
env.Load(robot_file)
testrobot = env.GetKinBody('testrobot')

# Set the camera viewing angle
viewer = env.GetViewer()
viewer.SetCamera([
    [-2.2672434e-03, -2.3854859e-01,  9.7112791e-01, -3.0416364e+00],
    [-9.9998839e-01, -3.5866221e-03, -3.2156431e-03, -6.2602991e-03],
    [ 4.2501560e-03, -9.7112393e-01, -2.3853769e-01,  1.4986903e+00],
    [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  1.0000000e+00]])

# Run test
CheckAdjacentLinks(testrobot)

# Load interactive python console
import IPython;
IPython.embed()
