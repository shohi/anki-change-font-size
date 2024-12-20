from aqt import mw
from aqt.qt import QApplication, QWebEngineProfile, QWebEngineSettings

# Version: 0.0.1

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

# use current setting
config_handler(mw.addonManager.getConfig(__name__))

# register handler
register_config_handler(__name__)