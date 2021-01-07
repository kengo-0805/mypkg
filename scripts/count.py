#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count')                                # ノード名「count」に設定
pub = rospy.Publisher('count_up', Int32, queue_size=1)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(10)                                   # 10Hzで実行
n = 0
while not rospy.is_shutdown():
    n += 1

    print(n)
    if n // 10 == 3:
        print("💩💩💩💩💩")
    elif n % 3 == 0:
        print("うんこ")
    elif n % 10 == 3:
        print("💩💩💩💩💩")
    else:
        print("💩")
    pub.publish(n)
    rate.sleep()
