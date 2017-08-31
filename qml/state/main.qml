import QtQuick 1.0

Rectangle {
	id: page
	width: 500; height: 200
	color: "lightgray"

	Text {
		id: helloText
		text: "Hello world"
		y : 30
		anchors.horizontalCenter: page.horizontalCenter
		font.pointSize: 24; font.bold: true

		MouseArea { id: mouseArea; anchors.fill: parent }

		states: State {
			name: "down"; when: mouseArea.pressed == true
			PropertyChanges { target: helloText; y: 160; rotation: 180; color: "red" }

		}

		transitions: Transition {
			from: ""; to: "down"; reversible: true
			ParallelAnimation {
				NumberAnimation { properties: "y, rotation"; duration: 500; easing.type: Easing.InOutQuad }
				ColorAnimation { duration: 500 }
			}
		}
	}
}
