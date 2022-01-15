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
