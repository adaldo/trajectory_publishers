#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms
import abstract_tp as atp


class ZeroTP(atp.AbstractTP):

    def compute_point(self, time):
        #raise NotImplementedError()
        return gms.Point()



if __name__ == '__main__':
    tp = ZeroTP()
