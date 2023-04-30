from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex


class PandasModel(QAbstractTableModel):
    def __init__(self, data, haveOperation=True, floatRule=None):
        super().__init__()
        if haveOperation:
            data['操作'] = None
        self.floatRule = floatRule
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                if section < self._data.shape[1]:
                    return str(self._data.columns[section])
                else:
                    return None
            elif orientation == Qt.Vertical:
                return str(section + 1)
        return None

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            row = index.row()
            col = index.column()
            value = self._data.iloc[row, col]
            if self.floatRule:
                if col == self.floatRule[0]:
                    return f"{value:.{self.floatRule[1]}f}"
            return str(self._data.iloc[row, col])

        return None

    def dataX(self, rowIndex, colIndex, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            row = rowIndex
            col = colIndex
            return str(self._data.iloc[row, col])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            try:
                self._data.iloc[row, col] = value
            except:
                return False
            self.dataChanged.emit(index, index)
            return True
        return False

    def updateRow(self, row, item):
        for i in range(self.columnCount() - 1):
            self.setData(self.index(row, i), item[i], Qt.EditRole)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        self._data.drop(self._data.index[row], inplace=True)
        self.endRemoveRows()

    # def appendData(self, data):
    #     rowCount = self.rowCount()
    #     newFrame = DataFrame(data, columns=self._data.columns)
    #     self.beginInsertRows(QModelIndex(), rowCount, rowCount)
    #     self._data = pd.concat([self._data, newFrame], ignore_index=True)
    #     self.endInsertRows()

    def appendRow(self, data):
        rowCount = self.rowCount()
        self.beginInsertRows(QModelIndex(), rowCount, rowCount)
        self._data.loc[rowCount] = data
        self.endInsertRows()

    def clearRows(self):
        for i in range(self.rowCount() - 1, -1, -1):
            self.removeRow(i)
