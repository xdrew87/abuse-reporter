"""
AbuseIPDB Reporter - GUI Version 2.0.0 (PyQt6)

A beautiful graphical user interface for submitting abuse reports to AbuseIPDB API v2.
Built with PyQt6 for modern cross-platform UI with dark mode support.
Category text displays with correct colors and automatically hides/shows based on theme.
"""

import sys
import os
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QLineEdit, QComboBox, QTextEdit,
    QPushButton, QCheckBox, QSlider, QMessageBox, QScrollArea,
    QFrame, QProgressBar
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon

from dotenv import load_dotenv

# Multi-location .env discovery
env_paths = [
    Path.cwd() / '.env',
    Path(__file__).parent / '.env',
]
for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        break
else:
    load_dotenv()

from categories import CATEGORIES, get_category_id
from validators import validate_ip, validate_confidence, validate_comment, validate_api_key
from client import AbuseIPDBClient


class AbuseReporterGUI(QMainWindow):
    """Main GUI application with light and dark mode support."""
    
    # Accent colors (same in both modes)
    PRIMARY = "#0066cc"
    SECONDARY = "#00aaff"
    SUCCESS = "#00aa00"
    ERROR = "#ff3333"
    WARNING = "#ffaa00"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AbuseIPDB Reporter v2.0.0")
        self.setGeometry(100, 100, 1100, 750)
        
        self.dark_mode = False
        
        logo_path = Path(__file__).parent / "logo.svg"
        if logo_path.exists():
            self.setWindowIcon(QIcon(str(logo_path)))
        
        self.api_key = os.getenv("ABUSEIPDB_API_KEY")
        self.apply_theme()
        self.create_ui()
        
        if not self.api_key:
            QMessageBox.warning(self, " API Key Required",
                "ABUSEIPDB_API_KEY not configured.\nSet it in Settings tab or .env file.")
    
    def get_theme(self):
        """Return current theme colors."""
        if self.dark_mode:
            return {
                'bg': "#1e1e1e",
                'card': "#2d2d2d",
                'text': "#e0e0e0",
                'border': "#444444",
                'secondary': "#999999",
                'cat_text': "#00ccff",  # Light cyan for dark mode
            }
        else:
            return {
                'bg': "#f5f5f5",
                'card': "#ffffff",
                'text': "#333333",
                'border': "#e0e0e0",
                'secondary': "#666666",
                'cat_text': self.PRIMARY,  # Blue for light mode
            }
    
    def get_stylesheet(self):
        """Generate stylesheet based on current theme."""
        t = self.get_theme()
        return f"""
        QMainWindow {{ background-color: {t['bg']}; }}
        QWidget {{ background-color: {t['bg']}; color: {t['text']}; }}
        QLabel {{ color: {t['text']}; }}
        QLineEdit, QTextEdit {{ background-color: {t['card']}; color: {t['text']}; border: 1px solid {t['border']}; border-radius: 4px; padding: 6px; }}
        QLineEdit:focus, QTextEdit:focus {{ border: 2px solid {self.PRIMARY}; }}
        QComboBox {{ background-color: {t['card']}; color: {t['text']}; border: 1px solid {t['border']}; border-radius: 4px; padding: 4px; }}
        QComboBox:focus {{ border: 2px solid {self.PRIMARY}; }}
        QPushButton {{ background-color: {self.PRIMARY}; color: white; border: none; border-radius: 4px; padding: 8px 16px; font-weight: bold; min-height: 40px; }}
        QPushButton:hover {{ background-color: {self.SECONDARY}; }}
        QTabWidget::pane {{ border: 1px solid {t['border']}; }}
        QTabBar::tab {{ background-color: {t['border']}; color: {t['text']}; padding: 6px 20px; border: 1px solid {t['border']}; border-bottom: none; border-top-left-radius: 4px; border-top-right-radius: 4px; margin-right: 2px; }}
        QTabBar::tab:selected {{ background-color: {t['card']}; border-bottom: 2px solid {self.PRIMARY}; }}
        QCheckBox {{ color: {t['text']}; }}
        QSlider::groove:horizontal {{ background-color: {t['border']}; height: 6px; border-radius: 3px; }}
        QSlider::handle:horizontal {{ background-color: {self.PRIMARY}; width: 16px; margin: -5px 0; border-radius: 8px; }}
        QSlider::handle:horizontal:hover {{ background-color: {self.SECONDARY}; }}
        """
    
    def apply_theme(self):
        """Apply the current theme."""
        self.setStyleSheet(self.get_stylesheet())
    
    def create_ui(self):
        """Create main UI."""
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Header
        header = QHBoxLayout()
        logo_path = Path(__file__).parent / "logo.svg"
        if logo_path.exists():
            logo = QLabel()
            logo.setPixmap(QPixmap(str(logo_path)).scaledToWidth(60, Qt.TransformationMode.SmoothTransformation))
            logo.setFixedSize(60, 60)
            header.addWidget(logo)
        
        title = QLabel(" AbuseIPDB Reporter")
        title_font = QFont("Segoe UI", 18, QFont.Weight.Bold)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {self.PRIMARY};")
        header.addWidget(title, 1)
        
        version = QLabel("v2.0.0")
        version.setStyleSheet("color: #888888; font-size: 9pt;")
        header.addWidget(version)
        layout.addLayout(header)
        
        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setStyleSheet(f"color: {self.get_theme()['border']};")
        layout.addWidget(sep)
        
        # Tabs
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        self.create_submit_tab()
        self.create_bulk_tab()
        self.create_categories_tab()
        self.create_settings_tab()
        
        central.setLayout(layout)
    
    def create_submit_tab(self):
        """Create single report tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(12)
        t = self.get_theme()
        
        layout.addWidget(QLabel("IP Address"))
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("e.g., 192.0.2.1")
        layout.addWidget(self.ip_input)
        
        layout.addWidget(QLabel("Category"))
        self.category_combo = QComboBox()
        self.category_combo.addItems([CATEGORIES[cid] for cid in sorted(CATEGORIES.keys())])
        layout.addWidget(self.category_combo)
        
        layout.addWidget(QLabel("Comment"))
        self.comment_input = QTextEdit()
        self.comment_input.setPlaceholderText("Describe the abuse...")
        self.comment_input.setMaximumHeight(80)
        layout.addWidget(self.comment_input)
        
        layout.addWidget(QLabel("Confidence (0-100%)"))
        conf_h = QHBoxLayout()
        self.conf_slider = QSlider(Qt.Orientation.Horizontal)
        self.conf_slider.setRange(0, 100)
        self.conf_slider.setValue(100)
        self.conf_slider.setTickInterval(10)
        self.conf_label = QLabel("100%")
        self.conf_label.setMinimumWidth(40)
        self.conf_slider.valueChanged.connect(lambda v: self.conf_label.setText(f"{v}%"))
        conf_h.addWidget(self.conf_slider, 1)
        conf_h.addWidget(self.conf_label)
        layout.addLayout(conf_h)
        
        self.dry_run_cb = QCheckBox(" Dry-run mode")
        layout.addWidget(self.dry_run_cb)
        
        btn = QPushButton(" Submit Report")
        btn.setMinimumHeight(42)
        btn.clicked.connect(self.submit_single)
        layout.addWidget(btn)
        
        self.submit_status = QLabel("")
        self.submit_status.setWordWrap(True)
        layout.addWidget(self.submit_status)
        layout.addStretch()
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, " Submit")
    
    def create_bulk_tab(self):
        """Create bulk report tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(12)
        
        layout.addWidget(QLabel("IP Addresses (one per line)"))
        self.bulk_ips = QTextEdit()
        self.bulk_ips.setPlaceholderText("192.0.2.1\n192.0.2.2")
        self.bulk_ips.setMaximumHeight(80)
        layout.addWidget(self.bulk_ips)
        
        layout.addWidget(QLabel("Category"))
        self.bulk_cat = QComboBox()
        self.bulk_cat.addItems([CATEGORIES[cid] for cid in sorted(CATEGORIES.keys())])
        layout.addWidget(self.bulk_cat)
        
        layout.addWidget(QLabel("Comment"))
        self.bulk_comment = QTextEdit()
        self.bulk_comment.setMaximumHeight(70)
        layout.addWidget(self.bulk_comment)
        
        layout.addWidget(QLabel("Confidence (0-100%)"))
        bulk_conf_h = QHBoxLayout()
        self.bulk_conf_slider = QSlider(Qt.Orientation.Horizontal)
        self.bulk_conf_slider.setRange(0, 100)
        self.bulk_conf_slider.setValue(100)
        self.bulk_conf_slider.setTickInterval(10)
        self.bulk_conf_label = QLabel("100%")
        self.bulk_conf_label.setMinimumWidth(40)
        self.bulk_conf_slider.valueChanged.connect(lambda v: self.bulk_conf_label.setText(f"{v}%"))
        bulk_conf_h.addWidget(self.bulk_conf_slider, 1)
        bulk_conf_h.addWidget(self.bulk_conf_label)
        layout.addLayout(bulk_conf_h)
        
        self.bulk_progress = QProgressBar()
        self.bulk_progress.setVisible(False)
        layout.addWidget(self.bulk_progress)
        
        btn = QPushButton("🚀 Submit Bulk")
        btn.setMinimumHeight(42)
        btn.clicked.connect(self.submit_bulk)
        layout.addWidget(btn)
        
        self.bulk_status = QLabel("")
        self.bulk_status.setWordWrap(True)
        layout.addWidget(self.bulk_status)
        layout.addStretch()
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "📦 Bulk")
    
    def create_categories_tab(self):
        """Create categories tab with proper text colors for both modes."""
        tab = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("AbuseIPDB Categories"))
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_w = QWidget()
        scroll_l = QVBoxLayout()
        scroll_l.setSpacing(8)
        
        t = self.get_theme()
        
        for cid in sorted(CATEGORIES.keys()):
            cname = CATEGORIES[cid]
            
            card = QFrame()
            card.setStyleSheet(f"background-color: {t['card']}; border-left: 4px solid {self.PRIMARY}; border-radius: 4px; padding: 10px;")
            card_l = QVBoxLayout()
            
            # Category label with theme-appropriate color
            cat_label = QLabel(f"[ID: {cid}] {cname}")
            cat_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
            cat_label.setStyleSheet(f"color: {t['cat_text']};")  # Use theme-specific color
            card_l.addWidget(cat_label)
            
            desc = QLabel(f"For reporting: {cname}")
            desc.setStyleSheet(f"color: {t['secondary']}; font-size: 9pt;")
            card_l.addWidget(desc)
            
            card.setLayout(card_l)
            scroll_l.addWidget(card)
        
        scroll_l.addStretch()
        scroll_w.setLayout(scroll_l)
        scroll.setWidget(scroll_w)
        layout.addWidget(scroll)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "📚 Categories")
    
    def create_settings_tab(self):
        """Create settings tab."""
        tab = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        layout.addWidget(QLabel("🎨 Appearance"))
        theme_h = QHBoxLayout()
        self.theme_btn = QPushButton(f"🌙 Dark Mode: {'ON' if self.dark_mode else 'OFF'}")
        self.theme_btn.setMinimumHeight(35)
        self.theme_btn.clicked.connect(self.toggle_theme)
        theme_h.addWidget(self.theme_btn)
        theme_h.addStretch()
        layout.addLayout(theme_h)
        
        layout.addWidget(QLabel("🔐 API Configuration"))
        
        if self.api_key:
            status = f"✅ API Key: {self.api_key[:10]}{'*'*10}"
            status_color = self.SUCCESS
        else:
            status = "❌ API Key: Not configured"
            status_color = self.ERROR
        
        self.status_lbl = QLabel(status)
        self.status_lbl.setStyleSheet(f"color: {status_color};")
        layout.addWidget(self.status_lbl)
        
        # API key input
        layout.addWidget(QLabel("Enter/Update API Key:"))
        key_h = QHBoxLayout()
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Paste your AbuseIPDB API key here")
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.api_key_input.setText(self.api_key if self.api_key else "")
        key_h.addWidget(self.api_key_input, 1)
        
        save_key_btn = QPushButton("💾 Save Key")
        save_key_btn.setMinimumHeight(35)
        save_key_btn.clicked.connect(self.save_api_key)
        key_h.addWidget(save_key_btn)
        layout.addLayout(key_h)
        
        layout.addWidget(QLabel("Setup Instructions:"))
        
        inst = QLabel(
            "1. Get FREE API key from:\n   https://www.abuseipdb.com/api\n\n"
            "2. Paste your key above and click 'Save Key'\n   (Will be saved to .env file)\n\n"
            "3. Key will be used on next submission\n\n"
            "💡 The .env file is saved in the app directory"
        )
        t = self.get_theme()
        inst.setStyleSheet(f"color: {t['text']}; font-family: Courier New; font-size: 9pt; background-color: {t['card']}; padding: 10px; border-radius: 4px;")
        inst.setWordWrap(True)
        layout.addWidget(inst)
        
        layout.addSpacing(15)
        layout.addWidget(QLabel("ℹ️ About"))
        
        about = QLabel(
            "AbuseIPDB Reporter v2.0.0\n\n"
            "✓ PyQt6 GUI\n"
            "✓ Light & Dark Mode\n"
            "✓ IPv4 & IPv6\n"
            "✓ All 23 categories\n"
            "✓ Dry-run mode\n\n"
            "📄 License: MIT"
        )
        layout.addWidget(about)
        layout.addStretch()
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "⚙️ Settings")
    
    def toggle_theme(self):
        """Toggle between light and dark mode."""
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        
        # Recreate all tabs
        self.tabs.clear()
        self.create_submit_tab()
        self.create_bulk_tab()
        self.create_categories_tab()
        self.create_settings_tab()
        
        mode = "🌙 Dark Mode" if self.dark_mode else "☀️ Light Mode"
        QMessageBox.information(self, "Theme Changed", f"Switched to {mode}")
    
    def save_api_key(self):
        """Save API key to .env file."""
        key = self.api_key_input.text().strip()
        
        if not key:
            QMessageBox.critical(self, "Error", "API key cannot be empty")
            return
        
        if len(key) < 10:
            QMessageBox.critical(self, "Error", "API key seems too short")
            return
        
        try:
            # Find or create .env file in script directory
            env_file = Path(__file__).parent / '.env'
            
            # Read existing .env if it exists
            env_content = {}
            if env_file.exists():
                with open(env_file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            k, v = line.split('=', 1)
                            env_content[k.strip()] = v.strip()
            
            # Update API key
            env_content['ABUSEIPDB_API_KEY'] = key
            
            # Write back to .env
            with open(env_file, 'w') as f:
                f.write("# AbuseIPDB Reporter Configuration\n")
                f.write("# Keep this file secure - it contains your API key\n\n")
                for k, v in env_content.items():
                    f.write(f"{k}={v}\n")
            
            # Update the instance variable
            self.api_key = key
            
            # Update status label
            self.status_lbl.setText(f"✅ API Key: {key[:10]}{'*'*10}")
            self.status_lbl.setStyleSheet(f"color: {self.SUCCESS};")
            
            # Clear and disable input
            self.api_key_input.setText("")
            
            QMessageBox.information(self, "✅ Success",
                f"API key saved successfully!\n\nFile: {env_file}\n\n"
                "Your key will be used for all future reports.")
        
        except PermissionError:
            QMessageBox.critical(self, "Error",
                f"Permission denied writing to {env_file}\n\n"
                "Try running the application as administrator.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save API key:\n{str(e)}")
    
    def submit_single(self):
        """Submit single report."""
        ip = self.ip_input.text().strip()
        if not ip or not validate_ip(ip):
            QMessageBox.critical(self, "Error", "Invalid IP address")
            return
        
        comment = self.comment_input.toPlainText().strip()
        if not comment:
            QMessageBox.critical(self, "Error", "Comment required")
            return
        
        confidence = self.conf_slider.value()
        cat_name = self.category_combo.currentText()
        cat_id = get_category_id(cat_name)
        
        if self.dry_run_cb.isChecked():
            self.submit_status.setText("✅ Validation passed (dry-run)")
            self.submit_status.setStyleSheet(f"color: {self.SUCCESS};")
            QMessageBox.information(self, "✅ Dry-Run OK", f"IP: {ip}\nCategory: {cat_name}\nConfidence: {confidence}%")
            return
        
        if not self.api_key:
            QMessageBox.critical(self, "Error", "API key not configured")
            return
        
        try:
            self.submit_status.setText("⏳ Submitting...")
            self.submit_status.setStyleSheet(f"color: {self.WARNING};")
            QApplication.processEvents()
            
            client = AbuseIPDBClient(self.api_key)
            result = client.submit_report(ip, [cat_id], comment, confidence)
            
            if result.success:
                self.submit_status.setText("✅ Report submitted successfully")
                self.submit_status.setStyleSheet(f"color: {self.SUCCESS};")
                QMessageBox.information(self, "✅ Success", "Report submitted!")
                self.ip_input.clear()
                self.comment_input.clear()
            else:
                self.submit_status.setText(f"❌ {result.message}")
                self.submit_status.setStyleSheet(f"color: {self.ERROR};")
                QMessageBox.critical(self, "Error", result.message)
        except Exception as e:
            self.submit_status.setText(f"❌ Error: {str(e)}")
            self.submit_status.setStyleSheet(f"color: {self.ERROR};")
            QMessageBox.critical(self, "Error", str(e))
    
    def submit_bulk(self):
        """Submit bulk reports."""
        ips = [ip.strip() for ip in self.bulk_ips.toPlainText().split('\n') if ip.strip()]
        if not ips:
            QMessageBox.critical(self, "Error", "Enter at least one IP")
            return
        
        if not all(validate_ip(ip) for ip in ips):
            QMessageBox.critical(self, "Error", "Invalid IP in list")
            return
        
        comment = self.bulk_comment.toPlainText().strip()
        if not comment:
            QMessageBox.critical(self, "Error", "Comment required")
            return
        
        if not self.api_key:
            QMessageBox.critical(self, "Error", "API key not configured")
            return
        
        try:
            self.bulk_progress.setVisible(True)
            self.bulk_progress.setMaximum(len(ips))
            
            cat_id = get_category_id(self.bulk_cat.currentText())
            confidence = self.bulk_conf_slider.value()
            
            client = AbuseIPDBClient(self.api_key)
            successful = 0
            
            for i, ip in enumerate(ips, 1):
                self.bulk_status.setText(f"⏳ Submitting {i}/{len(ips)}...")
                self.bulk_progress.setValue(i)
                QApplication.processEvents()
                
                result = client.submit_report(ip, [cat_id], comment, confidence)
                if result.success:
                    successful += 1
            
            self.bulk_progress.setVisible(False)
            self.bulk_status.setText(f"✅ Complete: {successful}/{len(ips)} successful")
            self.bulk_status.setStyleSheet(f"color: {self.SUCCESS};")
            QMessageBox.information(self, "✅ Done", f"Submitted {successful}/{len(ips)}")
        except Exception as e:
            self.bulk_progress.setVisible(False)
            self.bulk_status.setText(f"❌ Error: {str(e)}")
            self.bulk_status.setStyleSheet(f"color: {self.ERROR};")
            QMessageBox.critical(self, "Error", str(e))


def main():
    app = QApplication(sys.argv)
    window = AbuseReporterGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
