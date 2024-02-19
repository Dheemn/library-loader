#include "kicadsettings.h"
#include "ui_kicadsettings.h"

KicadSettings::KicadSettings(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::KicadSettings)
{
    ui->setupUi(this);
}

KicadSettings::~KicadSettings()
{
    delete ui;
}


void KicadSettings::on_kicad_settings_box_accepted()
{
    if (sV.hasPropertiesChanged != false) {
    }
    this->done(QDialog::Accepted);
}


void KicadSettings::on_kicad_settings_box_rejected()
{
    this->done(QDialog::Rejected);
}
