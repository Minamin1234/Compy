from typing import NoReturn as void
from typing import List

class MModule(object):
    ModuleName:str = "module"
    Commands:List[str] = []

    def __init__(self) -> void:
        pass

    def ExecuteCommand(self,args:List[str]):
        pass

    def ShowHelp(self):
        print("----------Commands----------")
        for cmd in self.Commands:
            print(self.ModuleName + 
                  "." +
                  cmd)
        return

class MStd(MModule):
    def __init__(self) -> void:
        self.ModuleName = "std"
        self.Commands = [
            "print",
            "help"
            ]
        return

    def ExecuteCommand(self, args: List[str]):
        if args[1] == self.Commands[0]:
            print(args[2])
        elif args[1] == self.Commands[1]:
            self.ShowHelp()
        return

class MCommand(object):
    Modules:List[MModule] = []
    DefaultCommands:List[str] = ["help","quit"]
    ModuleSprt:str = "."
    SprtInArgs:str = ","

    def __init__(self) -> void:
        newmodule = MStd()
        self.IncludeNewModule(newmodule)
        return

    def Run(self) -> void:
        while True:
            cmd:str = input()
            args:List[str] = self.EncodeArgs(cmd)
            self.ExecuteCommand(args)
            if args[0] == "quit":
                break
        return


    def EncodeArgs(self,words:str) -> List[str]:
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