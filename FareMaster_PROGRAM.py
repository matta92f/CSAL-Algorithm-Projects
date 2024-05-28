# Import Necessary Modules and Libraries from PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    # Load UI
    # Connect Two Button Clicks
    # Set Column Count and Header Labels
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('FareMasterUI_ViewData.ui', self)

        self.btnAddPane.clicked.connect(self.show_AddRecordPane)
        self.btnSort.clicked.connect(self.do_SelectionSort)

        self.tblData.setColumnCount(12)
        self.tblData.setHorizontalHeaderLabels([
            "DriverID", "First Name", "Last Name", "JeepneyID", "Origin", "Destination",
            "Time of Departure", "Total Passengers", "Total Fares Collected",
            "DispatcherID", "First Name", "Last Name"
        ])

    def show_AddRecordPane(self):
        # Create an AddRecord Dialog
        # Execute AddRecord Dialog
        # Retrieve Record Data
        # Pass to add_Record
        dialog = AddRecord(self)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.get_record_data()
            self.add_Record(data)

    def add_Record(self, data):
        # Add New Row to tblData Table
        # Fill Table with Provided Values
        row_count = self.tblData.rowCount()
        self.tblData.insertRow(row_count)

        for column, item in enumerate(data):
            table_item = QTableWidgetItem(str(item))
            self.tblData.setItem(row_count, column, table_item)

    def do_SelectionSort(self):
        # Perform Selection Sort on Data in tblData Table
        # Sort Data by the "Total Fares Collected" Column
        # Update Table with Sorted Data
        rows = []
        for row in range(self.tblData.rowCount()):
            row_data = []
            for column in range(self.tblData.columnCount()):
                item = self.tblData.item(row, column)
                row_data.append(item.text())
            rows.append(row_data)

        n = len(rows)
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if rows[j][8] > rows[max_index][8]:
                    max_index = j
            if max_index != i:
                rows[max_index], rows[i] = rows[i], rows[max_index]

        self.tblData.setRowCount(0)

        for row, data in enumerate(rows):
            self.tblData.insertRow(row)
            for column, item in enumerate(data):
                table_item = QTableWidgetItem(item)
                self.tblData.setItem(row, column, table_item)


class AddRecord(QDialog):
    # Load UI
    # Connect Three Button Clicks
    def __init__(self, parent=None):
        super(AddRecord, self).__init__(parent)
        loadUi('FareMasterUI_AddPane.ui', self)

        self.btnAdd.clicked.connect(self.on_AddButton_clicked)
        self.btnClear.clicked.connect(self.on_ClearButton_clicked)
        self.btnViewData.clicked.connect(self.on_ViewData_clicked)

    def on_AddButton_clicked(self):
        # Collect Values from Fields
        # Store Values in record_data List
        # Accept Dialog
        # Allow Main Window to Retrieve Record Data
        record_data = [
            self.tbDriverId.text(),
            self.tbDriverFN.text(),
            self.tbDriverLN.text(),
            self.tbJeepneyId.text(),
            self.cmbOrigin.currentText(),
            self.cmbDestination.currentText(),
            self.timeDepart.time().toString("hh:mm AP"),
            self.spnPassenger.value(),
            self.spnFares.value(),
            self.tbDispatcherId.text(),
            self.tbDispatcherFN.text(),
            self.tbDispatcherLN.text()
        ]
        self.record_data = record_data
        self.accept()

    def on_ClearButton_clicked(self):
        # Clear Values from Fields
        self.tbDriverId.clear()
        self.tbDriverFN.clear()
        self.tbDriverLN.clear()
        self.tbJeepneyId.clear()
        self.cmbOrigin.clear()
        self.cmbDestination.clear()
        self.timeDepart.clear()
        self.spnPassenger.clear()
        self.spnFares.clear()
        self.tbDispatcherId.clear()
        self.tbDispatcherFN.clear()
        self.tbDispatcherLN.clear()

    def on_ViewData_clicked(self):
        # Close Current Dialog
        # Show Main Window
        main_window = self.parent()
        self.close()
        main_window.show()

    def get_record_data(self):
        # Return record_data List
        return self.record_data


if __name__ == '__main__':
    # Show Main Window
    # Start Application Event Loop
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())