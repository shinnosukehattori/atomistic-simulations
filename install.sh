#!/bin/bash

# 依存関係のインストール
pip install -r requirements.txt

# nequip_modelディレクトリの初期化
if [ ! -d "nequip_model" ]; then
    mkdir nequip_model
fi

echo "インストールが完了しました"