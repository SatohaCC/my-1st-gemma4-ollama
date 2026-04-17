# 🛠 インストール手順

このプロジェクトを実行するためのセットアップ手順です。

## 1. Ollama のインストール
Windows の PowerShell を開き、以下のコマンドを実行して Ollama をインストールします。

```powershell
irm https://ollama.com/install.ps1 | iex
```

## 2. Python 環境のセットアップ
`uv` を使用して仮想環境の作成と、必要なライブラリのインストールを行います。

```bash
# uv自体のインストール
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# 依存関係の同期（仮想環境の自動作成・インストール）
uv sync
```

新規インストールの場合、uv initから
```bash
uv init
uv add ollama
```

## 3. モデルの準備と動作確認
使用するモデル (`gemma4:e4b`) をダウンロードし、対話モードで起動します。

```bash
ollama run gemma4:e4b
```

> [!NOTE]
> モデルの初回実行時にはダウンロードが始まります。完了後、そのままコンソールでチャットが可能です。

---

### Ollamaの止め方
タスクトレイから右クリックで止める？？
