"""
Anki addon to change font size for UI and web content.
Version: 0.0.1
Note: Only supports Qt6 (Anki 24.11+)
"""

from aqt import mw
from aqt.qt import QApplication, QWebEngineProfile, QWebEngineSettings


def apply_font_size(config: dict) -> None:
    """Apply font size configuration to Anki UI and web content."""
    font_size = config.get("font-size", 18)

    # Set UI font size
    font = QApplication.font()
    font.setPixelSize(font_size)
    QApplication.setFont(font)

    # Set web content minimum font size
    profile = QWebEngineProfile.defaultProfile()
    if profile:
        settings = profile.settings()
        if settings:
            settings.setFontSize(QWebEngineSettings.FontSize.MinimumFontSize, font_size)


# Apply current configuration
config = mw.addonManager.getConfig(__name__)
if config:
    apply_font_size(config)

# Register handler for configuration updates
mw.addonManager.setConfigUpdatedAction(__name__, apply_font_size)
