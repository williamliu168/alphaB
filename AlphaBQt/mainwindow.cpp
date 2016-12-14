#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QGridLayout>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QGridLayout *mainLayout = new QGridLayout;
    mainLayout->setColumnStretch(0, 1);
    mainLayout->setColumnStretch(3, 2);
    mainLayout->addWidget(m_chart, 1, 1);

    // m_treeMapWidget.m_prototypeNumber = 1;
    // m_treeMapWidget.Initialize();
    // m_treeMapWidget.show();

}

MainWindow::~MainWindow()
{
    delete ui;
}
