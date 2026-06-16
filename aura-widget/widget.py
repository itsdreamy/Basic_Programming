from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QTextEdit, QPushButton, QLabel)
from PyQt6.QtGui import QPainter, QColor, QPen
from brain import AIBrain

class AIWorker(QThread):
    """Separate thread to fetch AI answers so the GUI stays buttery smooth."""
    response_ready = pyqtSignal(str)

    def __init__(self, brain, user_text, include_clip):
        super().__init__()
        self.brain = brain
        self.user_text = user_text
        self.include_clip = include_clip

    def run(self):
        reply = self.brain.process_response(self.user_text, self.include_clip)
        self.response_ready.emit(reply)


class FloatingOrb(QWidget):
    """The actual visual floating widget."""
    def __init__(self):
        super().__init__()
        self.brain = AIBrain()
        self.is_expanded = False
        self.drag_position = None
        
        self.init_ui()

    def init_ui(self):
        # Framework setup: Frameless, transparent background, stays on top of everything
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.SubWindow)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.resize(320, 450)
        self.move(100, 100) # Initial spawn position on your desktop

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        # 1. The Interactive AI Orb Header
        self.orb_button = QPushButton()
        self.orb_button.setFixedSize(50, 50)
        self.orb_button.setCursor(Qt.CursorShape.PointingHandCursor)
        # Smooth styling: Dark slate blue glowing sphere
        self.orb_button.setStyleSheet("""
            QPushButton {
                background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #4A5568, stop:1 #2D3748);
                border: 2px solid #63B3ED;
                border-radius: 25px;
            }
            QPushButton:hover {
                border: 2px solid #4FD1C5;
                background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #5A67D8, stop:1 #3C366B);
            }
        """)
        self.orb_button.clicked.connect(self.toggle_expansion)
        self.main_layout.addWidget(self.orb_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # 2. Hidden Panel Container (Slides/Reveals when orb clicked)
        self.panel_widget = QWidget()
        self.panel_widget.setStyleSheet("""
            QWidget {
                background-color: #1A202C;
                border-radius: 12px;
                border: 1px solid #4A5568;
            }
        """)
        panel_layout = QVBoxLayout()
        
        # Chat log display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("color: #E2E8F0; border: none; font-size: 12px;")
        self.chat_display.setPlaceholderText("AURA Companion ready...")
        panel_layout.addWidget(self.chat_display)

        # Bottom Input Area
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ask AURA or command...")
        self.input_field.setStyleSheet("color: white; background-color: #2D3748; padding: 6px; border-radius: 6px; border: none;")
        self.input_field.returnPressed.connect(self.send_to_ai)
        input_layout.addWidget(self.input_field)

        # Specialized Smart Clipboard Button
        self.clip_btn = QPushButton("📋")
        self.clip_btn.setToolTip("Ask using your highlighted clipboard text context")
        self.clip_btn.setFixedSize(30, 30)
        self.clip_btn.setStyleSheet("color: white; background-color: #4A5568; border-radius: 6px; font-size: 14px;")
        self.clip_btn.clicked.connect(lambda: self.send_to_ai(use_clipboard=True))
        input_layout.addWidget(self.clip_btn)

        panel_layout.addLayout(input_layout)
        self.panel_widget.setLayout(panel_layout)
        
        self.main_layout.addWidget(self.panel_widget)
        self.panel_widget.setVisible(False) # Start hidden until clicked

    def toggle_expansion(self):
        """Collapses or expands the main chat panel when the bubble icon is clicked."""
        self.is_expanded = not self.is_expanded
        self.panel_widget.setVisible(self.is_expanded)

    def send_to_ai(self, use_clipboard=False):
        text = self.input_field.text().strip()
        if not text and not use_clipboard:
            return

        if use_clipboard:
            text = text if text else "Analyze or fix this code/text from my clipboard:"
            self.chat_display.append(f"<b>You (with clipboard):</b> {text}")
        else:
            self.chat_display.append(f"<b>You:</b> {text}")

        self.input_field.clear()
        self.chat_display.append("<i style='color: #A0AEC0;'>AURA is thinking...</i>")
        
        # Change Orb color to dynamic Purple to show active "Thinking Mode"
        self.orb_button.setStyleSheet("background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, stop:0 #9F7AEA, stop:1 #553C9A); border: 2px solid #D6BCFA; border-radius: 25px;")

        # Fire off asynchronous background worker thread so the main program never hangs
        self.worker = AIWorker(self.brain, text, use_clipboard)
        self.worker.response_ready.connect(self.handle_ai_response)
        self.worker.start()

    def handle_ai_response(self, reply):
        # Reset visual orb style back to default blue "Idle"
        self.orb_button.setStyleSheet("""
            QPushButton {
                background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 #4A5568, stop:1 #2D3748);
                border: 2px solid #63B3ED; border-radius: 25px;
            }
            QPushButton:hover { border: 2px solid #4FD1C5; }
        """)
        # Remove the 'Thinking...' text and print the real reply
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.chat_display.setTextCursor(cursor)
        
        self.chat_display.append(f"<b>AURA:</b> {reply}<br>")

    # --- Desktop Drag and Drop Movement Handlers ---
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()