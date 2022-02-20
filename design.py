# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 437)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widthInput = QLineEdit(self.centralwidget)
        self.widthInput.setObjectName(u"widthInput")

        self.gridLayout.addWidget(self.widthInput, 2, 1, 1, 1)

        self.heightInput = QLineEdit(self.centralwidget)
        self.heightInput.setObjectName(u"heightInput")

        self.gridLayout.addWidget(self.heightInput, 2, 3, 1, 1)

        self.resizeButton = QPushButton(self.centralwidget)
        self.resizeButton.setObjectName(u"resizeButton")

        self.gridLayout.addWidget(self.resizeButton, 2, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 547, 324))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imgLabel = QLabel(self.scrollAreaWidgetContents)
        self.imgLabel.setObjectName(u"imgLabel")

        self.gridLayout_2.addWidget(self.imgLabel, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)

        self.chooseFileBtn = QPushButton(self.centralwidget)
        self.chooseFileBtn.setObjectName(u"chooseFileBtn")

        self.gridLayout.addWidget(self.chooseFileBtn, 1, 4, 1, 1)

        self.openFileInput = QLineEdit(self.centralwidget)
        self.openFileInput.setObjectName(u"openFileInput")

        self.gridLayout.addWidget(self.openFileInput, 1, 0, 1, 4)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 3, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Resize Image", None))
        self.resizeButton.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.imgLabel.setText("")
        self.chooseFileBtn.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

