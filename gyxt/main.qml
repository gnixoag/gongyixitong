import QtQuick 2.3
import QtQuick.Window 2.0
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import QtQuick.Controls.Material 2.3
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    width: 800
    height: 600
    visible: true



    title: qsTr("工艺系统")
    Login {
        id: login
    }
    About {
        id: aboutwindow
    }

    //文件菜单命令
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
    Action {
        text: qsTr("工艺设计")
        id: gysj
    }

    Action {
        text: qsTr("输出BOM")
        id: scbom
    }


    //系统配置命令
    Action {
        text: qsTr("模块配置")
        id: mkpz
    }
    Action {
        text: qsTr("用户管理")
        id: yhgl
    }
    Action {
        text: qsTr("用户组管理")
        id: yhzgl
    }

    //帮助菜单命令
    Action {
        id: about
        text: qsTr("关于")
        onTriggered: aboutwindow.show()
    }

    menuBar: MenuBar {
        Menu {
            title: qsTr("工艺BOM(&G)")
            MenuItem {
                action: newbom
            }
            MenuItem {
                action: shbom
            }
            MenuItem {
                action: cxbom
            }

            MenuSeparator {
            }
            MenuItem {
                action: gysj
            }

            MenuSeparator {
            }
            MenuItem {
                action: scbom
            }
        }
        Menu {
            title: qsTr("系统配置")
            MenuItem {
                action: mkpz
            }
            MenuItem {
                action: yhgl
            }
            MenuItem {
                action: yhzgl
            }
        }
        Menu {
            title: qsTr("帮助")
            MenuItem{action: about}
        }
    }

    toolBar: ToolBar {

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

    statusBar: RowLayout {
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

    TableView {
        anchors.fill: parent
        Button {
            text: "dfasdf"
        }
    }
}
