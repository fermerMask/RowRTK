import json
import os

# config.json のパスを定義
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "conf", "config.json")

# JSON を読み込み
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

# 各種定数として展開
APP_NAME = config.get("app_name", "RowRTK")
APP_VERSION = config.get("version", "")
FONT_TYPE = config.get("font_type", "Arial")
FONT_SIZE = config.get("font_size", 12)
THEME = config.get("theme", "blue")
