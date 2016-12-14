#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "Widgets/TreeMapWidget.h"
#include "Widgets/Chart.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;

    ClientWidgets::TreeMapWidget m_treeMapWidget;
    ClientWidgets::Chart    m_chart;

};

#endif // MAINWINDOW_H
