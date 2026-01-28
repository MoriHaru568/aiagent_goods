# aiagent_goods
## セットアップ手順

1. 開発環境の準備  
   以下のツールをインストールしてください。  
   - Python（推奨: 3.11 以上）  
   - VSCode などのコードエディタ  
   - Git  

2. リポジトリをクローン  
   GitHub からコードをクローンします。

   ```bash
   git clone <リポジトリのURL>
   cd <プロジェクトディレクトリ>
   ```

3. 環境変数ファイルの作成  
   `.env.sample` をコピーして `.env` ファイルを作成し、環境変数を設定します。

   ```bash
   cp .env.sample .env
   ```

   `.env` ファイルを編集し、以下のように OpenAI の APIキーを設定してください。

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. 仮想環境の作成  
   ターミナルで以下のコマンドを実行し、仮想環境を作成します。

   ```bash
   python -m venv env
   ```

5. 仮想環境の有効化とライブラリのインストール  

   - Windows の場合

     ```bash
     .\env\Scripts\activate
     pip install -r requirements.txt
     ```

   - macOS / Linux の場合

     ```bash
     source env/bin/activate
     pip install -r requirements.txt
     ```

6. アプリケーションの起動  
   以下のコマンドを実行して、アプリを起動します。

   ```bash
   python app.py
   ```

7. 動作確認  
   コマンド実行後、ターミナルに以下のようなURLが表示されます。

   ```
   Running on http://xxx
   ```

   表示された URL をブラウザで開いてください。
