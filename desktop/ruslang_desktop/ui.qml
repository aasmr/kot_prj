import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    title: "Разметка русских слов"
    width: 640
    height: 480

    Component
    {
        id:startup_v
        Rectangle
        {
            anchors.fill: parent
            Text {
                id: enterid_req
                x: 225
                text: qsTr("Введите id или ник из ВК")
                anchors.top: parent.top
                font.pixelSize: 32
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 20
                color: "#2d95f7"
            }
            Text {
                id: enterid_req_1
                text: qsTr("или хоть что-нибудь, что позволит мне, Лёхе Смирнову, идентифицировать вас как знакомого")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: enterid_req.bottom
                font.pixelSize: 18
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                anchors.rightMargin: 20
                anchors.leftMargin: 20
                anchors.topMargin: 10
                color: "#777777"
            }
            TextField {
                id: user_id_ent
                placeholderText: "вот сюды"
                height: 50
                visible: true
                color: "#000000"
                text: qsTr("")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: enterid_req_1.bottom
                font.pixelSize: 18
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                clip: false
                anchors.rightMargin: 20
                anchors.leftMargin: 20
                font.weight: Font.ExtraLight
                anchors.topMargin: 20

            }
            Text {
                id: enterid_war
                text: qsTr("Эту комбинацию букв кто-то занял, поменяй пожалуйста.\nЕсли возникли проблемы со входом, свяжись со мной в vk или в tg")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: user_id_ent.bottom
                font.pixelSize: 14
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                wrapMode: Text.WordWrap
                anchors.rightMargin: 20
                anchors.leftMargin: 20
                anchors.topMargin: 10
                color: "red"
                visible: false
            }

            Button {
                id: button_start
                x: 170
                y: 409
                text: qsTr("СТАРТУЕМ")
                anchors.bottom: parent.bottom
                checkable: false
                checked: false
                anchors.bottomMargin: 30
                anchors.horizontalCenter: parent.horizontalCenter
                font.pointSize: 18
                width: 300
                flat: true
                background: Rectangle {
                    implicitWidth: 300
                    implicitHeight: 40
                    opacity: enabled ? 1 : 0.3
                    color: button_start.down ? "#17a81a" : "#21be2b"
                    border.width: 1
                    radius: 10
                }
            }

            CheckDelegate {
                id: training_flag
                x: 232
                y: 158
                text: qsTr("Хочу пройти обучение")
                anchors.bottom: button_start.top
                wheelEnabled: true
                font.pointSize: 12
                anchors.bottomMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter
                indicator: Rectangle {
                    implicitWidth: 26
                    implicitHeight: 26
                    x: training_flag.width - width - training_flag.rightPadding
                    y: training_flag.topPadding + training_flag.availableHeight / 2 - height / 2
                    radius: 3
                    color: "transparent"
                    border.color: training_flag.down ? "#2d95f7" : "#21be2b"

                    Rectangle {
                        width: 14
                        height: 14
                        x: 6
                        y: 6
                        radius: 2
                        color: training_flag.down ? "#2d95f7" : "#21be2b"
                        visible: training_flag.checked
                    }
                }

            }
        }
    }

    Component
    {
        id:workspace_v
        Rectangle
        {
            anchors.fill: parent

            Text {
                id: word
                x: 225
                text: qsTr("word")
                anchors.top: parent.top
                font.pixelSize: 32
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 20
            }

            TextField {
                id: word_edit
                y: 81
                height: 50
                visible: true
                color: "#000000"
                text: qsTr("")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: word.bottom
                font.pixelSize: 18
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                placeholderText: "введите исправление"
                clip: false
                anchors.rightMargin: 20
                anchors.leftMargin: 20
                font.weight: Font.ExtraLight
                anchors.topMargin: 20

            }

            Switch {
                id: obscene_sw
                text: qsTr("Мат")
                anchors.left: sleng_sw.left
                anchors.top: word_edit.bottom
                anchors.leftMargin: 0
                topPadding: 0
                font.bold: true
                font.pointSize: 12
                autoExclusive: false
                checked: false
                display: AbstractButton.TextOnly
                anchors.topMargin: 30

                indicator:
                    Rectangle {
                    implicitWidth: 48
                    implicitHeight: 26
                    x: obscene_sw.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 13
                    border.color:obscene_sw.checked ? "#f82d2d" :"#сссссс"
                    Rectangle {
                        x: obscene_sw.checked ? parent.width - width : 0
                        width: 26
                        height: 26
                        radius: 13
                        color: obscene_sw.down ? "#cccccc" : "#ffffff"
                        border.color: obscene_sw.checked ? (obscene_sw.down ? "#17a81a" : "#f82d2d") : "#999999"
                        layer.enabled: false
                    }
                }
            }
            Switch {
                id: sleng_sw
                x: 22
                text: qsTr("Слэнг")
                anchors.top: obscene_sw.bottom
                topPadding: 0
                font.bold: true
                font.pointSize: 12
                autoExclusive: false
                checked: false
                display: AbstractButton.TextOnly
                anchors.topMargin: 10
                anchors.horizontalCenter: parent.horizontalCenter

                indicator:
                    Rectangle {
                    implicitWidth: 48
                    implicitHeight: 26
                    x: sleng_sw.leftPadding
                    y: parent.height / 2 - height / 2
                    radius: 13
                    border.color:sleng_sw.checked ? "#2d95f7" :"#сссссс"
                    Rectangle {
                        x: sleng_sw.checked ? parent.width - width : 0
                        width: 26
                        height: 26
                        radius: 13
                        color: sleng_sw.down ? "#cccccc" : "#ffffff"
                        border.color: sleng_sw.checked ? (sleng_sw.down ? "#17a81a" : "#2d95f7") : "#999999"
                        layer.enabled: false
                    }
                }
            }
        }
    }

    Component
    {
        id:training_v
        Rectangle
        {
            color: 'red'
        }
    }
    Loader
    {
        anchors.fill: parent
        id:loader
        sourceComponent: startup_v
    }

}





/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}D{i:5}D{i:8}D{i:22}D{i:18;invisible:true}
}
##^##*/
