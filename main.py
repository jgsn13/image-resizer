from design import Ui_MainWindow
from pathlib import Path
from theme import set_theme
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QIcon, QPixmap


class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QIcon("assets/window_icon.png"))

        self.current_dir = str(Path.home())
        self.chooseFileBtn.clicked.connect(self.open_image)
        self.resizeButton.clicked.connect(self.resize_image)
        self.saveButton.clicked.connect(self.save)

    def open_image(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            "Open image",
            self.current_dir,  # cross-platform home directory
            # FIX: 'options=QFileDialog.DontUseNativeDialog'
            filter="*.png *.jpg *.jpeg",
        )
        self.current_dir = str(image).split(f"{image}")[0]
        self.openFileInput.setText(image)  # add image path to file input
        self.img = QPixmap(image)  # do not change the original image
        self.imgLabel.setPixmap(self.img)
        self.widthInput.setText(str(self.img.width()))
        self.heightInput.setText(str(self.img.height()))

    def resize_image(self):
        width = int(self.widthInput.text())
        height = int(self.heightInput.text())

        original_width = self.img.width()
        original_height = self.img.height()

        if width != original_width and height != original_height:
            self.img = self.img.scaled(width, height)
        elif width != original_width:
            self.img = self.img.scaledToWidth(width)
        else:
            self.img = self.img.scaledToHeight(height)

        self.imgLabel.setPixmap(self.img)
        self.widthInput.setText(str(self.img.width()))
        self.heightInput.setText(str(self.img.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget, "Save image", self.current_dir
        )
        new_image = self.img.copy()
        new_image.save(image, "PNG")


if __name__ == "__main__":
    app = QApplication()
    set_theme(app)
    resize_image = ResizeImage()
    resize_image.show()
    app.exec()
