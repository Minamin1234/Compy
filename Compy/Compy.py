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