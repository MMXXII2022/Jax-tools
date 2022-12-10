

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print(bcolors.HEADER + "hello world")
# print(bcolors.OKBLUE + "hello world")
# print(bcolors.OKCYAN + "hello world")
# print(bcolors.OKGREEN + "hello world")
# print(bcolors.WARNING + "hello world")
# print(bcolors.FAIL + "hello world")
# print(bcolors.ENDC + "hello world")
# print(bcolors.BOLD + "hello world")
# print(bcolors.UNDERLINE + "hello world")


class Jax:
    """
    Jax tools is a module built in with some tools in which you can describe and name variables as an object
    You can refer to the object in many commands, some changing properties of the object and some outputting the properties.
    """
    def __init__(self, name, txt, help):
        Objects = []
        self.name = name
        self.txt = txt
        self.name_ = name
        self.txt_ = txt
        self.help = help
        Objects.append(self.name)
        print(bcolors.OKBLUE + str(Objects))
        print(bcolors.OKBLUE + "proper Jax Object registered with the following properties: " + bcolors.OKGREEN + "name: " + self.name + " and text: " + self.txt + '\n')
    def chName(self, NewName):
        self.name = NewName
        print(bcolors.OKCYAN + "Name has been changed to", NewName)
    def chText(self, NewTxt):
        self.txt = NewTxt
        print(bcolors.OKCYAN + "txt has been changed to", NewTxt)
    def Reset(self):
        self.name = self.name_
        print('Name has been reset to', self.name_)
        self.txt = self.txt_
        print('text has been reset to', self.txt_)

Var = ('txtRef')
Var2 = ('A small object to test')


Obj = Jax('Test', Var, Var2)
Obj2 = Jax('Test1', 'Test', 'Help')

ib = "ob"
ib = "ob"


