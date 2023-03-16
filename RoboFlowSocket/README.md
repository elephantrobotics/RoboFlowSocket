# RoboFlowSocket

**This is python API for mycobot pro 600**

# Mycobot pro 600

Import to your project:

```python
from RoboFlowSocket import RoboFlowSocket

erobot = RoboFlowSocket()

cur_angles = erobot.get_angles()
print(cur_angles)
```

## Overall status

### get_angles
- **Prototype**:`get_angles()`
- **Description**: get angls of all joints
- **Return value**:`list`A list of floating point values representing the angles of all joints
- **Example**:If the call was successful and will receive **get_angles:[0.174058, 0.520382, -0.07874, 0.092855, 0.0, 0.030356]**，If any error occurs, the InvalidAngles() function will be returned（defined as : **[-1.0, -2.0, -3.0, -4.0, -1.0, -1.0]**）

### set_angles
- **Prototype**:`set_angles(angles_array, speed)`
- **Description**:Send all angles to all the joints of the robot arm
- **Parameters**:
  - `angles_array`
  - `joint1_angle`: Joint 1 angle ，range -180.00 ~ 180.00
  - `joint2_angle`: Joint 2 angle ，range -270.00 ~ 90.00
  - `joint3_angle`: Joint 3 angle ，range -150.00 ~ 150.00
  - `joint4_angle`: Joint 4 angle ，range -260.00 ~ 80.00
  - `joint5_angle`: Joint 5 angle ，range -168.00 ~ 168.00
  - `joint6_angle`: Joint 6 angle ，range -174.00 ~ 174.00
  - `speed`: Motion speed，range 0 ~ 2000
- **Example**:**set_angles(10.0,11.0,12.2,12.3,11.1,16.0,500) **，If the call was successful and will receive **set_angles:[ok]** ，If any error occurs, will receive **set_angles:error_message**

### set_angle
- **Prototype**:`set_angle(joint, angle, speed)`

- **Description**:Send angle to the specified joint

- **Parameters**:
  
  - `joint`: J1 / J2 / J3 / J4 / J5 / J6
  
  - `angle`: Refer to the parameter description of set_angles() for details about the angle range of each joint
  
    `speed`: Motion speed, range 0 ~ 2000
  
  - **Example：** **set_angle(1,50.5,500)**，If the call was successful and will receive **set_angle：[ok]**，If any error occurs, will receive **set_angle:error_message**

### get_coords
- **Prototype**:`get_coords()`
- **Description**:get current coordinates of robot
- **Return value：** `list`A list of coordinates and poses of length 6, sequentially `[x, y, z, rx, ry, rz]`
- **Example：** If the call was successful and will receive **get_coords :[0.174058, 0.520382, -0.07874, 0.092855, 0.0, 0.030356]**，If any error occurs, the InvalidAngles() function will be returned（defined as : **[-1.0, -2.0, -3.0, -4.0, -1.0, -1.0]**）
### set_coords
- **Prototype**:`set_coords(coords_array, speed)`
- **Description**:Send the overall coordinates and attitude, so that the head of the robot moves from the original point to the specified point
- **Parameters：**
  - `axis_x_coord`: x coordinate
  - `axis_y_coord`: y coordinate
  - `axis_z_coord`: z coordinate
  - `axis_rx_coord`: rx coordinate
  - `axis_ry_coord`: ry coordinate
  - `axis_rz_coord`: rz coordinate
  - `speed`: Motion speed , range 0 ~ 2000
- **Example：** **set_coords(10.0,11.0,12.2,12.3,11.1,16.0,500)**，If the call was successful and will receive **set_coords:[ok]**，If any error occurs, will receive **set_coords:error_message**
### set_coord
- **Prototype**:`set_coord(axis, coord, speed)`
- **Description**: Send a single coordinate value to the robot for movement
- **Parameters**：
  - `axis`: x / y / z / rx / ry / rz
  - `coord`: coordinate value
  - `speed`: Motion speed , range 0-2000
- **Example：** **set_coord(x,50.5,500)** ，If the call was successful and will receive **set_coords:[ok]**。If any error occurs, will receive **set_coords:error_message**
### jog_coord
- **Prototype**:`jog_coord(axis, dirc, speed)`
- **Description**:Control the robot to move continuously according to the specified axis direction
- **Parameters**：
  - `axis`: Representing different directions, the available parameters are x / y / z / rx / ry / rz
  - `dirc`: It mainly controls the direction of movement of the robot arm, -1 - negative direction ，0 - stop，1 - positive direction
  - `speed`: speed range 0 ~ 2000
- **Example：** **jog_coord(‘x’,1, 500)** ，If the call was successful and will receive **jog_coord:[ok]**，If any error occurs, will receive **jog_coord:error_message**
### jog_stop
- **Prototype**:`jog_stop(axis)`
- **Description**:Control the robot to stop moving in the direction of the specified coordinate axis
- **Parameters**：
  - `axis`: Representing different directions, the available parameters are x / y / z / rx / ry / rz
### jog_angle
- **Prototype**:`jog_angle(joint, dirc, speed)`
- **Description**: Control the robot to keep moving at the specified Angle
- **Parameters**：
  - `joint`: Represents the joint of the robot, and the available parameters are J1 / J2 / J3 / J4 / J5 / J6
  - `dirc`: It mainly controls the direction of movement of the robot arm，-1 - negative direction ，0 - stop，1 - positive direction
  - `speed`: speed range 0 ~ 2000
