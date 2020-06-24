# ratelimit-test
[ratelimit](https://github.com/tomasbasham/ratelimit) をテストする


モックサーバーの準備

- json-server をinstall
   - `npm install -g json-server`
- json-server を起動する
   - `json-server --watch db.json`

クライアント側(API呼び出し)の準備

```
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install ratelimit requests
```

テストを実行する。
json-serverを実行したターミナルを見守って、1分間に10回呼び出しているか確認する。

```
python3 ratelimit_test.py
```