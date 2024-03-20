#include <QDialog>
#include <QFileDialog>
#include <QDebug>
#include "kicadsettings.h"
#include "ui_kicadsettings.h"

KicadSettings::KicadSettings(
        QWidget *parent,
        QString curr_library_directory)
    : QDialog(parent)
    , ui(new Ui::KicadSettings)
{
    ui->setupUi(this);

    connect(this, &QDialog::finished, this, [this]() {
        emit dataAvailable(libraryDirectory);
    });

    qDebug() << "Current Library Directory: " << curr_library_directory;
    libraryDirectory = curr_library_directory;
    ui->directory_path->setText(libraryDirectory);
}

KicadSettings::~KicadSettings()
{
    delete ui;
}


void KicadSettings::on_kicad_settings_box_accepted()
{
    this->done(0);
}


void KicadSettings::on_kicad_settings_box_rejected()
{
    // this->done(-1);
    this->done(0);
}

void KicadSettings::on_browse_path_button_clicked()
{
    QString folder_path = QFileDialog::getExistingDirectory(this, "Open Folder", "/home/dheemanth/");
    ui->directory_path->setText(folder_path);
    if (libraryDirectory != folder_path) {
        libraryDirectory = folder_path;
    } else {
        qDebug("Selected folder is same.");
    }
}

