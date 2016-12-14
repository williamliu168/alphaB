#ifndef CLIENTWIDGETS_CHART_H
#define CLIENTWIDGETS_CHART_H

#include <QObject>
#include <QBrush>
#include <QPen>
#include <QWidget>

namespace ClientWidgets
{

class Chart : public QWidget
{
    Q_OBJECT

public:
    Chart( QWidget *parent = 0);

public slots:
    void setPen(const QPen &pen);
    void setBrush(const QBrush &brush);

protected:
    void paintEvent(QPaintEvent *event) Q_DECL_OVERRIDE;

protected:
    void DrawLine();

private:
    QPen    m_pen;
    QBrush  m_brush;
};

}

#endif // CLIENTWIDGETS_CHART_H
