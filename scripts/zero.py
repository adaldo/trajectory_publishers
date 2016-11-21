#! /usr/bin/env python

import rospy as rp
import geometry_msgs.msg as gms
import abstract as abt


class Zero(atp.Abstract):

    def compute_point(self, time):
        #raise NotImplementedError()
        return gms.Point()



if __name__ == '__main__':
    rp.init_node('zero')
    tp = Zero()
    tp.start()
    
