#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms

import numpy as np

import abstract as abt


class Circle(abt.Abstract):

    def compute_point(self, time):
        point = gms.Point()
        arr = np.zeros(3)
        arr[0] = self.__RADIUS*np.cos(self.__ANGVEL*time)
        arr[1] = self.__RADIUS*np.sin(self.__ANGVEL*time)
        arr[2] = 0.0
        arr = self.__ROTATION.dot(arr)
        point.x = arr[0]
        point.y = arr[1]
        point.z = arr[2]
        return point


    def __init__(self,
            frequency = rp.get_param('frequency', 3e1),
            radius = rp.get_param('radius', 1.0),
            rotation = np.array(
                rp.get_param('rotation', np.eye(3).tolist())),
            angvel = rp.get_param('angvel', 1.0)):
        self.__RADIUS = radius
        self.__ROTATION = rotation
        self.__ANGVEL = angvel
        abt.Abstract.__init__(self, frequency)



if __name__ == '__main__':
    tp = Circle()
