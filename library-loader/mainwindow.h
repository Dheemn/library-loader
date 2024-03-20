#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "kicadsettings.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

typedef struct
{
    QString ecad_software;
    QString watch_path;
    QString libraryDirectory;
} AppSettings;

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void writeLog(QString log_string);

private slots:
    void on_file_select_button_clicked();

    void on_ecad_choice_box_currentTextChanged(const QString &arg1);

    void on_settingsButton_clicked();

    void dataAvailable(const QString s);

private:
    Ui::MainWindow *ui;

    AppSettings setting;
};
#endif // MAINWINDOW_H
