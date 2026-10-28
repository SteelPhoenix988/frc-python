#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import rev


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        # 1. Initialize the SPARK MAX on CAN ID 1 as a Brushless motor (e.g., NEO)
        self.left_back_motor = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushed)
        self.left_front_motor = rev.SparkMax(10, rev.SparkLowLevel.MotorType.kBrushed)
        self.right_back_motor = rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushed)
        self.right_front_motor = rev.SparkMax(6, rev.SparkLowLevel.MotorType.kBrushed)

        # self.joy = wpilib.XboxController(0)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""

        # self.left_back_motor.set(-0.1)
        self.left_front_motor.set(0.1)
        # self.right_back_motor.set(0.1)
        # self.right_front_motor.set(0.1)


    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wpilib.run(MyRobot)