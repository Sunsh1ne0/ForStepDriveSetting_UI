# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import math
import numpy as np

import struct
from random import random

import serial
from PySide6.QtCore import QTimer
from ui_ForDrive import Ui_ForDrive
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import pyqtgraph as pg

# arduinoNano = serial.Serial('COM17', 9600)

class MyArrowItem(pg.ArrowItem):
    def paint(self, p, *args):
        p.translate(-self.boundingRect().center())
        pg.ArrowItem.paint(self, p, *args)

class InputMessage:
    def __init__(self, port, line):
        self.total_size = None
        self.message_converted = None
        self.message = None
        self.line_format = line
        self.port = port
        self.convert_data = self.line_format.split()
        self.data_number = len(self.convert_data)

    def get_msg_size(self):
        self.total_size = struct.calcsize('=' + self.line_format)

    def receive(self):
        temp = self.port.readline(1)
        temporary = 0

        if temp == b'!':
            if self.port.in_waiting >= self.total_size:
                self.message = struct.unpack('=' + self.line_format, self.port.read(self.total_size))
                self.message_converted = list(self.message)
                for counter in range(self.data_number - 1):
                    try:
                        temporary += ord(self.message_converted[counter])
                    except TypeError:
                        temporary += self.message_converted[counter]
                if round(self.message_converted[self.data_number - 1], 3) != round(temporary, 3):
                    self.message_converted = None
                self.port.reset_input_buffer()

            else:
                self.port.reset_input_buffer()


# inpMSGNano = InputMessage(arduinoNano, "f f")
# inpMSGNano = InputMessage(arduinoNano, "f f")


