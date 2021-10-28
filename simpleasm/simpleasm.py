# author: Dimitriy i0x <annihilation.ga>
# feel free to modify or copy this code 
# but also specify credits (link to this repo or file)

def __e(obj,n,v):obj[n]=v
def __del(obj):del obj
def __raise(e):raise e
__=(lambda ret,*argc:ret)
___=(lambda *argc:0)
___e=(lambda obj,n,v:setattr(obj,n,v))
___c=(lambda obj,n:___e(globals(),obj,{**obj,n:""}))
___p=(lambda obj:print(obj))
___if=(lambda*__:__[0]if __[1]else __[2])
___join=(lambda a:[a[0],a[1]])
__import=type("__import",(),{"__init__":lambda self:None,"__lshift__":lambda self,mod:__(self,___e(self,"mod",mod),__e(globals(),mod,__import__(mod))),"__lt__":lambda self,sub:__(self,__e(globals(),sub,getattr(__import__(getattr(self,"mod")),sub)))if type(sub)==str else[__(self,__e(globals(),sub_,getattr(__import__(self.mod),sub_)))for sub_ in sub],"__eq__":(lambda self,aln:___(__e(globals(),aln,globals()['sub']),__del(globals()['sub'])))})()
__include=type("__include",(),{"__init__":lambda self:None,"__lt__":lambda self,file:exec(open(file,"r").read())})()

__import <<"enum" <("Enum","unique","auto")

__SASM = type("__SASM", (object,), {
  "OP_CODES": type("OP_CODES", (), {
    "OP_PUSH": auto(),
    "OP_MOVE": auto(),
    "__metaclass__": unique,
    "__init__": (lambda self:None),
    "__list__": (lambda self:__(Enum("OP_CODES"," ".join([element for element in dir(self) if element.startswith("OP_")])),___())),
  })
})

program = [
    "move 20, eax",
    "push eax"
]

# WIP
