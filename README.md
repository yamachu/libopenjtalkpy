# libopenjtalkpy

Yet another LibOpenJTalk Python wrapper library

## libopenjtalkpy とは

OpenJTalkの非公式フォークの [LibOpenJTalk](https://github.com/yamachu/LibOpenJTalk) のラッパーライブラリ。
開発途中

## 特徴

PreBuiltのライブラリを使っているため、手元にCythonなどでビルドする環境が揃っていなくても動作する。
OpenJTalkでは提供されていないユーザ辞書機能の読み込みや、またユーザ辞書機能のコンパイル機能を備えている。

## インストール

### 動作確認済みの環境

WIP

### インストール方法

今後 pip でのインストールを可能にしますが，現在は _setup.py_ を使用してインストールします．

```
git clone https://github.com/yamachu/libopenjtalkpy.git
cd libopenjtalkpy
python setup.py install
```

このインストール中に使用しているプラットフォームを判別し，あらかじめビルドしてあるネイティブライブラリをダウンロードし展開します．

使用が可能になったかは

```
cd demo
python main.py
```

などで確認してみてください．


## 使い方

WIP

### 研究用途での使用

研究に使用する場合バージョンの固定などが必要になる場面があると思います．
本ラッパーはインストール時に [LibOpenJTalkのリリースページ](https://github.com/yamachu/LibOpenJTalk/release) から対象プラットフォームのライブラリをダウンロードしています．

自分で少し動作を変えたライブラリを試したいと言った場合は，

```
import libopenjtalkpy

libopenjtalkpy.get_native_library_path()
```

以上の手順でネイティブライブラリのインストールパスを取得することが出来ます．
そのパスに存在するライブラリファイルを置き換えることで，バージョンのピンニングなどが行なえます．

今後バージョンを指定し差し替えが可能なインタフェースなども検討しています．

#### 他の手段

ラッパー側でネイティブライブラリが読み込まれる前に読み込みパスを変更することで対応することも可能です．
ファイルの書き換えなどが必要なく，また User 権限でも可能であるなどのメリットが有ります．

```
import libopenjtalkpy

libopenjtalkpy._LibOpenJTalk_LIBRARY_PATH = 'HERE IS MY LIBRARY PATH'

from libopenjtalkpy.native import apis

# do something
```

このように _libopenjtalkpy_ の他のモジュールを呼ぶ以前に _libopenjtalkpy.\_LibOpenJTalk\_LIBRARY\_PATH_ を書き換えることで読み込み先を変更できます．
