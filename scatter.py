## Importing Libraries
from PySide2 import QtCore
from PySide2 import QtWidgets
import hou
import json
import os

class Scatter(QtWidgets.QWidget):
    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle('Scatter')
        self.vBox = QtWidgets.QVBoxLayout()

##------------------------------------Scatter Object--------------------------------------------##

        hbox1 = QtWidgets.QHBoxLayout()

        self.labelScatterObj = QtWidgets.QLabel('Which object do you want to scatter?', self)
        self.labelScatterObj.setMinimumWidth(175)
        hbox1.addWidget(self.labelScatterObj)

##                 ADD THE DROPDOWN OPTIONS!!!!!!!
        self.ddlScatterObj = QtWidgets.QComboBox(self)
        self.ddlScatterObj.setMinimumWidth(175)
        self.ddlScatterObj.addItem("")
        hbox1.addWidget(self.ddlScatterObj)
        self.vBox.addLayout(hbox1)

##------------------------------------Scatter Plane---------------------------------------------##

        hbox2 = QtWidgets.QHBoxLayout()

        self.labelScatterPlane = QtWidgets.QLabel('Select the plane you want to scatter on', self)
        self.labelScatterPlane.setMinimumWidth(175)
        hbox2.addWidget(self.labelScatterPlane)

##               ADD THE DROPDOWN OPTIONS!!!!!!
        self.ddlScatterPlane = QtWidgets.QComboBox(self)
        self.ddlScatterPlane.setMinimumWidth(175)
        self.ddlScatterPlane.addItem("")
        hbox2.addWidget(self.ddlScatterPlane)
        self.vBox.addLayout(hbox2)

##-------------------------------------Scatter Num-------------------------------------------------##

        hbox3 = QtWidgets.QHBoxLayout()
        self.labelScatterNum = QtWidgets.QLabel('How many of this object would you like to scatter', self)
        self.labelScatterNum.setMinimumWidth(175)
        hbox3.addWidget(self.labelScatterNum)

        self.textInputScatterNum = QtWidgets.QLineEdit(self)
        self.textInputScatterNum.setMinimumWidth(175)
        self.textInputScatterNum.textChanged.connect(self.textHasChangedScatterNum)
        hbox3.addWidget(self.textInputScatterNum)
        self.vBox.addLayout(hbox3)

##----------------------------------------Rotation-----------------------------------------------------##

        hbox4 = QtWidgets.QHBoxLayout()
        self.labelXRotation = QtWidgets.QLabel('How much rotation would you like (x,y,z)')
        self.labelXRotation.setMinimumWidth(175)
        hbox4.addWidget(self.labelXRotation)

        self.textInputRotationX = QtWidgets.QLineEdit(self)
        self.textInputRotationX.setMinimumWidth(50)
        self.textInputRotationX.textChanged.connect(self.textHasChangedRotationX)
        
        self.textInputRotationY = QtWidgets.QLineEdit(self)
        self.textInputRotationY.setMinimumWidth(50)
        self.textInputRotationY.textChanged.connect(self.textHasChangedRotationY)

        self.textInputRotationZ = QtWidgets.QLineEdit(self)
        self.textInputRotationZ.setMinimumWidth(50)
        self.textInputRotationZ.textChanged.connect(self.textHasChangedRotationZ)

        hbox4.addWidget(self.textInputRotationX)
        hbox4.addWidget(self.textInputRotationY)
        hbox4.addWidget(self.textInputRotationZ)
        self.vBox.addLayout(hbox4)

##-------------------------------------SnapToGround-------------------------------------##

        hbox5 = QtWidgets.QHboxLayout()
        
        self.cbSnapToGround = QtWidgets.QCheckBox("SnapToGround", self)
        self.cbSnapToGround.setMinimumWidth(150)
        self.cbSnapToGround.stateChanged.connect(self.stateHasChangedSnapToGround)
        
        hbox5.addWidget(self.cbSnapToGround)
        self.vBox.addLayout(hbox5)

##---------------------------------------------Button----------------------------------##

        hbox6 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton("Build", self)
        hbox6.addWidget(self.button)
        self.vBox.addLayout(hbox6)

##--------------------------------------------------------------------------------------##
        self.setLayout(self.vBox)


    def textHasChangedScatterNum(self):
        scatterNum = self.textInputScatterNum.text()

    def textHasChangedRotationX(self):
        rotationX = self.textInputRotationX.text()

    def textHasChangedRotationY(self):
        rotationY = self.textInputRotationY.text()

    def textHasChangedRotationZ(self):
        rotationZ = self.textInputRotationZ.text()

    def stateHasChangedSnapToGround(self):
        snapToGround = self.cbSnapToGround()

dialog = Scatter()
dialog.show()