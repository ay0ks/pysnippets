# author: Dimitriy i0x <annihilation.ga>
# feel free to modify or copy this code 
# but also specify credits (link to this repo or file)

def __e(obj,n,v):obj[n]=v
def __raise(e):raise e
___e,__,___,__c,__p,__if,___join=(lambda obj,n,v:setattr(obj,n,v)),(lambda ret,*argc:ret),(lambda*argc:0),(lambda obj,n:___e(globals(),obj,{**obj,n:""})),(lambda obj:print(obj)),(lambda*__:__[0]if __[1]else __[2]),(lambda a:[a[0],a[1]])
__import=type("__import",(),{"__init__":lambda self:None,"__lshift__":lambda self,mod:__(self,___e(self,"mod",mod),__e(globals(),mod,__import__(mod))),"__lt__":lambda self,sub:__(self,__e(globals(),sub,getattr(__import__(getattr(self,"mod")),sub)))if type(sub)==str else[__(self,__e(globals(),sub_,getattr(__import__(self.mod),sub_)))for sub_ in sub]})()
__include=type("__include",(),{"__init__":lambda self:None,"__lt__":lambda self,file:exec(open(file,"r").read())})()

__cf=type("__cf",(object,),{"__init__":(lambda self,c:__(None,___(___e(self,"tfile",tempfile.mkstemp(".cpp","temp",os.getcwd())),___e(self,"source",getattr(self,"tfile")[1]),___e(self,"f",__s:=open(getattr(self,"source"),"wb")),getattr(self,"f").write(c.encode("utf-8")),),___(___e(self,"sts",subprocess.check_output(f"g++ -o a.out {getattr(self,'source')}",shell=True)),__if(print(subprocess.check_output("a.out").decode("utf-8")),getattr(self,"sts")==0,getattr(self,"sts")),),os.unlink("a.out"),__s.close()and os.unlink(getattr(self, "source")),))})
__c=type("__c",(),{"__init__":lambda self:None,"__lt__":(lambda self,c:__cf("\n".join([c_+"\n"if c_.endswith("{")else c_ for c_ in c])if type(c)==tuple else c))})()


__import <<"os"
__import <<"tempfile"
__import <<"subprocess"

__c <("""
#include <iostream>
#include <stdio.h>

class MyClass {
public:
  MyClass(std::string negr) {
    std::cout << negr << " ultra nigger" <<  std::endl;
  }
};

int main() {
  std::string negr = "kot";
  MyClass cls(negr);
  
  return 0;
}
""")
