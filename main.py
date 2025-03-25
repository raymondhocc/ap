import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QPushButton, QLabel, QTreeWidget,
                           QTreeWidgetItem, QFrame, QTableWidget, QHeaderView,
                           QTableWidgetItem, QLineEdit, QFileDialog, QToolBar,
                           QComboBox, QSpacerItem, QSizePolicy, QDialog,
                           QFormLayout, QDateEdit, QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt, QSize, QDate
from PyQt6.QtGui import QIcon, QPixmap, QAction, QDoubleValidator

class EnterBillDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Bill")
        self.setMinimumWidth(500)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # Vendor selection
        self.vendor_combo = QComboBox()
        self.vendor_combo.addItems(["Hacienda Design", "Cisco's", "FedEx", "Snyder Uniform Supply"])
        self.vendor_combo.setEditable(True)
        form_layout.addRow("Vendor:", self.vendor_combo)

        # Invoice number
        self.invoice_number = QLineEdit()
        form_layout.addRow("Invoice #:", self.invoice_number)

        # Invoice date
        self.invoice_date = QDateEdit()
        self.invoice_date.setDate(QDate.currentDate())
        self.invoice_date.setCalendarPopup(True)
        form_layout.addRow("Invoice Date:", self.invoice_date)

        # Due date
        self.due_date = QDateEdit()
        self.due_date.setDate(QDate.currentDate().addDays(30))
        self.due_date.setCalendarPopup(True)
        form_layout.addRow("Due Date:", self.due_date)

        # Currency and amount
        amount_layout = QHBoxLayout()
        self.currency_combo = QComboBox()
        self.currency_combo.addItems(["USD", "EUR", "GBP"])
        self.amount_input = QLineEdit()
        self.amount_input.setValidator(QDoubleValidator(0.00, 999999999.99, 2))
        amount_layout.addWidget(self.currency_combo)
        amount_layout.addWidget(self.amount_input)
        form_layout.addRow("Amount:", amount_layout)

        # Payment method
        self.payment_method = QComboBox()
        self.payment_method.addItems(["Check", "Wire", "ePayment", "Virtual Card"])
        form_layout.addRow("Payment Method:", self.payment_method)

        # Bank account
        self.bank_account = QComboBox()
        self.bank_account.addItems(["Bank of America - 1408", "Wells Fargo - 2356"])
        form_layout.addRow("Pay From:", self.bank_account)

        # Notes
        self.notes = QTextEdit()
        self.notes.setMaximumHeight(100)
        form_layout.addRow("Notes:", self.notes)

        layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #0066cc;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #0052a3;
            }
        """)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        layout.addLayout(button_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AP Management System")
        self.setMinimumSize(1200, 800)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Top bar
        top_bar = QWidget()
        top_bar.setStyleSheet("background-color: white; border-bottom: 1px solid #ddd;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(10, 5, 10, 5)
        
        # Logo and company name
        logo_label = QLabel("AP")
        logo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2d3436;")
        
        company_combo = QComboBox()
        company_combo.addItem("Mach 5 LLC")
        company_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px;
                min-width: 150px;
            }
        """)
        
        # Right side icons
        icon_layout = QHBoxLayout()
        icons = ["🔍", "👤", "🕒", "🔄", "⚙️", "📋"]
        for icon in icons:
            btn = QPushButton(icon)
            btn.setFixedSize(32, 32)
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    border-radius: 16px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            icon_layout.addWidget(btn)
        
        search_box = QLineEdit()
        search_box.setPlaceholderText("Search...")
        search_box.setMinimumWidth(300)
        search_box.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px;
                background-color: #f8f9fa;
            }
        """)
        
        top_layout.addWidget(logo_label)
        top_layout.addWidget(company_combo)
        top_layout.addStretch()
        top_layout.addWidget(search_box)
        top_layout.addLayout(icon_layout)
        
        # Action toolbar
        action_bar = QWidget()
        action_bar.setStyleSheet("background-color: #f8f9fa; border-bottom: 1px solid #ddd;")
        action_layout = QHBoxLayout(action_bar)
        action_layout.setContentsMargins(10, 5, 10, 5)
        
        # Bills label and filters
        bills_label = QLabel("Bills")
        bills_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # Filter buttons
        filter_layout = QHBoxLayout()
        filters = ["Unpaid bills", "All bills", "Recurring bills", "Vendor credits"]
        for filter_text in filters:
            btn = QPushButton(filter_text)
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    padding: 5px 10px;
                    color: #666;
                }
                QPushButton:hover {
                    color: #000;
                    background-color: #e0e0e0;
                }
            """)
            filter_layout.addWidget(btn)
        
        # Upload and Enter Bill buttons
        upload_btn = QPushButton("Upload Invoice")
        upload_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 8px 15px;
                color: #333;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        upload_btn.clicked.connect(self.upload_invoice)
        
        enter_bill_btn = QPushButton("Enter Bill")
        enter_bill_btn.setStyleSheet("""
            QPushButton {
                background-color: #0066cc;
                border: none;
                border-radius: 4px;
                padding: 8px 15px;
                color: white;
            }
            QPushButton:hover {
                background-color: #0052a3;
            }
        """)
        enter_bill_btn.clicked.connect(self.show_enter_bill_dialog)
        
        action_layout.addWidget(bills_label)
        action_layout.addSpacing(20)
        action_layout.addLayout(filter_layout)
        action_layout.addStretch()
        action_layout.addWidget(upload_btn)
        action_layout.addWidget(enter_bill_btn)
        
        # Main content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Left sidebar
        left_sidebar = QWidget()
        left_sidebar.setMaximumWidth(200)
        left_sidebar.setStyleSheet("background-color: #f8f9fa; border-right: 1px solid #ddd;")
        left_layout = QVBoxLayout(left_sidebar)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        # Add menu items to left sidebar with dashboard features
        menu_items = {
            "DASHBOARD": [
                ("📊 Overview", "View key metrics and summaries"),
                ("💰 Cash Flow", "Track incoming and outgoing money"),
                ("📈 Analytics", "View detailed financial reports"),
                ("⚡ Quick Actions", "Common tasks and shortcuts")
            ],
            "PAYABLES": [
                ("📥 Inbox", "Review incoming documents"),
                ("📄 Documents", "Manage all documents"),
                ("👥 Vendors", "Manage vendor relationships"),
                ("✓ Approvals", "Review and approve items"),
                ("💳 Bills", "Manage and pay bills"),
                ("💸 Payments out", "Track outgoing payments")
            ],
            "RECEIVABLES": [
                ("🏢 Customers", "Manage customer relationships"),
                ("📋 Invoices", "Create and track invoices"),
                ("💱 Payments in", "Track incoming payments")
            ],
            "OTHER": [
                ("📊 Reports", "Generate financial reports"),
                ("❓ Support", "Get help and support")
            ]
        }
        
        for category, items in menu_items.items():
            # Add category label
            category_label = QLabel(category)
            category_label.setStyleSheet("""
                QLabel {
                    padding: 10px;
                    color: #666;
                    font-size: 12px;
                    font-weight: bold;
                    background-color: #f8f9fa;
                }
            """)
            left_layout.addWidget(category_label)
            
            # Add menu items with icons and tooltips
            for item_text, tooltip in items:
                btn = QPushButton(item_text)
                btn.setToolTip(tooltip)
                btn.setStyleSheet("""
                    QPushButton {
                        text-align: left;
                        padding: 10px 20px;
                        border: none;
                        color: #333;
                    }
                    QPushButton:hover {
                        background-color: #e9ecef;
                    }
                """)
                left_layout.addWidget(btn)
        
        left_layout.addStretch()
        
        # Main content table
        table = QTableWidget()
        table.setColumnCount(8)
        headers = ["Invoice #", "Vendor", "Due date", "Amount", "Status",
                  "Process date", "Payment type", "Pay from"]
        table.setHorizontalHeaderLabels(headers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setStyleSheet("""
            QTableWidget {
                border: none;
                background-color: white;
            }
            QHeaderView::section {
                background-color: white;
                padding: 8px;
                border: none;
                border-bottom: 1px solid #ddd;
                font-weight: bold;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
        """)
        
        # Add some sample data
        sample_data = [
            ["2023-09-13", "Hacienda Design", "09/20/23", "USD 800.00", "Manual", "09/28/23", "ePayment→9/29", "Bank of America"],
            ["34234234", "Cisco's", "10/10/23", "EUR 1,201.00", "Manual", "09/25/23", "Wire→9/15", "Bank of America"],
            ["11/28/2022", "FedEx", "10/13/23", "USD 705.27", "Manual", "10/05/23", "Virtual→9/28", "Bank of America"],
            ["89K227", "Snyder Uniform Supply", "12/23/23", "USD 500.00", "Manual", "12/21/23", "Check→9/27", "Bank of America"]
        ]
        
        table.setRowCount(len(sample_data))
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                table.setItem(row, col, item)
        
        # Add widgets to layouts
        content_layout.addWidget(left_sidebar)
        content_layout.addWidget(table)
        
        # Add all main components to main layout
        main_layout.addWidget(top_bar)
        main_layout.addWidget(action_bar)
        main_layout.addWidget(content_widget)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        self.statusBar().setStyleSheet("border-top: 1px solid #ddd;")
        
    def upload_invoice(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Invoice files (*.pdf *.png *.jpg *.jpeg)")
        if file_dialog.exec():
            filenames = file_dialog.selectedFiles()
            if filenames:
                self.statusBar().showMessage(f"Uploaded: {filenames[0]}")
                
    def show_enter_bill_dialog(self):
        dialog = EnterBillDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            QMessageBox.information(self, "Success", "Bill saved successfully!")
            self.statusBar().showMessage("Bill saved successfully")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
