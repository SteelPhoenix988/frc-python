#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive

from phoenix6 import CANBus, configs, controls, hardware, signals


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        # Motor control from
        # https://github.com/CrossTheRoadElec/Phoenix6-Examples/blob/main/python/ArcadeDrive/robot.py
        self.rio = CANBus("rio")
        self.front_left_motor = hardware.TalonFX(21, self.rio)
        self.rear_left_motor = hardware.TalonFX(31, self.rio)
        self.front_right_motor = hardware.TalonFX(11, self.rio)
        self.rear_right_motor = hardware.TalonFX(41, self.rio)

        cfg = configs.TalonFXConfiguration()
        cfg.motor_output.inverted = configs.config_groups.InvertedValue.COUNTER_CLOCKWISE_POSITIVE
        self.front_left_motor.configurator.apply(cfg)

        cfg.motor_output.inverted = configs.config_groups.InvertedValue.CLOCKWISE_POSITIVE
        self.front_right_motor.configurator.apply(cfg)

        # Configure the rear motors to follow the front motors
        follow_left_request = controls.Follower(21, signals.MotorAlignmentValue.ALIGNED)
        self.rear_left_motor.set_control(follow_left_request)

        follow_right_request = controls.Follower(11, signals.MotorAlignmentValue.ALIGNED)
        self.rear_right_motor.set_control(follow_right_request)

        # Keep a reference to the DutyCycleOut control request to update periodically
        self.left_out = controls.DutyCycleOut(0)
        self.right_out = controls.DutyCycleOut(0)

        self.joy = wpilib.XboxController(0)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        # self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""

        throttle = self.joy.getLeftY() * -1
        wheel = self.joy.getRightX() * 1

        # And set the DutyCycleOut to the motor controllers
        self.front_left_motor.set_control(self.left_out.with_output(throttle + wheel))
        self.front_right_motor.set_control(self.right_out.with_output(throttle - wheel))

    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wpilib.run(MyRobot)