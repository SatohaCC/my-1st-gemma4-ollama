
### Ollamaをインストール
irm https://ollama.com/install.ps1 | iex


### ollama 起動
上下キーでモデルを選択してEnterで起動
そのままコンソールでチャットは可能

---


# Ollamaサーバーの起動
ollama serve

# 別ターミナルで実行
# E4B（最もバランスが良い）
ollama run gemma4

# 26B MoE（M3 Pro 36GBなら快適に動く）
ollama run gemma4:26b

# 31B Dense（36GB以上推奨）
ollama run gemma4:31b
