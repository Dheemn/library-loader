#ifndef KICADSETTINGS_H
#define KICADSETTINGS_H

#include <QDialog>

namespace Ui {
class KicadSettings;
}

// typedef struct {
//     bool hasPropertiesChanged = false;
//     QString libraryDirectory;
// } Settings;

class KicadSettings : public QDialog
{
    Q_OBJECT

public:
    explicit KicadSettings(QWidget *parent = nullptr, QString curr_library_directory = NULL);
    ~KicadSettings();

signals:
    void dataAvailable(const QString s);

private slots:
    void on_kicad_settings_box_accepted();

    void on_kicad_settings_box_rejected();

    void on_browse_path_button_clicked();

private:
    Ui::KicadSettings *ui;

    QString libraryDirectory;
};

#endif // KICADSETTINGS_H
