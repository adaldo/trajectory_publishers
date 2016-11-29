#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms
import abstract as abt

import dynamic_reconfigure.server as drs
import trajpub.cfg.ConstantConfig as pc

import threading as thd


class Constant(abt.Abstract):

    def reconfig_callback(self, config, level):
        self.__LOCK.acquire()
        self.__x = config["x"]
        self.__y = config["y"]
        self.__z = config["z"]
        self.__LOCK.release()
        return config


    def compute_point(self, time):
        point = gms.Point()
        self.__LOCK.acquire()
        point.x = self.__x
        point.y = self.__y
        point.z = self.__z
        self.__LOCK.release()
        return point


    def __init__(self,
            frequency=rp.get_param('frequency', 3e1),
            x=rp.get_param('x', 0.0),
            y=rp.get_param('y', 0.0),
            z=rp.get_param('z', 0.0)):
        abt.Abstract.__init__(self, frequency)
        self.__LOCK = thd.Lock()
        self.__x = x
        self.__y = y
        self.__z = z
        drs.Server(pc, self.reconfig_callback)



if __name__ == '__main__':
    rp.init_node('constant')
    tp = Constant()
    tp.start()
