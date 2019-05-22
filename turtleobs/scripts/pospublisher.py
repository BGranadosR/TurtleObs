#!/usr/bin/env python

import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import turtlesim.srv

from std_msgs.msg import String
from turtlesim.msg import Pose
#from turtlesim.msg import Velocity
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from std_srvs.srv import Empty
import std_srvs.srv
#import math
#import time
#from std_srvs.srv import Empty

def poseCallback(pose_message):
    global x_t
    global y_t
    global theta_t
    
    x_t = pose_message.x
    y_t = pose_message.y
    theta_t = pose_message.theta

    #def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def initial():
    

#    rospy.wait_for_service('clear')
#    rospy.ServiceProxy('clear', std_srvs.srv.Clear)
              
    rospy.wait_for_service('kill')
    killer = rospy.ServiceProxy('kill', turtlesim.srv.Kill)
    killer('turtle1')   
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(1, 1, 0, 'turtle1')
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(2, 3, 0, 'obs1')
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(6, 5, 0, 'obs2')
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    spawner(8, 8, 0, 'obs3')
        
    
    
    
    
def listener():
       
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
    rospy.init_node('listener', anonymous=True)
    
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():

        print ('Xtortuga = ', x_t)
        print ('Ytortuga = ', y_t)
        print ('Orientacion = ', theta_t)
        rate.sleep()
        
def segunda():
      
        print ('segunda tarea /n')

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

#    def talker():
#    pub = rospy.Publisher('chatter', String, queue_size=10)
#    rospy.init_node('talker', anonymous=True)
#    rate = rospy.Rate(2) # 2hz
#    while not rospy.is_shutdown():
#        hello_str = "cadena en el log %s"% rospy.get_time()
#        rospy.loginfo(hello_str)
#        pub.publish(hello_str)
#        rate.sleep()

if __name__ == '__main__':
    try:
        initial()
        listener()
        segunda()
             
    except rospy.ROSInterruptException:
        pass
