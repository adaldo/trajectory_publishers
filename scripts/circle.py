#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms

import numpy as np

import abstract as abt

import threading as thd
import dynamic_reconfigure.server as drs
import trajpub.cfg.CircleConfig as pc



class Circle(abt.Abstract):


    def reconfig_callback(self, config, level):
        self.__LOCK.acquire()
        self.__CENTER = np.array([config["x0"], config["y0"], config["z0"]])
        self.__RADIUS = config["radius"]
        self.__ANGVEL = config["speed"]/self.__RADIUS
        self.__LOCK.release()
        return config


    def compute_point(self, time):
        point = gms.Point()
        arr = np.zeros(3)
        self.__LOCK.acquire()
        arr[0] = self.__RADIUS*np.cos(self.__ANGVEL*time)
        arr[1] = self.__RADIUS*np.sin(self.__ANGVEL*time)
        arr[2] = 0.0
        arr = self.__ROTATION.dot(arr)
        arr += self.__CENTER
        point.x = arr[0]
        point.y = arr[1]
        point.z = arr[2]
        self.__LOCK.release()
        return point


    def __init__(self,
            frequency = rp.get_param('frequency', 3e1),
            center = np.array(
                rp.get_param('center', np.zeros(3).tolist())),
            radius = rp.get_param('radius', 1.0),
            rotation = np.array(
                rp.get_param('rotation', np.eye(3).tolist())),
            speed = rp.get_param('speed', 1.0)):
        abt.Abstract.__init__(self, frequency)
        self.__LOCK = thd.Lock()
        self.__CENTER = center
        self.__RADIUS = radius
        self.__ROTATION = rotation
        self.__ANGVEL = speed/radius
        drs.Server(pc, self.reconfig_callback)



if __name__ == '__main__':
    rp.init_node('circle')
    tp = Circle()
    tp.start()
