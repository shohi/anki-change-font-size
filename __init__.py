from aqt import mw
from aqt.qt import QApplication, QWebEngineProfile, QWebEngineSettings

# NOTE: only support Qt6

# --------------------- config --------------------
# config only available in addon's init module
def config_handler(config):
    font_size = config['font-size']

    # current window
    font = QApplication.font()
    font.setPixelSize(font_size)
    QApplication.setFont(font)

    # web engine window
    weps = QWebEngineProfile.defaultProfile().settings()
    weps.setFontSize(QWebEngineSettings.FontSize.MinimumFontSize, font_size)

def register_config_handler(mod):
    mw.addonManager.setConfigUpdatedAction(mod, config_handler)

register_config_handler(__name__)