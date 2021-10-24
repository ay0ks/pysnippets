# author: Dimitriy i0x <annihilation.ga>
# feel free to modify or copy this code 
# but also specify credits (link to this repo or file)

def __e(obj,n,v):obj[n]=v
def __raise(e):raise e
___e,__,___,__c,__p,__if,___join=(lambda obj,n,v:setattr(obj,n,v)),(lambda ret,*argc:ret),(lambda *argc:0),(lambda obj,n:___e(globals(),obj,{**obj,n:""})),(lambda obj:print(obj)),(lambda*__:__[0]if __[1]else __[2]),(lambda a:[a[0],a[1]])
__import=type("__import",(),{"__init__":lambda self:None,"__lshift__":lambda self,mod:__(self,___e(self,"mod",mod),__e(globals(),mod,__import__(mod))),"__lt__":lambda self,sub:__(self,__e(globals(),sub,getattr(__import__(getattr(self,"mod")),sub)))if type(sub)==str else[__(self,__e(globals(),sub_,getattr(__import__(self.mod),sub_)))for sub_ in sub]})()
__include=type("__include",(),{"__init__":lambda self:None,"__lt__":lambda self,file:exec(open(file,"r").read())})()
__af=type("__af",(object,),{"__init__":(lambda self,code,ret_type,*arg_types:___(___(___(___e(self,"tfile",___join(tempfile.mkstemp(".S","assembly",os.getcwd()))),___(___e(self,"fd",getattr(self,"tfile")[0]),___e(self,"source",getattr(self,"tfile")[1]))),___(___(os.write(getattr(self,"fd"),code.encode("utf-8")),os.close(getattr(self,"fd"))),___e(self,"target",os.path.splitext(getattr(self,"source"))[0]),___(subprocess.check_call(["nasm",getattr(self,"source")]),os.unlink(getattr(self,"source"))))),___(___(___(___e(self,"binary",open(getattr(self,"target"),"rb").read()),os.unlink(getattr(self,"target"))),___(___e(self,"bin_len",len(getattr(self,"binary"))),___e(self,"code_buffer",create_string_buffer(4096*2+getattr(self,"bin_len"))))),___(___e(self,"addr",(addressof(getattr(self,"code_buffer"))+4096)&(~(4096-1))),memmove(getattr(self,"addr"),getattr(self,"binary"),getattr(self,"bin_len")))),___(___(___(___e(self,"mprotect",cdll.LoadLibrary("libc.so.6").mprotect),___e(self,"mp_ret",getattr(self,"mprotect")(getattr(self,"addr"),getattr(self,"bin_len"),4))),__if((lambda:__raise(OSError("Unable to change memory protection"))),getattr(self,"mp_ret"),0)),___(___e(self,"func",CFUNCTYPE(ret_type,*arg_types)(getattr(self,"addr"))),___e(self,"addr",getattr(self,"addr")),___e(self,"bin_len",getattr(self,"bin_len")))))),"__call__":(lambda self,*args:getattr(self,'func')(*args)),"__del__":(lambda self:__if(getattr(self,"mprotect")(getattr(self,"addr"),getattr(self,"bin_len"),3),hasattr(self,"mprotect"),0))});___(setattr(_af___e:=(lambda obj,n,v:setattr(obj,n,v)),"_af___e_",classmethod(_af___e)),setattr(_af___join:=___join,"_af___join",classmethod(_af___join)),setattr(_af__if:=__if,"_af__if",classmethod(_af__if)))
__asm=type("__asm",(),{"__init__":lambda self,ret_t:___e(self,"ret_type",ret_t),"__lt__":(lambda self,asm:__af("\n".join(asm),getattr(self,"ret_type")))})



__import <<"os"
__import <<"tempfile"
__import <<"subprocess"
__import <<"ctypes" <(
 "addressof", 
 "c_int", 
 "cdll", 
 "create_string_buffer", 
 "CFUNCTYPE",
 "memmove"
)

__asm(c_int) <(
  "BITS 64",
  "mov rax, rdi",
  "add rax, rsi",
  "ret"
)
