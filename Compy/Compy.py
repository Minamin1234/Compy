from typing import NoReturn as void
from typing import List
import math

#コマンドにモジュールを組み込む為の拡張可能な基底クラス
class MModule(object):
    #モジュールの名称．モジュールを呼び出す際のコマンドになります．
    ModuleName:str = "module"
    #モジュールの機能コマンド一覧
    Commands:List[str] = []

    def __init__(self) -> void:
        pass

    #(イベント)モジュールのコマンドを実行します．
    def ExecuteCommand(self,args:List[str]) -> void:
        pass

    #(イベント)モジュールのコマンド一覧を表示します．
    def ShowHelp(self) -> void:
        print("----------Commands----------")
        for cmd in self.Commands:
            print(self.ModuleName + 
                  "." +
                  cmd)
        return

#基底クラスから継承済みの標準のコマンドモジュール
class MStd(MModule):
    def __init__(self) -> void:
        self.ModuleName = "std"
        self.Commands = [
            "print",
            "help"
            ]
        return

    def ExecuteCommand(self, args: List[str]) -> void:
        if args[1] == self.Commands[0]:
            print(args[2])
        elif args[1] == self.Commands[1]:
            self.ShowHelp()
        return

class MMath(MModule):
    def __init__(self) -> void:
        self.ModuleName = "math"
        self.Commands = [
            "abs",
            "sin",
            "cos",
            "tan",
            "rad",
            "pow",
            "sqrt",
            "max",
            "min",
            "pi",
            "e",
            "help"
            ]
        return

    def ExecuteCommand(self, args: List[str]) -> void:
        if len(args) >= 4:
            val1:float
            val2:float
            print(args)
            if args[2] != "":
                val1 = float(args[2])
            if args[3] != "":
                val2 = float(args[3])

        if args[1] == self.Commands[0]:
            print(abs(val1))
        elif args[1] == self.Commands[1]:
            print(sin(val1))
        elif args[1] == self.Commands[2]:
            print(math.cos(val1))
        elif args[1] == self.Commands[3]:
            print(math.tan(val1))
        elif args[1] == self.Commands[4]:
            print(math.radians(val1))
        elif args[1] == self.Commands[5]:
            print(math.pow(val1,val2))
        elif args[1] == self.Commands[6]:
            print(math.sqrt(val1))
        elif args[1] == self.Commands[7]:
            print(max([val1,val2]))
        elif args[1] == self.Commands[8]:
            print(min([val1,val2]))
        elif args[1] == self.Commands[9]:
            print(math.pi)
        elif args[1] == self.Commands[10]:
            print(math.e)
        elif args[1] == self.Commands[11]:
            self.ShowHelp()
        return


#コマンド機能を提供する為のクラス．
#この機能を起動すると，無限ループになる為，同時に他の処理も行うならば非同期処理で実行するべきです．
class MCommand(object):
    Modules:List[MModule] = []
    DefaultCommands:List[str] = ["help","quit"]
    ModuleSprt:str = "."
    SprtInArgs:str = ","

    def __init__(self) -> void:
        newmodule = MStd()
        self.IncludeNewModule(newmodule)
        mmath = MMath()
        self.IncludeNewModule(mmath)
        return

    #これを実行すると，ユーザが終了処理を行うまで繰り返されます．
    def Run(self) -> void:
        while True:
            cmd:str = input()
            args:List[str] = self.DecodeArgs(cmd)
            self.ExecuteCommand(args)
            if args[0] == "quit":
                break
        return


    def DecodeArgs(self,words:str) -> List[str]:
        args:List[str] = [""]
        level:int = 0
        for w in words:
            if w == self.ModuleSprt:
                level = level + 1
                args.append("")
                continue
            elif w == self.SprtInArgs:
                level = level + 1
                args.append("")
                continue
            elif w == "(":
                level = level + 1
                args.append("")
                continue
            elif w == ")":
                level = level + 1
                args.append("")
                continue
            args[level] = args[level] + w
        return args
            
    def IncludeNewModule(self,module:MModule) -> void:
        self.Modules.append(module)
        return

    def ShowAllModuleCommandInfo(self) -> void:
        for module in self.Modules:
            module.ShowHelp()
        return

    def ShowAllDefaultCommands(self) -> void:
        print("----------DefaultCommands----------")
        for cmd in self.DefaultCommands:
            print(cmd)
        return

    def ExecuteCommand(self,args:List[str]) -> void:
        print("")
        if args[0] == self.DefaultCommands[0]:
            self.ShowAllDefaultCommands()
            return

        for module in self.Modules:
            if args[0] == module.ModuleName:
                module.ExecuteCommand(args)
        return