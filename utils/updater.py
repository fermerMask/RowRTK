import requests
import json
import os
import subprocess

# config.py から設定をインポート
from .config import VERSION_CHECK_URL

def check_for_updates():
    try:
        response = requests.get(VERSION_CHECK_URL)
        data = response.json()

        current_version = "1.0.0"  # 現在のアプリバージョン（固定または別途設定）
        latest_version = data['version']

        if latest_version > current_version:
            print(f"新しいバージョン {latest_version} が利用可能です！")
            download_url = data['download_url']
            download_and_install_update(download_url)
        else:
            print("現在のバージョンは最新です。")
    except Exception as e:
        print(f"アップデートの確認中にエラーが発生しました: {e}")

def download_and_install_update(download_url):
    try:
        print(f"ダウンロード中: {download_url}")
        response = requests.get(download_url)
        with open("update_installer.exe", "wb") as f:
            f.write(response.content)
        
        print("ダウンロード完了。インストールを開始します...")
        subprocess.run(["update_installer.exe"])
    except Exception as e:
        print(f"アップデートのダウンロード中にエラーが発生しました: {e}")
