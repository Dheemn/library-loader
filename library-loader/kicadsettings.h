#ifndef KICADSETTINGS_H
#define KICADSETTINGS_H

#include <QDialog>

namespace Ui {
class KicadSettings;
}

typedef struct {
    bool hasPropertiesChanged = false;
} SettingsValue;

class KicadSettings : public QDialog
{
    Q_OBJECT

public:
    explicit KicadSettings(QWidget *parent = nullptr);
    ~KicadSettings();

private slots:
    void on_kicad_settings_box_accepted();

    void on_kicad_settings_box_rejected();

private:
    Ui::KicadSettings *ui;

    SettingsValue sV;
};

#endif // KICADSETTINGS_H
