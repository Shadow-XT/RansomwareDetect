# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesPdPfKk.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.horizontalLayout = QHBoxLayout(MainPages)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1_home = QWidget()
        self.page_1_home.setObjectName(u"page_1_home")
        self.page_1_home.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1_home)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1_home)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1_home)
        self.page_2_init_file = QWidget()
        self.page_2_init_file.setObjectName(u"page_2_init_file")
        self.verticalLayout_3 = QVBoxLayout(self.page_2_init_file)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.page_2_init_file)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hlayout2_title = QVBoxLayout()
        self.hlayout2_title.setObjectName(u"hlayout2_title")
        self.label_set_file = QLabel(self.widget)
        self.label_set_file.setObjectName(u"label_set_file")
        font = QFont()
        font.setPointSize(20)
        self.label_set_file.setFont(font)

        self.hlayout2_title.addWidget(self.label_set_file, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.hlayout2_title)

        self.hlayout2_table = QHBoxLayout()
        self.hlayout2_table.setObjectName(u"hlayout2_table")

        self.verticalLayout_2.addLayout(self.hlayout2_table)

        self.hlayout2_button = QHBoxLayout()
        self.hlayout2_button.setObjectName(u"hlayout2_button")

        self.verticalLayout_2.addLayout(self.hlayout2_button)


        self.verticalLayout_3.addWidget(self.widget)

        self.pages.addWidget(self.page_2_init_file)
        self.page_3_monitor = QWidget()
        self.page_3_monitor.setObjectName(u"page_3_monitor")
        self.verticalLayout_5 = QVBoxLayout(self.page_3_monitor)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.page_3_monitor)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.hlayout3_title = QHBoxLayout()
        self.hlayout3_title.setObjectName(u"hlayout3_title")
        self.label_run = QLabel(self.widget_2)
        self.label_run.setObjectName(u"label_run")
        self.label_run.setFont(font)

        self.hlayout3_title.addWidget(self.label_run, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.hlayout3_title)

        self.hlayout3_table = QHBoxLayout()
        self.hlayout3_table.setObjectName(u"hlayout3_table")

        self.verticalLayout_4.addLayout(self.hlayout3_table)

        self.hlayout3_process_button = QHBoxLayout()
        self.hlayout3_process_button.setObjectName(u"hlayout3_process_button")
        self.vlayout3_progress = QVBoxLayout()
        self.vlayout3_progress.setObjectName(u"vlayout3_progress")

        self.hlayout3_process_button.addLayout(self.vlayout3_progress)

        self.glayout3_button = QGridLayout()
        self.glayout3_button.setSpacing(2)
        self.glayout3_button.setObjectName(u"glayout3_button")

        self.hlayout3_process_button.addLayout(self.glayout3_button)

        self.hlayout3_process_button.setStretch(0, 1)
        self.hlayout3_process_button.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.hlayout3_process_button)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.pages.addWidget(self.page_3_monitor)
        self.page_4_database = QWidget()
        self.page_4_database.setObjectName(u"page_4_database")
        self.pages.addWidget(self.page_4_database)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 233, 265))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font1)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.label_set_file.setText(QCoreApplication.translate("MainPages", u"\u8bf1\u9975\u6587\u4ef6\u914d\u7f6e", None))
        self.label_run.setText(QCoreApplication.translate("MainPages", u"\u6267\u884c\u68c0\u6d4b", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

