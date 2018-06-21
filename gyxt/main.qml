import QtQuick 2.0
import QtQuick.Window 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3
import QtQuick.Controls 1.4 as C
import QtQuick.Controls.Material 2.3

ApplicationWindow {
    width: 800
    height: 600
    visible: true
    Material.theme: Material.Light
    Material.accent: Material.Purple
    Material.background: Material.Dark

    title: qsTr("工艺系统")
    Login {
        id: login
    }
    About {
        id: aboutwindow
    }
    menuBar: MenuBar {
        Menu {
            title: qsTr("工艺BOM(&G)")
            Action {
                text: qsTr("新建BOM")
                id: newbom
                onTriggered: {
                    login.show()
                    console.debug("打开登入窗口")
                }
            }
            Action {
                text: qsTr("审核BOM")
                id: shbom
            }
            Action {
                text: qsTr("查询BOM")
                id: cxbom
            }
            MenuSeparator {
            }

            Action {
                text: qsTr("工艺设计")
            }
            MenuSeparator {
            }
            Action {
                text: qsTr("输出BOM")
            }
        }
        Menu {
            title: qsTr("系统配置")
            Action {
                text: qsTr("模块配置")
            }
            Action {
                text: qsTr("用户管理")
            }
            Action {
                text: qsTr("用户组管理")
            }
        }
        Menu {
            title: qsTr("帮助")
            Action {
                id: about
                text: qsTr("关于")
                onTriggered: aboutwindow.show()
            }
        }
    }

    header: ToolBar {

        ColorAnimation {
            from: "white"
            to: "black"
            duration: 200
        }
        RowLayout {
            ToolButton {
                action: newbom
            }
            ToolButton {
                action: shbom
            }
            ToolButton {
                action: cxbom
            }
            ToolButton {
                action: about
            }
        }
    }

    footer: RowLayout {
        Label {
            text: qsTr("状态栏，提示：")
        }
    }
    ListModel {
        id: libraryModel
        ListElement {
            name: "Bill Smith"
            number: "555 3264"
        }
        ListElement {
            name: "John Brown"
            number: "555 8426"
        }
        ListElement {
            name: "Sam Wise"
            number: "555 0473"
        }
    }
    ListView {
        width: 180
        height: 200

        model: libraryModel
        delegate: Text {
            text: name + ": " + number
        }
    }

    C.TableView {
        anchors.fill: parent
        Button {
            text: "dfasdf"
        }
    }
}
