## Importing Libraries
from PySide2 import QtCore
from PySide2 import QtWidgets
import hou
import json
import os
import random

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

        self.textInputScatterObj = QtWidgets.QLineEdit(self)
        self.textInputScatterObj.setMinimumWidth(175)
        hbox1.addWidget(self.textInputScatterObj)
        self.vBox.addLayout(hbox1)

##------------------------------------Scatter Plane---------------------------------------------##
        
        hbox2 = QtWidgets.QHBoxLayout()

        self.labelScatterObjLocation = QtWidgets.QLabel('where is the object located, eg. /obj/geo1/', self)
        self.labelScatterObjLocation.setMinimumWidth(175)
        hbox2.addWidget(self.labelScatterObjLocation)

        self.textInputScatterObjLocation = QtWidgets.QLineEdit(self)
        self.textInputScatterObjLocation.setMinimumWidth(175)
        hbox2.addWidget(self.textInputScatterObjLocation) 
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

        
##--------------------------------Translation upper bounds-----------------------------------##
        hbox5 = QtWidgets.QHBoxLayout()
        self.labelTranslationLower = QtWidgets.QLabel('what are the lower bounds of translation you would like? (x,y,z)')
        self.labelTranslationLower.setMinimumWidth(175)
        hbox5.addWidget(self.labelTranslationLower)

        self.textInputTranslationLowerX = QtWidgets.QLineEdit(self)
        self.textInputTranslationLowerX.setMinimumWidth(50)
        self.textInputTranslationLowerX.textChanged.connect(self.textHasChangedTranslationLowerX)

        self.textInputTranslationLowerY = QtWidgets.QLineEdit(self)
        self.textInputTranslationLowerY.setMinimumWidth(50)
        self.textInputTranslationLowerY.textChanged.connect(self.textHasChangedTranslationLowerY)

        self.textInputTranslationLowerZ = QtWidgets.QLineEdit(self)
        self.textInputTranslationLowerZ.setMinimumWidth(50)
        self.textInputTranslationLowerZ.textChanged.connect(self.textHasChangedTranslationLowerZ)

        hbox5.addWidget(self.textInputTranslationLowerX)
        hbox5.addWidget(self.textInputTranslationLowerY)
        hbox5.addWidget(self.textInputTranslationLowerZ)
        self.vBox.addLayout(hbox5)
##--------------------------------Translation lower bounds-----------------------------------##
        hbox6 = QtWidgets.QHBoxLayout()
        self.labelTranslationUpper = QtWidgets.QLabel('what are the upper bounds of translation you would like? (x,y,z)')
        self.labelTranslationUpper.setMinimumWidth(175)
        hbox6.addWidget(self.labelTranslationUpper)

        self.textInputTranslationUpperX = QtWidgets.QLineEdit(self)
        self.textInputTranslationUpperX.setMinimumWidth(50)
        self.textInputTranslationUpperX.textChanged.connect(self.textHasChangedTranslationUpperX)
        
        self.textInputTranslationUpperY = QtWidgets.QLineEdit(self)
        self.textInputTranslationUpperY.setMinimumWidth(50)
        self.textInputTranslationLowerY.textChanged.connect(self.textHasChangedTranslationUpperY)

        self.textInputTranslationUpperZ = QtWidgets.QLineEdit(self)
        self.textInputTranslationUpperZ.setMinimumWidth(50)
        self.textInputTranslationUpperZ.textChanged.connect(self.textHasChangedTranslationUpperZ)

        hbox6.addWidget(self.textInputTranslationUpperX)
        hbox6.addWidget(self.textInputTranslationUpperY)
        hbox6.addWidget(self.textInputTranslationUpperZ)
        self.vBox.addLayout(hbox6)

##-------------------------------------SnapToGround-------------------------------------##
        '''
        hbox5 = QtWidgets.QHBoxLayout()
        
        self.cbSnapToGround = QtWidgets.QCheckBox("SnapToGround", self)
        self.cbSnapToGround.setMinimumWidth(150)
        self.cbSnapToGround.stateChanged.connect(self.stateHasChangedSnapToGround)
        
        hbox5.addWidget(self.cbSnapToGround)
        self.vBox.addLayout(hbox5)
        '''
