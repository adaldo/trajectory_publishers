#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms


class Abstract:


    def compute_point(self, time):
        raise NotImplementedError()
        #return gms.Point()


    def __init__(self,
            frequency=rp.get_param('frequency', 3e1)):
        self.__pub = rp.Publisher(
            name='point',
            data_class=gms.Point,
            queue_size=10)
        self.__RATE = rp.Rate(frequency)
        self.__INIT_TIME = rp.get_time()

    def start(self):
        while not rp.is_shutdown():
            time = rp.get_time()-self.__INIT_TIME
            #rp.logwarn(time)
            point = self.compute_point(time)
            #rp.logwarn(point)
            self.__pub.publish(point)
            self.__RATE.sleep()


if __name__ == '__main__':
    rp.init_node('abstract')
    tp = Abstract()
    tp.start()
