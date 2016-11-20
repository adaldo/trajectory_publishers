#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms


class AbstractTP:


    def compute_point(self, time):
        raise NotImplementedError()
        #return gms.Point()


    def __init__(self,
            frequency=rp.get_param('frequency', 1e1)):
        rp.init_node('abstract_tp')
        pub = rp.Publisher(
            name='trajectory_point',
            data_class=gms.Point,
            queue_size=10)
        RATE = rp.Rate(frequency)
        INIT_TIME = rp.get_time()
        while not rp.is_shutdown():
            time = rp.get_time()-INIT_TIME
            #rp.logwarn(time)
            point = self.compute_point(time)
            #rp.logwarn(point)
            pub.publish(point)
            RATE.sleep()


if __name__ == '__main__':
    tp = AbstractTP()