##---------------------------------------------Button----------------------------------##

        hbox7 = QtWidgets.QHBoxLayout()
        self.button = QtWidgets.QPushButton('Build', self)
        self.button.clicked.connect(self.buildProject)
        hbox7.addWidget(self.button)
        self.vBox.addLayout(hbox7)

      

##--------------------------------------------------------------------------------------##
        self.setLayout(self.vBox)


    def textHasChangedScatterObj(self):
        scatterObjText = self.textInputScatterObj.text()
    
    def textHasChangedScatterObjLocation(self):
        scatterObjText = self.extInputScatterObjLocation.text()

    def textHasChangedScatterNum(self):
        scatterNum = self.textInputScatterNum.text()

    def textHasChangedRotationX(self):
        rotationX = self.textInputRotationX.text()

    def textHasChangedRotationY(self):
        rotationY = self.textInputRotationY.text()

    def textHasChangedRotationZ(self):
        rotationZ = self.textInputRotationZ.text()
        
    def textHasChangedTranslationLowerX(self):
        translationLowerX = self.textInputTranslationLowerX

    def textHasChangedTranslationLowerY(self):
        translationLowerY = self.textInputTranslationLowerY

    def textHasChangedTranslationLowerZ(self):
        translationLowerZ = self.textInputTranslationLowerZ

    def textHasChangedTranslationUpperX(self):
        translationUpperX = self.textInputTranslationUpperX

    def textHasChangedTranslationUpperY(self):
        translationUpperY = self.textInputTranslationUpperY

    def textHasChangedTranslationUpperZ(self):
        translationUpperZ = self.textInputTranslationUpperZ


    def buildProject(self):


        scatterObjText = self.textInputScatterObj.text()
        scatterObjLocation = self.textInputScatterObjLocation.text()
        scatterNumText = self.textInputScatterNum.text()
        rotationXText = self.textInputRotationX.text()
        rotationYText = self.textInputRotationY.text()
        rotationZText = self.textInputRotationZ.text()
        translationLowerX = self.textInputTranslationLowerX.text()
        translationLowerY = self.textInputTranslationLowerY.text()
        translationLowerZ = self.textInputTranslationLowerZ.text()
        translationUpperX = self.textInputTranslationUpperX.text()
        translationUpperY = self.textInputTranslationUpperY.text()
        translationUpperZ = self.textInputTranslationUpperZ.text()

       # print(scatterObjText)

        scatterObj = hou.node(f'{scatterObjLocation}{scatterObjText}')
        obj = hou.node("/obj")
        myGeo = hou.node(f'{scatterObjLocation}')
        timesRan = 0
        subnet = myGeo.createNode("subnet", 'scatter')
        mySub = hou.node(f'{scatterObjLocation}scatter/')
        merge = mySub.createNode("merge", 'merge1')
        subnet.setInput(0, scatterObj)

        for i in range(int(scatterNumText)):
                timesRan+=1
                randomRotationX = random.randint (0, (int(rotationXText)))
                randomRotationY = random.randint (0, (int(rotationYText)))
                randomRotationZ = random.randint (0, (int(rotationZText)))
                randomTranslationX = random.randint ((int(translationLowerX)), (int(translationUpperX)))
                randomTranslationY = random.randint ((int(translationLowerY)), (int(translationUpperY)))
                randomTranslationZ = random.randint ((int(translationLowerZ)), (int(translationUpperZ)))
                
                copy = mySub.createNode("copyxform", f'copy{timesRan}')
                copyNum = copy.parm('ncy')
                copyTranslateX = copy.parm('tx')
                copyTranslateY = copy.parm('ty')
                copyTranslateZ = copy.parm('tz')
                copyRotateX = copy.parm('rx')
                copyRotateY = copy.parm('ry')
                copyRotateZ = copy.parm('rz')
                copyNum.set(2)
                copyTranslateX.set(randomTranslationX)
                copyTranslateY.set(randomTranslationY)
                copyTranslateZ.set(randomTranslationZ)
                copyRotateX.set(randomRotationX)
                copyRotateY.set(randomRotationY)
                copyRotateZ.set(randomRotationZ)
                copy.setInput(0, mySub.indirectInputs()[0])
                merge.setInput(timesRan, copy)

                print(scatterObj)
                print(randomRotationX, randomRotationY, randomRotationZ)
                print(randomTranslationX, randomTranslationY, randomTranslationZ)
                print(timesRan)



dialog = Scatter()
dialog.show()
