from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLineEdit
from model import generate_response

class ChatInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.messages = QListWidget()

        self.new_message = QLineEdit()
        self.new_message.setPlaceholderText("Enter your message here")

        self.add_button = QPushButton("Add message")
        self.add_button.clicked.connect(self.add_message)

        self.edit_button = QPushButton("Edit message")
        self.edit_button.clicked.connect(self.edit_message)

        self.delete_button = QPushButton("Delete message")
        self.delete_button.clicked.connect(self.delete_message)

        self.regenerate_button = QPushButton("Regenerate request")
        self.regenerate_button.clicked.connect(self.regenerate_request)

        layout = QVBoxLayout()
        layout.addWidget(self.messages)
        layout.addWidget(self.new_message)
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.regenerate_button)

        self.setLayout(layout)

    def add_message(self):
        message = self.new_message.text()
        response = generate_response(message)
        self.messages.addItem(f"You: {message}")
        self.messages.addItem(f"GPT-Neo: {response}")
        self.new_message.clear()

    def edit_message(self):
        current_item = self.messages.currentItem()
        if current_item:
            new_text = self.new_message.text()
            current_item.setText(new_text)
            self.new_message.clear()

    def delete_message(self):
        current_item = self.messages.currentItem()
        if current_item:
            row = self.messages.row(current_item)
            self.messages.takeItem(row)

    def regenerate_request(self):
        current_item = self.messages.currentItem()
        if current_item:
            new_text = generate_response(current_item.text())
            current_item.setText(new_text)

def main():
    app = QApplication([])
    chat = ChatInterface()
    chat.show()
    app.exec_()

if __name__ == "__main__":
    main()
