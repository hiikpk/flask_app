#coding: utf-8

#必要なモジュールのインポート
from flask import Flask, render_template

#appという名前でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

#--- View側の設定 ---
#ルートディレクトリにアクセスした場合のの挙動
@app.route('/')
def index():
    #return 'Hello World!'
    return render_template('index.html')

#エントリーポート
if __name__ == '__main__':
    app.run()

