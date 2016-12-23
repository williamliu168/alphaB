#include "Chart.h"

#include <QPainter>

namespace ClientWidgets
{

Chart::Chart(QWidget *parent)
    : QWidget(parent)
{
    setBackgroundRole(QPalette::Base);
    setAutoFillBackground(true);
}

void Chart::setPen(const QPen &in_pen)
{
    this->m_pen = in_pen;
    update();
}

void Chart::setBrush(const QBrush &in_brush)
{
    this->m_brush = in_brush;
    update();
}

void Chart::paintEvent(QPaintEvent * /* event */)
{
    static const QPoint points[4] = {
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    };

    QPainter painter(this);
    painter.setPen(m_pen);
    painter.setBrush(m_brush);

    painter.drawPolyline(points, 4);
    painter.drawPolygon(points, 4);

    painter.setPen(palette().dark().color());
    painter.setBrush(Qt::NoBrush);
    painter.drawRect(QRect(0, 0, width() - 1, height() - 1));
}

}
