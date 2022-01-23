from typing import NoReturn as void
from typing import List
import math

#コマンドにモジュールを組み込む為の拡張可能な基底クラス
class MModule(object):
    #モジュールの名称．モジュールを呼び出す際のコマンドになります．
    ModuleName:str = "module"
    #モジュールの機能コマンド一覧
    Commands:List[str] = []
    #このモジュールを所有するコマンドデバイス(型はMCommand型)
    CommandDevice = None

    def __init__(self) -> void:
        pass

    #このモジュールを所有するコマンドデバイスを登録します．
    def SetCmdDev(self,newcmddev):
        self.CommandDevice = newcmddev
        return

    #(イベント)モジュールのコマンドを実行します．
    def ExecuteCommand(self,args:List[str]) -> void:
        pass

    #(イベント)コマンドの実行結果を出力しようとする際に呼ばれます。
    def PrintString(self,value) -> void:
        self.CommandDevice.PrintString(str(value))
        return

    #(イベント)モジュールのコマンド一覧を直接コンソール上に表示します．
    def ShowHelp(self) -> void:
        self.PrintString("----------Commands----------")
        for cmd in self.Commands:
            self.PrintString(self.ModuleName + 
                  "." +
                  cmd)
        return

    #(イベント)モジュールのコマンド一覧のリストを返します。
    def GetHelpList(self) -> List[str]:
        cmdlist:List[str] = []
        cmdlist.append("----------Commands----------")
        for cmd in self.Commands:
            cmdlist.append(self.ModuleName + "." + cmd)
        return cmdlist

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
            self.PrintString(args[2])
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
            if args[2] != "":
                val1 = float(args[2])
            if args[3] != "":
                val2 = float(args[3])

        if args[1] == self.Commands[0]:
            self.PrintString(abs(val1))
        elif args[1] == self.Commands[1]:
            self.PrintString(math.sin(val1))
        elif args[1] == self.Commands[2]:
            self.PrintString(math.cos(val1))
        elif args[1] == self.Commands[3]:
            self.PrintString(math.tan(val1))
        elif args[1] == self.Commands[4]:
            self.PrintString(math.radians(val1))
        elif args[1] == self.Commands[5]:
            self.PrintString(math.pow(val1,val2))
        elif args[1] == self.Commands[6]:
            self.PrintString(math.sqrt(val1))
        elif args[1] == self.Commands[7]:
            self.PrintString(max([val1,val2]))
        elif args[1] == self.Commands[8]:
            self.PrintString(min([val1,val2]))
        elif args[1] == self.Commands[9]:
            self.PrintString(math.pi)
        elif args[1] == self.Commands[10]:
            self.PrintString(math.e)
        elif args[1] == self.Commands[11]:
            self.ShowHelp()
        return


#コマンド機能を提供する為のクラス．
#この機能を起動すると，無限ループになる為，同時に他の処理も行うならば非同期処理で実行するべきです．
class MCommand(object):
    Version:str = "v5.0beta"
    Modules:List[MModule] = []
    DefaultCommands:List[str] = ["help","quit"]
    ModuleSprt:str = "."
    SprtInArgs:str = ","

    def __init__(self) -> void:
        newmodule = MStd()
        newmodule.SetCmdDev(self)
        self.IncludeNewModule(newmodule)
        mmath = MMath()
        mmath.SetCmdDev(self)
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

    #コンソールから入力された文字を解読し、
    #モジュール名・コマンド名・引数含むリストを返します。
    def DecodeArgs(self,words:str) -> List[str]:
        args:List[str] = [""]
        level:int = 0
        modulefrag:bool = False
        for w in words:
            if w == self.ModuleSprt and modulefrag == False:
                level = level + 1
                args.append("")
                modulefrag = True
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
            
    #指定した定義済みのモジュールを導入します。
    def IncludeNewModule(self,module:MModule) -> void:
        self.Modules.append(module)
        return

    #(イベント)このクラスで文字出力される際に呼ばれます。
    def PrintString(self,value) -> void:
        print(">>" + str(value))
        return

    #導入された全てのモジュールのコマンド一覧を表示します。
    def ShowAllModuleCommandInfo(self) -> void:
        for module in self.Modules:
            module.ShowHelp()
        return

    #このクラスの規定コマンド一覧を表示します。
    def ShowAllDefaultCommands(self) -> void:
        print("----------DefaultCommands----------")
        for cmd in self.DefaultCommands:
            self.PrintString(cmd)
        return

    #指定した引数でコマンドを実行します。
    def ExecuteCommand(self,args:List[str]) -> void:
        self.PrintString("")
        if args[0] == self.DefaultCommands[0]:
            self.ShowAllDefaultCommands()
            return

        for module in self.Modules:
            if args[0] == module.ModuleName:
                module.ExecuteCommand(args)
        return

    #コマンドから解読・コマンドの実行までの一連の処理を行います．
    def Execute(self,word:str):
        args:List[str] = self.DecodeArgs(word)
        self.ExecuteCommand(args)