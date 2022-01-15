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

## ユーザ定義のモジュールを定義する - How to define user's module.
### 概要 - Overview
```py
import Compy
from typing import NoReturn as void
from typing import List


class NEWMODULE(Compy.MModule):
    def __init__(self):
        self.ModuleName = "newmodule"
        self.Commands = ["hello","foo"]
        return

    def ExecuteCommand(self,args: List[str]) -> void:
        if args[1] == self.Commands[0]:
            print("Hello World!")
        elif args[1] == self.Commands[1]:
            print("foofoofoofoofoo")
        return

newmodule = NEWMODULE()
CmdDev = MCommand()
CmdDev.IncludeNewModule(newmodule)

CmdDev.Run()
```
### 解説
ユーザ定義のモジュールを定義するには`MModule`クラスから継承します．<br>
以下のコードが必ず記述すべき内容です．<br>
```py
import Compy
from typing import NoReturn as void
from typing import List

class NEWMODULE(Compy.MModule):
    def __init__(self):
        self.ModuleName = ""
        self.Commands = [""]
        return

    def ExecuteCommand(self,args: List[str]) -> void:
        return
```
今回は`NEWMODULE`という名称のモジュールを定義すると仮定します．<br>
`hello`コマンド，`foo`コマンドを定義し，"Hello World!"と"foofoofoofoofoo"をコンソール上に出力するモジュールを定義します．<br>
* `import Compy`に加えて，`from typing import NoReturn as void`と`from typing import List`を追加します．
```py
import Compy
from typing import NoReturn as void
from typing import List
```

* `Compy.MModule`クラスから継承します．<br>
```py
class NEWMODULE(MModule):
```

* コンストラクタを定義します．
```py
class NEWMODULE(Compy.MModule):
    def __init__(self):
```

* コンストラクタには属性(=メンバ変数)`self.ModuleName`と`self.Commands`を代入する処理を定義します．<br>
```py
    def __init__(self):
        self.ModuleName = "newmodule"
        self.Commands = ["hello","foo"]
        return
```

* コマンドには2つのキーワードを定義しました．<br>
```py
self.Commands = ["hello","foo"]
#self.Commands[0] -> "hello"
#self.Commands[1] -> "foo"
```

* イベント`def ExecuteCommand(self,args: List[str]) -> void:`を定義します．<br>
```py
    def ExecuteCommand(self,args: List[str]) -> void:
        if args[1] == self.Commands[0]:
            print("Hello World!")
        elif args[1] == self.Commands[1]:
            print("foofoofoofoofoo")
        return
```
コンソールから入力されたモジュール名，命令と引数の含まれるリスト`args`が渡されるので，そのリストから対象のコマンドの処理を定義します．<br>
ここでは，"Hello World!"と"foofoofoofoofoo"を表示させる処理を定義しました．
```py
        if args[1] == self.Commands[0]:
            print("Hello World!")
        elif args[1] == self.Commands[1]:
            print("foofoofoofoofoo")
        return
```

* 定義したモジュールクラスをインスタンス化します．<br>
```py
newmodule = NEWMODULE()
```

* コマンドクラス`MCommand`もインスタンス化します．<br>
```py
newmodule = NEWMODULE()
CmdDev = Compy.MCommand()
```

* `Compy.MCommand`の`IncludeNewModule()`を実行します．<br>
引数には先ほどインスタンス化した`newmodule`を指定します．<br>
```py
newmodule = NEWMODULE()
CmdDev = Compy.MCommand()
CmdDev.IncludeNewModule(newmodule)
```

* 普段通り，`Compy.MCommand`の`Run()`を実行します．<br>
```py
newmodule = NEWMODULE()
CmdDev = Compy.MCommand()
CmdDev.IncludeNewModule(newmodule)

CmdDev.Run()
```

### `help`コマンドが呼ばれた際の表示処理を定義する
先ほどのクラス定義で加えて`def ShowHelp(self) -> void:`を定義します．<br>
ここでは，コマンド毎の説明を出力しています．
```py
    def ShowHelp(self) -> void:
        print("----------Commands----------")
        for cmd in self.Commands:
            print(self.ModuleName + "." + cmd)
        return
```

### 最終結果
```py
import Compy
from typing import NoReturn as void
from typing import List

class NEWMODULE(Compy.MModule):
    def __init__(self):
        self.ModuleName = "newmodule"
        self.Commands = ["hello","foo"]
        return

    def ExecuteCommand(self,args: List[str]) -> void:
        if args[1] == self.Commands[0]:
            print("Hello World!")
        elif args[1] == self.Commands[1]:
            print("foofoofoofoofoo")
        return

    def ShowHelp(self) -> void:
        print("----------Commands----------")
        for cmd in self.Commands:
            print(self.ModuleName + "." + cmd)
        return

newmodule = NEWMODULE()
CmdDev = Compy.MCommand()
CmdDev.IncludeNewModule(newmodule)

CmdDev.Run()
```
