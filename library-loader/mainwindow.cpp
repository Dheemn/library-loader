#include <QFileDialog>
#include <QDebug>
#include "kicadsettings.h"
#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setting.ecad_software = ui->ecad_choice_box->currentText();
    setting.watch_path = "/home/dheemanth/Components";
    setting.libraryDirectory = "";
    // Settings sV;

    ui->folder_select_path->setText(setting.watch_path);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::writeLog(QString log_string)
{
    QString pre_log = ui->ecad_history->toPlainText();
    if (pre_log == "")
    {
        ui->ecad_history->setText(log_string);
    } else {
        ui->ecad_history->setText(pre_log + "\n" + log_string);
    }
}

void MainWindow::on_file_select_button_clicked()
{
    QString folder_path = QFileDialog::getExistingDirectory(this, "Open Folder", "/home/dheemanth/");
    ui->folder_select_path->setText(folder_path);
    setting.watch_path = folder_path;
    writeLog("Component watch path set to " + folder_path);
}


void MainWindow::on_ecad_choice_box_currentTextChanged(const QString &arg1)
{
    setting.ecad_software = arg1;
    writeLog("ECAD software changed to " + arg1);
}


void MainWindow::on_settingsButton_clicked()
{
    if (setting.ecad_software == "KiCad") {
        auto ks = new KicadSettings(this, setting.libraryDirectory);
        // int msg = ks->exec();
        ks->show();

        connect(ks, &KicadSettings::dataAvailable, this, &MainWindow::dataAvailable);
        // qDebug("Message: %d", msg);
        // if ( msg == 1 ) {
        //     writeLog("KiCad settings updated");
        // }
    }
}

void MainWindow::dataAvailable(const QString s)
{
    qDebug() << "Library directory: " << s;
    if ( s != setting.libraryDirectory) {
        setting.libraryDirectory = s;
        writeLog("Settings updated");
    } else {
        writeLog("Nothing to update");
    }
}

