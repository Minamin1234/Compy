Welcome to the Compy wiki!
# `from` Compy，`Compy.py`
## 概要 - About
コマンドアプリケーション上でコマンドによる振る舞いを提供する為のクラスモジュール
ユーザ定義のコマンドと機能の実装も可能．

## 機能 - Function
コマンドを呼び出し，定義した処理を行います．<br>
そして，以下の手順を繰り返します．
* コマンドの取得
* コマンドの解読，対象モジュールと命令，引数を読み取る．
* コマンドで指定したモジュールを実行
* 実行結果をコンソール上に表示させる．<br><br>
```quit```コマンドが呼び出されるまで，上記の手順を永遠に繰り返します．

## 環境 - Environment
(推奨=開発した環境)<br>
python 3.7 <= <br>

## 使用方法 - How To Use
### ダイジェスト - Overview
```py
from Compy import MCommand
MC = MCommand()
MC.Run()
```
### 解説
* `Compy.py`をプロジェクトに追加します．
* `main`ファイルに以下のコードように記述し本コンソールクラスモジュールをインポートします．
```py
from Compy import MCommand
```
* インスタンス化を行います．
```py
MC = MCommand()
```
* 以下の関数を実行する事で，コンソール機能がアクティブになります．
```py
MC.Run()
```

## クラス - Classes
```py
class MCommand(object):
class MStd(MModule):
class MModule(object):
```

## 属性 - attribute

* ```class MCommand(object):```
```py
Modules:List[MModule] = []
DefaultCommands:List[str] = ["help","quit"]
ModuleSprt:str = "."
SprtInArgs:str = ","
```

* ```class MStd(MModule):```
```py
self.ModuleName = "std"
self.Commands = ["print","help"]
```

* ```class MModule(object):```
```py
ModuleName:str = "module"
Commands:List[str] = []
```

## メゾット(ユーザが実行可能)
* ```class MCommand(object):```
```py
def Run(self) -> void:
def DecodeArgs(self,words:str) -> List[str]:
def IncludeNewModule(self,module:MModule) -> void:
def ShowAllModuleCommandInfo(self) -> void:
def ShowAllDefaultCommands(self) -> void:
def ExecuteCommand(self,args:List[str]) -> void:
```

* ```class MStd(MModule):```
```py
none
```

* ```class MModule(object):```
```py
none
```

## イベント(ユーザによる実行は不可．定義のみが可能)
* ```class MCommand(object):```
```py
none
```

* ```class MStd(MModule):```
```py
def __init__(self) -> void:
def ExecuteCommand(self, args: List[str]) -> void:
```

* ```class MModule(object):```
```py
def __init__(self) -> void:
def ExecuteCommand(self,args:List[str]) -> void:
def ShowHelp(self) -> void:
```
