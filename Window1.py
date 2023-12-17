# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

import struct
from random import random

import serial
from PySide6.QtCore import QTimer
from ui_ForDrive import Ui_ForDrive
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

# arduinoNano = serial.Serial('COM11', 115200)


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


# inpMSGNano = InputMessage(arduinoNano, "f f f f f f")
# inpMSGNano = InputMessage(arduinoNano, "f f f f f f")


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
        self.setupUi(self)
        self.widget.addLegend()
        self.widget.setBackground('w')
        styles = {'color': 'r', 'font-size': '20px'}
        self.x = [0]
        self.y = [0]
        self.y1 = [0]
        self.widget.setLabel('left', 'Current, A', **styles)
        self.widget.setLabel('bottom', 'Seconds (s)', **styles)
        self.data_line = self.widget.plot(self.x, self.y)
        self.data_line1 = self.widget.plot(self.x, self.y)
        self.widget.showGrid(x=True, y=True)
        self.timer = QTimer()
        self.timer.setInterval(40)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.update_plot_data()
        self.graphReset.clicked.connect(self.ResetGraph)
        self.positionUpdate.clicked.connect(self.SendPosition)
        self.sendPID.clicked.connect(self.SendPID)
        self.center
        self.SendPID()
        

    def __del__(self):
        self.timer = None

    def update_plot_data(self):
        None
        # inpMSGNano.port.reset_input_buffer()
        # inpMSGNano.get_msg_size()
        # inpMSGNano.receive()
        # print(inpMSGNano.message_converted)
        # for byteCounter in range(1, 5):
        #     if len(self.x) > 400:
        #         if self.start_pos:
        #             self.x = self.x[1:]  # Remove the first y element.
        #             self.y = self.y[1:]  # Remove the first
        #             self.y1 = self.y1[1:]
        #             self.start_pos = False
        #         break
        #     self.x.append((self.x[-1] + 0.04))  # Add a new value 1 higher than the last.
        #     if self.checkBoxStopGraph.checkState() == Qt.Unchecked:
        #         while len(self.x) != len(self.y):
        #             while len(self.x) != len(self.y1):
        #                 try:
        #                     None
        #                     # self.y1.append((inpMSGNano.message_converted[byteCounter] - 330) * 5 / 1024 / 0.185)
        #                 except:
        #                     self.y1.append(self.y1[-1])
        #             try:
        #                 # self.y.append((inpMSGNano.message_converted[byteCounter] - 330) * 5 / 1024 / 0.185)
        #                 None
        #             except:
        #                 self.y.append(self.y[-1])
        #         self.data_line.setData(self.x, self.y,  pen=(2, 3))  # Update the data.
        #         self.data_line1.setData(self.x, self.y1,  pen=(4, 2))

    def ResetGraph(self):
        self.x = [0]  # 100 time points
        self.y = [self.y[-1]]
        self.y1 = [self.y1[-1]]
        self.timer.stop()
        self.timer.start()

    def center(self):
        qr = self.frameGeometry()
        cp = QWidget.QScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def SendPosition(self):
        self.position = self.doubleSpinBox_4.value()
        crc = self.pGain + self.iGain + self.dGain + self.position
        package = struct.pack('=' + "c f f f f f", b'@', self.position, self.pGain, self.iGain, self.dGain, round(crc, 5))
        # arduinoNano.write(package)

    def SendPID(self):
        self.pGain = self.doubleSpinBox.value()
        self.iGain = self.doubleSpinBox_2.value()
        self.dGain = self.doubleSpinBox_3.value()

        self.CurrentValues.setText("P: " + str(round(self.pGain, 3)) + " I: " + str(round(self.iGain, 5)) + " D: " + str(round(self.dGain, 3)))
