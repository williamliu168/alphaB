#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    system("pause");

    std::ifstream infile("C:\\Users\\wiliu\\Desktop\\AlphaB\\AlphaBQt\\grand.csv");
    if (!infile) {
        std::cout<<"Fail to find file"<<std::endl;
    }
    std::string line;
    while (std::getline(infile, line))
    {
        break;
        std::istringstream ss(line);
        std::string token;
        int i = 0;
        while(std::getline(ss, token, '|')) {
            if (i==1)
            {
                std::cout << token << '\n';
            }
            i++;
        }
    }

    // return a.exec();
    return 1;
}
