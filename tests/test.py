from RoboFlowSocket import RoboFlowSocket

# 连接机械臂服务端IP地址的端口
erobot = RoboFlowSocket()

# # 测试读取机械臂信息
cur_angles = erobot.get_angles()
print(cur_angles)
cur_coords = erobot.get_coords()
print(cur_coords)

# 控制机械臂关节运动90°
angles = [90.0, -90.0, 0.0, -90.0, 0.0, 0.0]
erobot.set_angles(angles, 500)

