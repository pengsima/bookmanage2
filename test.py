# 类一旦重写__new__方法,该类的实例化由__new__来控制,__init__会失效
class A:

    def __init__(self,name):
       self.name=name
       pass
    def __new__(cls, name,*args, **kwargs):
        cls.name = name

        obj = object.__new__(cls)
        # 先利用object.__new__开辟了一个对象内存空间,然后赋予属性实例化
        return  obj
#下面的的a其实是A元类实例化出来的,即a就是A这个类本身
#把__new__写在某个类里面就是要自定义这个类


a= A('小胖')
print(A.__dict__,a.__dict__)