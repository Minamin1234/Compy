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
    def ExecuteCommand(self,args:List[str]) -> str:
        pass

    #(イベント)コマンドの実行結果を出力しようとする際に呼ばれます。
    def PrintString(self,value) -> void:
        self.CommandDevice.PrintString(str(value))
        return

    #(イベント)モジュールのコマンド一覧を直接コンソール上に表示します．
    def ShowHelp(self) -> str:
        result:str = ""
        result += "----------Commands----------" + "\n"
        self.PrintString("----------Commands----------")
        for cmd in self.Commands:
            self.PrintString(self.ModuleName + 
                  "." +
                  cmd)
            result += self.ModuleName + "." + cmd + "\n"
        return result

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

    def ExecuteCommand(self, args: List[str]) -> str:
        result:str = ""
        if args[1] == self.Commands[0]:
            self.PrintString(args[2])
            result += args[2] + "\n"
        elif args[1] == self.Commands[1]:
            result = self.ShowHelp()
        return result

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

    def ExecuteCommand(self, args: List[str]) -> str:
        result:str = ""
        if len(args) >= 4:
            val1:float
            val2:float
            if args[2] != "":
                val1 = float(args[2])
            if args[3] != "":
                val2 = float(args[3])

        if args[1] == self.Commands[0]:
            self.PrintString(abs(val1))
            result = abs(val1)
        elif args[1] == self.Commands[1]:
            self.PrintString(math.sin(val1))
            result = math.sin(val1)
        elif args[1] == self.Commands[2]:
            self.PrintString(math.cos(val1))
            result = math.cos(val1)
        elif args[1] == self.Commands[3]:
            self.PrintString(math.tan(val1))
            result = math.tan(val1)
        elif args[1] == self.Commands[4]:
            self.PrintString(math.radians(val1))
            result = math.radians(val1)
        elif args[1] == self.Commands[5]:
            self.PrintString(math.pow(val1,val2))
            result = math.pow(val1,val2)
        elif args[1] == self.Commands[6]:
            self.PrintString(math.sqrt(val1))
            result = math.sqrt(val1)
        elif args[1] == self.Commands[7]:
            self.PrintString(max([val1,val2]))
            result = max([val1,val2])
        elif args[1] == self.Commands[8]:
            self.PrintString(min([val1,val2]))
            result = min([val1,val2])
        elif args[1] == self.Commands[9]:
            self.PrintString(math.pi)
            result = math.pi
        elif args[1] == self.Commands[10]:
            self.PrintString(math.e)
            result = math.e
        elif args[1] == self.Commands[11]:
            result = self.ShowHelp()
        return result


#コマンド機能を提供する為のクラス．
#この機能を起動すると，無限ループになる為，同時に他の処理も行うならば非同期処理で実行するべきです．
class MCommand(object):
    Version:str = "v6.0beta"
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
        module.SetCmdDev(self)
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
    def ShowAllDefaultCommands(self) -> str:
        result:str = ""
        print("----------DefaultCommands----------")
        result += "----------DefaultCommands----------" + "\n"
        for cmd in self.DefaultCommands:
            result += cmd + "\n"
            self.PrintString(cmd)
        return result

    #指定した引数でコマンドを実行します。
    def ExecuteCommand(self,args:List[str]) -> str:
        result:str = ""
        self.PrintString("")
        if args[0] == self.DefaultCommands[0]:
            result = self.ShowAllDefaultCommands()
            return result

        for module in self.Modules:
            if args[0] == module.ModuleName:
                result = module.ExecuteCommand(args)
        return result

    #コマンドから解読・コマンドの実行までの一連の処理を行います．
    def Execute(self,word:str) -> str:
        args:List[str] = self.DecodeArgs(word)
        result:str = self.ExecuteCommand(args)
        return result