import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4

Window {
    title: qsTr("关于")
    flags: Qt.Dialog
    minimumHeight: 300
    minimumWidth: 400
    maximumHeight: 300
    maximumWidth: 400

    Label{
    text: qsTr("面向MES系统的CAPP")
    font: font.pixelSize=50

    }

}
