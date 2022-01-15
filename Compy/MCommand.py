from typing import NoReturn as void
from typing import List

#�R�}���h�Ƀ��W���[����g�ݍ��ވׂ̊g���\�Ȋ��N���X
class MModule(object):
    #���W���[���̖��́D���W���[�����Ăяo���ۂ̃R�}���h�ɂȂ�܂��D
    ModuleName:str = "module"
    #���W���[���̋@�\�R�}���h�ꗗ
    Commands:List[str] = []

    def __init__(self) -> void:
        pass

    #(�C�x���g)���W���[���̃R�}���h�����s���܂��D
    def ExecuteCommand(self,args:List[str]):
        pass

    #(�C�x���g)���W���[���̃R�}���h�ꗗ��\�����܂��D
    def ShowHelp(self):
        print("----------Commands----------")
        for cmd in self.Commands:
            print(self.ModuleName + 
                  "." +
                  cmd)
        return

#���N���X����p���ς݂̕W���̃R�}���h���W���[��
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

#�R�}���h�@�\��񋟂���ׂ̃N���X�D
#���̋@�\���N������ƁC�������[�v�ɂȂ�ׁC�����ɑ��̏������s���Ȃ�Δ񓯊������Ŏ��s����ׂ��ł��D
class MCommand(object):
    Modules:List[MModule] = []
    DefaultCommands:List[str] = ["help","quit"]
    ModuleSprt:str = "."
    SprtInArgs:str = ","

    def __init__(self) -> void:
        newmodule = MStd()
        self.IncludeNewModule(newmodule)
        return

    #��������s����ƁC���[�U���I���������s���܂ŌJ��Ԃ���܂��D
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