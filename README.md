# MCP UUID サーバー

## 概要
このMCPサーバーは、UUIDを生成するためのシンプルなサービスを提供します。

## 環境要件
- Python 3.10以上
- MCP(Model Context Protocol)パッケージ v1.2.0以上
- Claude Desktop

## インストール方法
```bash
# 依存関係のインストール
uv pip sync
```

## 使用方法

### 1. Claude Desktopでの使用

#### 設定ファイルの編集
Claude Desktopの設定ファイルを編集して、このMCPサーバーを追加します。設定ファイルのパスは以下の通りです：

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

以下のJSON設定を追加します（既存の`mcpServers`オブジェクト内に追加）：

```json
{
  "mcpServers": {
    "uuid": {
      "command": "/path/to/uv",
      "args": [
          "--directory",
          "/path/to/mcp-uuid",
          "run",
          "get-uuid.py"
      ]
    }
  }
}
```

> 注意: `/path/to/uv`には、uvコマンドの絶対パスを指定してください。

### 2. 使用可能なツール

このMCPサーバーは以下のツールを提供します：

#### get_uuid
- 説明：新しいUUIDを生成します
- 入力パラメータ：なし
- 使用例：

Claude Desktopで以下のように入力することで、新しいUUIDを生成できます：
```
ランダムなIDを生成してください
```

すると、Claudeは内部的にMCPツールを呼び出し、新しいUUIDを生成して返します。

> 生成されたランダムなIDは次の通りです：
> eccf34af-1617-4f61-b148-e900bc1d3d00
