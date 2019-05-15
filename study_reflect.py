#类反射

class People:
     number_eye = 2

     def __init__(self,name,age):
         self.name = name
         self.age = age


if __name__ == '__main__':
    p = People('sanyue',24)
    print(People.number_eye)
    print(p.number_eye)
    print(p.name)

    #添加属性
    print(hasattr(People,"number_leg"))  #如果有返回True,没有就返回False，判断有没有这个属性
    print(hasattr(People, "number_eye"))

    setattr(People,"number_leg",2)    #添加类属性number_leg，，存在的就覆盖
    print(hasattr(People, "number_leg"))
    print(People.number_leg)

    setattr(p,"dance",True)    #添加类的实例属性 ，，存在的就覆盖
    print(p.dance)

    getattr(People,"number_leg")   #获取类属性的值
    getattr(p,"dance")             #获取实例属性的值

    delattr(p,"dance")     #删除实例属性d
    getattr(p,"dance")     #获取实例属性