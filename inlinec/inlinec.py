# author: Dimitriy i0x <annihilation.ga>
# feel free to modify or copy this code 
# but also specify credits (link to this repo or file)

def ___dictappend(object_,name,value):
 object_[name]=value
def __delete(object_):
 del object_
def __raise(e):
 raise exception
___rmulti=lambda to_return,*argc:to_return
___multi=lambda*argc:0
___assign=lambda object,name,value:setattr(object,name,value)
___acopy=lambda object,name:___assign(globals(),object,{**object,name:""})
___print=lambda object:print(object)
___if=lambda do_if,condition,do_else:do_if if condition else do_else
___join=lambda to_join:[to_join[0],to_join[1]]
___aiter=lambda action=print,args=(),element="i",to_iter=globals():___rmulti([action(element,*args)for element in to_iter],___multi())
___iter=lambda element="i",to_iter=globals():___multi([element for element in to_iter])
___riter=lambda element="i",to_iter=globals():___rmulti([element for element in to_iter],___multi())
___import=type("__import",(),{"__init__":(lambda self:None),"__lshift__":(lambda self,module:___rmulti(self,___assign(self,"module",module),___dictappend(globals(),module,__import__(module)),)),"__lt__":(lambda self,submodule:___rmulti(self,___dictappend(globals(),submodule,getattr(__import__(getattr(self,"module")),submodule),)if type(submodule)==str else[___rmulti(self,___dictappend(globals(),submodule_,getattr(__import__(self.module),submodule_),),)for submodule_ in submodule],)),"__eq__":(lambda self,alternate:___multi(___dictappend(globals(),alternate,globals()["submodule"]),__del(globals()["submodule"]),)),},)()
___include=type("__include",(),{"__init__":(lambda self:None),"__lt__":(lambda self,file:exec(open(file,"r").read())),})()

___clang=type("___clang",(object,),{
 "__init__":(lambda self, c:
  ___rmulti(None,
  ___multi(
  ___multi(
  ___assign(self, "temp", ___join(tempfile.mkstemp(".cpp","temp", os.getcwd()))),
  ___assign(self, "source", getattr(self, "temp")[1]),
  ___assign(self, "file", __s := open(getattr(self, "source"), "wb")),
  ),
  ___multi(
  getattr(self, "file").write(c.encode("utf-8")),
  getattr(self, "file").close(),
  ),
  ___multi(
  ___assign(self, "status", subprocess.check_output(f"g++ -o a.out {getattr(self,'source')}", shell=True)),
  ___if(
   ___print(subprocess.check_output(getattr(self, "source")[:-2]).decode("utf-8")),
   getattr(self, "status") == 0,
   ___print(getattr(self, "status"))
  ),
  ),
  __s.close() and os.unlink(getattr(self, "source"))
  )
  )
 )
})
__c=type("__c",(),{
 "__init__":(lambda self: None),
 "__lt__":(lambda self, c:
  ___clang("\n".join(
    [
     c_ + "\n" if c_.endswith("{") else c_ 
     for c_ in c
    ]
   ) if type(c)==tuple else c)
  )
})()


__import <<"os"
__import <<"tempfile"
__import <<"subprocess"

__c <("""
#include <iostream>
#include <stdio.h>

class MyClass {
public:
  MyClass(std::string hello) {
    std::cout << hello << " World!" <<  std::endl;
  }
};

int main() {
  std::string hello = "Hello";
  MyClass cls(hello);
  
  return 0;
}
""")
