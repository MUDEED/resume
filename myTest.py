import sys
from PySide2.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QTreeWidget,
    QTreeWidgetItem,
)


class MyTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["Items"])
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QTreeWidget.DragDrop)
        self.setDragDropOverwriteMode(True)

        # Create some initial items
        for i in range(5):
            item = QTreeWidgetItem(self)
            item.setText(0, f"Item {i}")

    def dropEvent(self, event):
        super().dropEvent(event)
        self.clearSelection()  # Clear selection after drop

    
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tree_widget = MyTreeWidget()
    tree_widget.show()
    sys.exit(app.exec_())
