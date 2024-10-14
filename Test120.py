import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QPushButton, QWidget, QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery


class Market:
    def __init__(self, title, price, description, number):
        self._title = title
        self._price = price
        self._description = description
        self._number = number

    def get_title(self):
        return self._title

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description

    def get_number(self):
        return self._number


class grafo(QWidget):
    def __init__(self, gnorismata):
        super().__init__()
        self.layout = QVBoxLayout()
        self.leksi = QLineEdit()
        self.layout.addWidget(self.leksi)

        self.button = QPushButton(f'Input {gnorismata}')
        self.button.clicked.connect(self.anagnosi)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def anagnosi(self):
        return self.leksi.text()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MarketSystem_of_Assessment1')
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)

        self.idInput = grafo('ID')
        self.layout.addWidget(self.idInput)

        self.titlos = grafo('title')
        self.layout.addWidget(self.titlos)

        self.timi = grafo('price')
        self.layout.addWidget(self.timi)

        self.perigrafi = grafo('description')
        self.layout.addWidget(self.perigrafi)

        self.arithmos = grafo('number')
        self.layout.addWidget(self.arithmos)

        self.addButton = QPushButton("Submit")
        self.addButton.clicked.connect(self.submit_data)
        self.layout.addWidget(self.addButton)
        
        self.deleteButton = QPushButton("Delete by ID")
        self.deleteButton.clicked.connect(self.delete_data)
        self.layout.addWidget(self.deleteButton)

        self.montelo = QSqlQueryModel()
        self.load_data()
        
        self.sentoni = QTableView()
        self.sentoni.setModel(self.montelo)
        self.layout.addWidget(self.sentoni)

    def load_data(self):
        link = QSqlDatabase.addDatabase('QSQLITE')
        link.setDatabaseName('A1_Market.db')
        if not link.open():
            print('Database Error: Could not connect to database')
            sys.exit(1)
            
        self.montelo.setQuery('select * from a1market')

    def submit_data(self):
        title = self.titlos.anagnosi()
        price = self.timi.anagnosi()
        description = self.perigrafi.anagnosi()
        number = self.arithmos.anagnosi()

        eisago = Market(title, price, description, number)

        link = QSqlDatabase.addDatabase('QSQLITE')
        link.setDatabaseName('A1_Market.db')
        if not link.open():
            print('Database Error: Could not connect to database')
            sys.exit(1)

        psachno = QSqlQuery()
        psachno.exec_(
            'create table if not exists a1market(id integer primary key, name text, price real not null, description text, number text)')

        psachno.exec_(f"insert into a1market(name, price, description, number) values ('{eisago.get_title()}', '{eisago.get_price()}', '{eisago.get_description()}', '{eisago.get_number()}')")

        self.load_data()
        self.sentoni.setModel(self.montelo)

    def delete_data(self):
        id_to_delete = self.idInput.anagnosi()
        
        link = QSqlDatabase.addDatabase('QSQLITE')
        link.setDatabaseName('A1_Market.db')
        if not link.open():
            print('Database Error: Could not connect to database')
            sys.exit(1)
        
        psachno = QSqlQuery()
        psachno.prepare('delete from a1market where id = :id')
        psachno.bindValue(':id', int(id_to_delete))
        
        if psachno.exec_():
            print('Record deleted successfully')
            self.load_data()
            self.sentoni.setModel(self.montelo)
        else:
            print('Error deleting record from database')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
