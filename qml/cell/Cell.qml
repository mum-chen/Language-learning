import QtQuick 1.0

Item {
	id: container
	property alias cellColor: rectangel.color
	signal clicked(color cellColor)

	width: 40; height:25

	Rectangle {
		id: rectangel
		border.color: "white"
		anchors.fill: parent
	}

	MouseArea {
		anchors.fill: parent
		onClicked: container.clicked(container.cellColor)
	}
}