class ForDrive(QWidget, Ui_ForDrive):
    def __init__(self, parent=None):
        super().__init__()
        temporary = self.palette()
        temporary.setColor(self.backgroundRole(), QColor(130,130,150))
        self.setPalette(temporary)
        self.start_pos = True
        self.dGain = 0.0
        self.iGain = 0.0
        self.pGain = 1.0
        self.position = 0.0
        self.number = 0

        self.trajectory_length = 20
        self.V = 0.3
        self.speed = 0
        self.angle = 0
        self.crc = self.speed + self.angle
        self.allowSend = False
        self.WindX = 0
        self.WindY = 0
        self.WindXMax = 0.8
        self.WindYMax = 0.8
        self.traj_x = [0, self.trajectory_length, self.trajectory_length, 0, 0]
        self.traj_y = [0, 0, self.trajectory_length, self.trajectory_length, 0]
        self.theta = 0
        self.theta_delta = 0
        self.theta_old = 1000
        self.num_point = 1
        self.multiplier = 0
        self.multiplier2 = 0

        self.setupUi(self)
        self.widget.addLegend()
        self.widget.setBackground('w')
        styles = {'color': 'r', 'font-size': '20px'}
        self.x = [0, 1]
        self.y = [0, 0]
        self.y1 = [0]
        self.widget.setLabel('left', 'Y, km', **styles)
        self.widget.setLabel('bottom', 'X, km', **styles)
        self.data_line = self.widget.plot(self.x, self.y)
        self.data_line1 = self.widget.plot(self.x, self.y)
        self.data_line2 = MyArrowItem(angle=0, tipAngle=0, headLen=0, tailLen=0, tailWidth=0, pen={'color': 'w', 'width': 3},  brush='r')
        self.data_line2.setPos(self.trajectory_length / 2, self.trajectory_length / 2)
        self.widget.addItem(self.data_line2)
        self.data_line3 = MyArrowItem(angle=0, tipAngle=0, headLen=0, tailLen=0, tailWidth=0, pen={'color': 'w', 'width': 3},  brush='blue')
        self.widget.addItem(self.data_line3)
        self.widget.showGrid(x=True, y=True)
        self.timer = QTimer()
        self.timer.setInterval(60)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.update_plot_data()
        self.graphReset.clicked.connect(self.ResetGraph)
        self.positionUpdate.clicked.connect(self.SendPosition)
        self.sendPID.clicked.connect(self.UpdateParams)
        self.center

        self.UpdateParams()
        

    def __del__(self):
        self.timer = None

    def update_plot_data(self):
        package = struct.pack('=' + "c f f f", b'@', self.speed, self.position, round(self.crc, 5))
        # print(package)

        # inpMSGNano.port.reset_input_buffer()
        # inpMSGNano.get_msg_size()
        # inpMSGNano.receive()
        # print(inpMSGNano.message_converted)
        # print(inpMSGNano.message_converted)
        # for byteCounter in range(1, 5):

        # if self.allowSend == True:
        #     arduinoNano.write(package)
            # None
        
        slowing = 0
        # num_point = 1

        dead_zone = 1
        
        
        match self.num_point:
            case 1:
                x_aim, y_aim = self.trajectory_length, 0
                self.multiplier = 1
                self.multiplier2 = 0
            case 2: 
                x_aim, y_aim = self.trajectory_length, self.trajectory_length
                self.multiplier = 1
                self.multiplier2 = 1
            case 3:
                x_aim, y_aim = 0, self.trajectory_length
                self.multiplier = 0
                self.multiplier2 = 0
            case 4:
                x_aim, y_aim = 0,0 
                self.multiplier = 0
                self.multiplier2 = 1
            case 5:
                x_aim, y_aim = self.trajectory_length, 0
                self.multiplier = 1
                self.multiplier2 = 0

        X_,Y_ ,self.theta_old= self.NN_Moving( self.x[-2],self.y[-2],20,self.x[-1],self.y[-1],20,x_aim,y_aim,self.num_point,slowing,self.theta_old,self.WindX,self.WindY)

        # print(self.num_point)
        if len(self.x) > 400:
            self.x = self.x[1:]  # Remove the first y element.
            self.y = self.y[1:]  # Remove the first
            self.y1 = self.y1[1:]
        self.x.append(X_)  # Add a new value 1 higher than the last.
        self.y.append(Y_)
        # print(self.y)
        if self.checkBoxStopGraph.checkState() == Qt.Unchecked:
            self.CurrentValues.setText(f"Theta: {self.theta_delta}")
            self.data_line.setData(self.x, self.y, pen=(2, 3))  # Update the data.
            self.data_line1.setData(self.traj_x, self.traj_y, pen=(4, 2))
            self.data_line3.setPos(self.x[-1], self.y[-1])
            self.data_line3.setStyle(angle=np.degrees(self.theta - self.multiplier2 * 2 * self.theta - np.pi * self.multiplier), tipAngle = 60, headLen = 16, tailLen = 0, tailWidth = 2, pen = {'color': 'w', 'width': 1},  brush='b')
            if np.sqrt(self.WindX ** 2 + self.WindY ** 2) != 0:
                self.data_line2.setStyle(angle=np.degrees(np.pi - np.arctan2(self.WindY, self.WindX)), tipAngle = 60, headLen = 16, tailLen = 16, tailWidth = 2, pen = {'color': 'w', 'width': 1},  brush='r')
            else:
                self.data_line2.setStyle(angle=np.degrees(np.pi - np.arctan2(self.WindY, self.WindX)), tipAngle = 60, headLen = 0, tailLen = 0, tailWidth = 0, pen = {'color': 'w', 'width': 1},  brush='r')
        if abs(X_ - x_aim) ** 2 + (Y_ - y_aim) ** 2 <= dead_zone ** 2:
            self.num_point = self.num_point + 1
            self.theta_old = 1000
            
            if self.num_point >= 6:
                self.num_point = 2        
        
    
    
    def NN_Moving(self, x_old, y_old, z_old, x, y, z, x_aim, y_aim, num_point, slowing, thetad_old, WindX, WindY): 
        if (num_point == 1):
            inito = x_old + 1, y_old
            s = 0
            j = 1
            l = 1
        elif (num_point == 2):
            inito = x_old + 1, y_old
            s = 0
            j = 1
            l = 1
        elif (num_point == 3):
            inito = x_old - 1, y_old
            s = np.pi 
            j = -1
            l = 1
        elif (num_point == 4):
            inito = x_old - 1, y_old
            s = np.pi
            j = -1
            l = -1
        else:
            inito = x_old + 1, y_old
            s = 0
            j = 1
            l = 1
            
        old = x_old, y_old
        aim = x_aim, y_aim
        current = x, y
        current_vec = self.make_vector(old, current)
        target_vec = self.make_vector(old, aim)
        ref = self.make_vector(old,inito)
        
    
        theta = self.get_angle(ref,current_vec)
        

        if (np.abs(thetad_old < 0.000001)):         
                theta_tar = theta
        else :
            theta_tar = self.get_angle(ref,target_vec)      
            
        if ((num_point == 1) | (num_point == 3)):
            if (target_vec[1] >= 0):         
                if (np.abs(theta) > np.abs(theta_tar)):
                    theta = theta - np.abs(theta_tar - theta) / 4
                else:
                    theta = theta + np.abs(theta_tar - theta) / 4 
            else:
                theta = theta - np.abs(theta_tar + theta) / 3

        elif (num_point == 2):
            if (current_vec[1] >= 0):
                if (np.abs(theta) > np.abs(theta_tar)):
                    theta = theta - np.abs(theta_tar - theta) / 4
                else:
                    theta = theta + np.abs(theta_tar - theta) / 4  
            else:
                theta = theta + np.abs(theta_tar + theta) / 4
                
        elif (num_point == 4):
            if (current_vec[1] < 0):        
                if (np.abs(theta) > np.abs(theta_tar)):
                    theta = theta - np.abs(theta_tar - theta) / 4
                else:
                    theta = theta + np.abs(theta_tar - theta) / 4   
            else:
                theta = theta - np.abs(theta_tar + theta) / 4

        else:
            if (target_vec[1] >= 0):
                l = 1
                if (np.abs(theta) > np.abs(theta_tar)):
                    theta = theta - np.abs(theta_tar - theta) / 4
                else:
                    theta = theta + np.abs(theta_tar - theta) / 4    
                theta = np.abs(theta)
            else:
                theta = theta - np.abs(theta_tar + theta) / 4
                l = -1
                theta = np.abs(theta)
            
        Vx = self.V * np.cos(s + j * theta) + WindX / 100
        Vy = self.V * np.sin(l * theta) + WindY / 100

        X_new = x + Vx
        Y_new = y + Vy    

        self.theta = theta
        self.theta_delta = np.degrees(theta_tar - theta)

        return(X_new, Y_new, np.abs(theta_tar - theta))

    def make_vector(self, p1, p2):
        """вектор из точек"""
        return p2[0] - p1[0], p2[1] - p1[1]

    def get_len(self, v):
        """длина вектора"""
        return math.sqrt(v[0] ** 2 + v[1] ** 2)

    def get_angle(self, v1, v2):
        """угол между двумя векторами"""
        return math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (self.get_len(v1) * self.get_len(v2)))


    def ResetGraph(self):
        self.x = [self.x[-2], self.x[-1]]  # 100 time points
        self.y = [self.y[-2], self.y[-1]]
        # self.y1 = [self.y1[-1]]
        self.timer.stop()
        self.timer.start()

    def center(self):
        qr = self.frameGeometry()
        cp = QWidget.QScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def SendPosition(self):
        self.allowSend = True if (self.allowSend == False) else False
        self.CurrentValues.setText(f"Target speed: {self.speed}, target angle: {self.angle},\n sending: {self.allowSend},\n WindX: {self.WindX}, WindY: {self.WindY}")
        
       
        # crc = self.speed + self.position
        # package = struct.pack('=' + "c f f f", b'@', self.speed, self.position, round(crc, 5))
        # arduinoNano.write(package)

    def UpdateParams(self):
        self.position = self.doubleSpinBox_4.value()
        self.speed = self.doubleSpinBox_3.value()
        self.WindX = self.doubleSpinBox.value()
        self.WindY = self.doubleSpinBox_2.value()
        

        self.CurrentValues.setText(f"Target speed: {self.speed}, target angle: {self.angle},\n sending: {self.allowSend},\n WindX: {self.WindX}, WindY: {self.WindY}")
    
    # def Moving(self,x_old,y_old,z_old,x,y,z,x_aim, y_aim, num_point,slowing, thetad_old, WindX, WindY, delta):  
         
    #     #print(x,y)
    #     if (num_point == 1):
    #         f = -1
    #     else:
    #         f= 1
    #     # theta_d = math.acos( ((x_aim-x_old)**2 + (y_aim-y_old)**2 + (x-x_old)**2 + (y-y_old)**2 - (x_aim-x_old)**2-(y_aim-y_old)**2)/(2*np.sqrt((x-x_old)**2+ (y-y_old)**2)*np.sqrt((x_aim-x_old)**2+ (y_aim-y_old)**2)))
        
        
    #     old = x_old, y_old
    #     aim = x_aim, y_aim
    #     current = x, y
    #     inito = x_old + 1, y_old
        
    #     current_vec = self.make_vector(old, current)
    #     target_vec = self.make_vector(old, aim)
    #     projection_vec = self.make_vector(old, inito)

    #     theta = self.get_angle(projection_vec,current_vec)  
        

    #     # theta = theta + f * theta_d / 1.1

    #     if(num_point==4):        
    #         theta = -theta
    #     if(num_point==5):        
    #         theta = -theta
    #     if (np.abs(thetad_old<0.000001)):         
    #         theta_d = 0
    #     else :
    #         theta_d = self.get_angle(current_vec, target_vec) 
    #     # theta = theta + f * (theta_d + math.atan2(WindY,WindX + 0.00001))/10
    #     # theta = theta + f * ((theta_d)/10 + delta/5)
    #     theta = theta + f * ((theta_d)/self.multiplier)
    #     self.multiplier += 0.5
    #     if self.multiplier >= 10:
    #         self.multiplier = 10
    #     print(f"theta: {np.degrees(theta)}, theta_d: {np.degrees(theta_d)},delta :{delta}") 
    #     V_max = self.V
    #     if abs(V_max) > 1:
    #         V_max = 1 * V_max / abs(V_max)
        
    #     # self.V = V_max + np.sqrt(WindX ** 2 + WindY ** 2) * math.atan2(WindY, (WindX + 0.01))
            
    #     # self.V = V_max + np.sqrt(WindX ** 2 + WindY ** 2) * math.atan2(WindY, (WindX + 0.01)) / 100
    #     self.V = V_max
    #     # print(V)                
    #     # X_new = x + (self.V*np.cos(theta) + WindX / 100)
    #     # Y_new = y + self.V*np.sin(theta) + WindY / 100
    #     Vx = self.V*np.cos(theta) + WindX
    #     Vy = self.V*np.sin(theta) + WindY
    #     angle_v = math.atan2(Vy,Vx+0.0001)
    #     print(Vx, Vy)

    #     delta = theta - angle_v
    #     if (np.abs(delta) >=2*np.pi-0.5):
    #         if ((delta)>0):

    #             delta = delta - 2*np.pi
    #         else  :
    #             delta = 2*np.pi + delta  
    #     X_new = x + Vx
    #     Y_new = y + Vy
    #     #angle_v = math.atan2(Vy,Vx+0.0001)

    #     return(X_new,Y_new,theta_d,delta)