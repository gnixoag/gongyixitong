import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4

Window {
    id: lg
    title: qsTr("面向MES系统的CAPP-用户登陆")
    flags: Qt.Dialog
    minimumHeight: 200
    minimumWidth: 400
    maximumHeight: 200
    maximumWidth: 400

    ColumnLayout {
        anchors.fill: parent
        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            Layout.topMargin: 10
            Label {
                text: qsTr("用户名:")
            }
            Item {
                width: password.width
                height: password.height
                ComboBox {
                    anchors.fill: parent
                    editable: true

                    MouseArea{
                    anchors.fill: parent
                    onDoubleClicked: { sele  }
                    }

                    model: ListModel {
                        id: model
                        ListElement {
                            text: ""
                        }
                        ListElement {
                            text: "admin"
                        }
                        ListElement {
                            text: "GaoXing"
                        }
                        ListElement {
                            text: "Linux"
                        }
                    }
                    onAccepted: {
                        if (find(editText) === -1)
                            model.append({
                                             text: editText
                                         })
                    }
                }
            }
        }
        RowLayout {
            id: b
            Layout.alignment: Qt.AlignHCenter
            Label {
                text: qsTr("密  码:")
            }
            TextField {
                id: password
                placeholderText: qsTr("请输入密码")
                echoMode: TextInput.Password
            }
        }

        RowLayout {
            Layout.alignment: Qt.AlignHCenter
            Layout.bottomMargin: 10
            spacing: 40
            Button {
                height: 10
                text: qsTr("登  陆")
            }
            Button {
                height: 10
                text: qsTr("取  消")
                onClicked: {
                    console.debug("关闭登入窗口")
                    close()
                }
            }
        }
    }
}
