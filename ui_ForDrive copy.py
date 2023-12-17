# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGridLayout,
                               QGroupBox, QHBoxLayout, QLabel, QLayout,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget


class Ui_ForDrive(object):
    def setupUi(self, ForDrive):
        if not ForDrive.objectName():
            ForDrive.setObjectName(u"ForDrive")
        ForDrive.resize(1024, 720)
        self.gridLayout = QGridLayout(ForDrive)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(ForDrive)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setStyleSheet(u"font: 700 11pt \"Segoe Print\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setStyleSheet(u"font: 700 9pt \"Segoe Script\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)
        self.doubleSpinBox.setMinimumSize(QSize(100, 0))
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(20.000000000000000)
        self.doubleSpinBox.setSingleStep(0.001000000000000)
        self.doubleSpinBox.setValue(1.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(u"font: 700 9pt \"Segoe Script\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_2.setMinimumSize(QSize(100, 0))
        self.doubleSpinBox_2.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_2.setDecimals(5)
        self.doubleSpinBox_2.setMaximum(20.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.000010000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe Script\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_3.setMinimumSize(QSize(100, 0))
        self.doubleSpinBox_3.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_3.setDecimals(3)
        self.doubleSpinBox_3.setMaximum(20.000000000000000)
        self.doubleSpinBox_3.setSingleStep(0.001000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 9pt \"Segoe Script\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_4.setMinimumSize(QSize(100, 0))
        self.doubleSpinBox_4.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_4.setMaximum(150.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.100000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBox_4, 0, Qt.AlignHCenter)

        self.CurrentValues = QLabel(self.groupBox_3)
        self.CurrentValues.setObjectName(u"CurrentValues")
        self.CurrentValues.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.CurrentValues)

        self.sendPID = QPushButton(self.groupBox_3)
        self.sendPID.setObjectName(u"sendPID")
        self.sendPID.setCheckable(False)

        self.verticalLayout.addWidget(self.sendPID)

        self.positionUpdate = QPushButton(self.groupBox_3)
        self.positionUpdate.setObjectName(u"positionUpdate")
        self.positionUpdate.setCheckable(False)

        self.verticalLayout.addWidget(self.positionUpdate)

        self.graphReset = QPushButton(self.groupBox_3)
        self.graphReset.setObjectName(u"graphReset")
        self.graphReset.setCheckable(False)

        self.verticalLayout.addWidget(self.graphReset)

        self.checkBoxStopGraph = QCheckBox(self.groupBox_3)
        self.checkBoxStopGraph.setObjectName(u"checkBoxStopGraph")

        self.verticalLayout.addWidget(self.checkBoxStopGraph)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAutoFillBackground(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(20)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setStyleSheet(u"font: 9pt \"Segoe Script\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.widget = PlotWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)

        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(ForDrive)

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/graph.png"),
                       QIcon.Selected, QIcon.On)
        self.setWindowIcon(icon)

        self.setWindowTitle('PID Setting')

        QMetaObject.connectSlotsByName(ForDrive)

    # setupUi

    def retranslateUi(self, ForDrive):
        ForDrive.setWindowTitle(QCoreApplication.translate("ForDrive", u"ForDrive", None))
        # if QT_CONFIG(accessibility)
        self.groupBox.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle("")
        self.groupBox_3.setTitle("")
        self.label_5.setText(QCoreApplication.translate("ForDrive",
                                                        u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041f\u0418\u0414",
                                                        None))
        self.label.setText(QCoreApplication.translate("ForDrive",
                                                      u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u041f",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("ForDrive",
                                                        u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0418",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("ForDrive",
                                                        u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0414",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("ForDrive",
                                                        u"\u041a\u043e\u043d\u0435\u0447\u043d\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435",
                                                        None))
        self.CurrentValues.setText("")
        self.sendPID.setText(
            QCoreApplication.translate("ForDrive", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c PID", None))
        self.positionUpdate.setText(QCoreApplication.translate("ForDrive",
                                                               u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435",
                                                               None))
        self.graphReset.setText(QCoreApplication.translate("ForDrive",
                                                           u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a",
                                                           None))
        self.checkBoxStopGraph.setText(QCoreApplication.translate("ForDrive",
                                                                  u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0443",
                                                                  None))
        self.groupBox_2.setTitle("")
        self.label_6.setText(QCoreApplication.translate("ForDrive",
                                                        u"\u041f\u0435\u0440\u0435\u0445\u043e\u0434\u043d\u043e\u0439 \u043f\u0440\u043e\u0446\u0435\u0441\u0441",
                                                        None))
    # retranslateUi
