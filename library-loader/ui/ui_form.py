# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(660, 335)
        Widget.setMinimumSize(QSize(660, 335))
        Widget.setMaximumSize(QSize(660, 335))
        self.settings_label = QLabel(Widget)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(10, 20, 639, 29))
        font = QFont()
        font.setPointSize(15)
        self.settings_label.setFont(font)
        self.settings_label.setTextFormat(Qt.PlainText)
        self.horizontalLayoutWidget_2 = QWidget(Widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 100, 641, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.ecad_choice_label = QLabel(self.horizontalLayoutWidget_2)
        self.ecad_choice_label.setObjectName(u"ecad_choice_label")

        self.horizontalLayout_2.addWidget(self.ecad_choice_label)

        self.horizontalSpacer_4 = QSpacerItem(38, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.ecad_choice_box = QComboBox(self.horizontalLayoutWidget_2)
        self.ecad_choice_box.addItem("")
        self.ecad_choice_box.addItem("")
        self.ecad_choice_box.setObjectName(u"ecad_choice_box")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ecad_choice_box.sizePolicy().hasHeightForWidth())
        self.ecad_choice_box.setSizePolicy(sizePolicy)
        self.ecad_choice_box.setMinimumSize(QSize(50, 0))
        self.ecad_choice_box.setMaximumSize(QSize(800, 16777215))
        self.ecad_choice_box.setInsertPolicy(QComboBox.NoInsert)

        self.horizontalLayout_2.addWidget(self.ecad_choice_box)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 641, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.watchpath_label = QLabel(self.horizontalLayoutWidget)
        self.watchpath_label.setObjectName(u"watchpath_label")

        self.horizontalLayout.addWidget(self.watchpath_label)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.folder_select_path = QLineEdit(self.horizontalLayoutWidget)
        self.folder_select_path.setObjectName(u"folder_select_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.folder_select_path.sizePolicy().hasHeightForWidth())
        self.folder_select_path.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.folder_select_path)

        self.file_select_button = QPushButton(self.horizontalLayoutWidget)
        self.file_select_button.setObjectName(u"file_select_button")

        self.horizontalLayout.addWidget(self.file_select_button)

        self.ecad_history = QTextEdit(Widget)
        self.ecad_history.setObjectName(u"ecad_history")
        self.ecad_history.setGeometry(QRect(10, 180, 641, 141))
        self.ecad_history.setReadOnly(True)
        self.history_label = QLabel(Widget)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setGeometry(QRect(10, 157, 81, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.history_label.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.settings_label.setText(QCoreApplication.translate("Widget", u"Settings", None))
        self.ecad_choice_label.setText(QCoreApplication.translate("Widget", u"Preferred ECAD Tool", None))
        self.ecad_choice_box.setItemText(0, QCoreApplication.translate("Widget", u"KiCAD", None))
        self.ecad_choice_box.setItemText(1, QCoreApplication.translate("Widget", u"Eagle", None))

        self.pushButton.setText(QCoreApplication.translate("Widget", u"Settings", None))
        self.watchpath_label.setText(QCoreApplication.translate("Widget", u"Downloads", None))
        self.file_select_button.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.ecad_history.setPlaceholderText("")
        self.history_label.setText(QCoreApplication.translate("Widget", u"History", None))
    # retranslateUi

