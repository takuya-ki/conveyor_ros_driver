#!/usr/bin/env python

import rospy
from conveyor.srv import SetCommand, SetCommandResponse

from dmh_commander import DMHCommander


class ConveyorNode:
    """Class to handle setting commands."""
    def __init__(self, ip, sockport):
        self._dmhctr = DMHCommander(ip, sockport)
        rospy.loginfo(self._dmhctr)
        rospy.sleep(1)
        self.set_command_srv = rospy.Service(
            "/conveyor/set_command",
            SetCommand,
            self.handle_set_command)

    def handle_set_command(self, req):
        """To handle sending commands via socket connection."""
        rospy.loginfo(str(req.command))
        self._dmhctr.sendcommand(str(req.command))
        rospy.sleep(1)
        return SetCommandResponse(
            success=None,  # TODO: implement
            message=None)  # TODO: implement


if __name__ == '__main__':
    rospy.init_node('conveyor_node', log_level=rospy.DEBUG)
    ip = rospy.get_param(
        "/conveyor/ip", "169.0.0.1")
    sockport = rospy.get_param(
        "/conveyor/sockport", 50007)
    rospy.loginfo(str(ip))
    rospy.loginfo(str(sockport))
    node = ConveyorNode(ip, sockport)
    rospy.spin()
