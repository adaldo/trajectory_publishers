#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms
import abstract_tp as atp


class ConstantTP(atp.AbstractTP):


    def compute_point(self, time):
        point = gms.Point()
        point.x = self.__x
        point.y = self.__y
        point.z = self.__z
        return point


    def __init__(self,
            frequency=rp.get_param('frequency', 1e1),
            x=rp.get_param('x', 0.0),
            y=rp.get_param('y', 0.0),
            z=rp.get_param('z', 0.0)):
        self.__x = x
        self.__y = y
        self.__z = z
        atp.AbstractTP.__init__(self, frequency)




if __name__ == '__main__':
    tp = ConstantTP()