- **Example：** **jog_angle(1, 1, 500)** ，If the call was successful and will receive **jog_angle:[ok]**, If any error occurs, will receive **jog_angle:error_message**
### task_stop
- **Prototype**:`task_stop()`
- **Description**:Stop current task
### wait
- **Prototype**:`wait(seconds)`
- **Description**:Set the robot wait time(s)
### power_on

- **Prototype**: `power_on()`
- **Description**:power on the robot
- **Example：** **power_on()**，If the call was successful and will receive **power_on:[ok]**，If any error occurs, will receive **power_on:error_message**

### power_off

- **Prototype**: `power_off()`
- **Description**: power off the robot
- **Example：** **power_off()**，If the call was successful and will receive **power_off:[ok]**，If any error occurs, will receive **power_off:error_message**

### get_speed
- **Prototype**:`get_speed()`
- **Description**:Gets the running speed in mm/s
- **Example：** **get_speed()** ，If the call was successful and will receive **get_speed: speed**，If any error occurs, will receive **get_speed:error_message**
### state_check
- **Prototype**:`state_check()`
- **Description**:Get the robot state
- **Example：** **state_check()** ，If the robot is in normal condition, it will receive **state_check:1**，If the robot is not in normal condition, it will receive **state_check:0**，If any error occurs, will receive **state_check:error_message**
### check_running
- **Prototype**:`check_running()`
- **Description**:check if the robot is running
- **Example：** **check_running()**，If the robot is running, it will receive **check_running:1**，If the robot is not running, it will receive **check_running:0**，If any error occurs, will receive **check_running:error_message**
### set_torque_limit
- **Prototype**:`set_torque_limit(axis, torque)`
- **Description**:Set the torque limit for the robot
- **Parameters**：
  - `axis`: x / y / z / rx / ry / rz
  - `torque`: range 0 ~ 2
- **Example：** **set_torque_limit(x,10.0)** ，If the call was successful and will receive **set_torque_limit:[ok]**，If any error occurs, will receive **set_torque_limit:error_message**
### set_payload
- **Prototype**:`set_payload(payload)`
- **Description**:set the payload of the robot
- **Parameters**：
  - `payload`: range 0.0 ~ 2.0
- **Example：** **set_payload(1.0)**，If the call was successful and will receive **set_payload:[ok]**，If any error occurs, will receive **set_payload:error_message**
### set_acceleration
- **Prototype**:`set_acceleration(acc)`
- **Description**: set the acceleration of the robot
- **Parameters**：
  - `acc` : Acceleration, which must be an integer in mm/s
- **Example：** **set_acceleration(50)**，If the call was successful and will receive **set_acceleration:[ok]**，If any error occurs, will receive **set_acceleration:error_message**
### wati_command_done
- **Prototype**:`wait_command_done()`
- **Description**:Wait until the last command completes
- **Example：** **wait_command_done()**，If the call was successful and will receive **set_payload:0**，If any error occurs, will receive **set_payload:error_message**
### pause_program
- **Prototype**:`pause_program()`
- **Description**:Pause a running program
- **Example：** **pause_program()** ，If the call was successful and will receive **pause_program:[ok]**，If any error occurs, will receive **pause_program:error_message**
### resume_program
- **Prototype**:`resume_program()`
- **Description**:Resume the paused program
-  **Example：** **resume_program()**，If the call was successful and will receive **resume_program:[ok]**，If any error occurs, will receive **resume_program:error_message**
### state_on

**Tip: Before using this command, run power_on() to power on the robot; otherwise, the system cannot be started**

- **Prototype**:`state_on()`
- **Description**:enable the system
- **Example：** **state_on()**，If the call was successful and will receive **state_on:[ok]** ，If any error occurs, will receive **state_on:error_message**
### state_off
- **Prototype**:`state_off()`
- **Description**:Shut down the system, but the robot is still powered on
- **Example：** **state_off()**，If the call was successful and will receive **state_off:[ok]**，If any error occurs, will receive **state_off:error_message**
### set_digital_out
- **Prototype**:`set_digital_out(pin_number, signal)`
- **Description**:set the signal of digital out pin
- **Parameters**：
  - `pin_number`: 0 to 5 indicates the base electrical port OUT 1 to 6. 16 ~ 17 Corresponding to the end electrical interface of the robot OUT 1-2 (refer to the Pro600 manual for reference)
  - `signal` : 1 - High, 0 - low
- **Example：** **set_digital_out(1,1)** If the call was successful and will receive **set_digital_out:[ok]**，If any error occurs, will receive **set_digital_out:error_message**

### set_init_gripper
- **Prototype**:`set_init_gripper()`
- **Description**:Gripper initialization
- **Example：** **set_init_gripper()**，If the call was successful and will receive **set_init_gripper:[ok]**，If any error occurs, will receive **set_init_gripper:error_message**
### set_open_gripper

- **Prototype**:`set_open_gripper()`
- **Description**:Open the gripper
- **Example：** **set_open_gripper()**，If the call was successful and will receive **set_open_gripper:[ok]**，If any error occurs, will receive **set_open_gripper:error_message**

### set_close_gripper

- **Prototype**:`set_close_gripper()`
- **Description**:Close the gripper
- **Example：** **set_close_gripper()**，If the call was successful and will receive **set_close_gripper:[ok]**，If any error occurs, will receive **set_close_gripper:error_message**

