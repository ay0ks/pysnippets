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

___assembly=type("___assembly",(object,),{
 "__init__":(lambda self,asm:
  ___rmulti(None,
  ___multi(
  ___multi(
  ___assign(self, "temp", ___join(tempfile.mkstemp(".S","temp", os.getcwd()))),
  ___assign(self, "source", getattr(self, "temp")[1]),
  ___assign(self, "file", __s := open(getattr(self, "source"), "wb")),
  ),
  ___multi(
  getattr(self, "file").write(asm.encode("utf-8")),
  getattr(self, "file").close(),
  ),
  ___multi(
  ___assign(self, "status", subprocess.check_output(f"nasm {getattr(self, 'source')}", shell=True)),
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
__asm=type("__asm",(),{
 "__init__":(lambda self:None),
 "__lt__":(lambda self,asm:
  ___assembly(asm if type(asm) is str else '\n'.join(asm))
 )
})()


___import <<"os"
___import <<"tempfile"
___import <<"subprocess"

__asm <("""

""")
