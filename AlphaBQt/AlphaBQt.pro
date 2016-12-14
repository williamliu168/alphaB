#-------------------------------------------------
#
# Project created by QtCreator 2016-11-24T15:36:39
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = AlphaBQt
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    Widgets/TreeMapWidget.cpp \
    Widgets/Chart.cpp

HEADERS  += mainwindow.h \
    fundamentaldata.h \
    fundamentaldatapoint.h \
    treemapwidget.h \
    Widgets/TreeMapWidget.h \
    Widgets/Chart.h

FORMS    += mainwindow.ui

CONFIG += console
