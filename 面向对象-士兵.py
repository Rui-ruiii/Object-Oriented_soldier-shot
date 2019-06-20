class Soldier:

    def __init__(self,name):

        self.name = name
        self.gun = None       #新兵没有枪
    def fire(self):
        #1.判断士兵是否有枪
        if self.gun == None:
            print("%s现在还没有枪，请尽快获取一把"%self.name)
            return
        else:
            #2.高喊口号
            print("%s大喊“冲鸭”"%self.name)
        #3.装填子弹
            self.gun.add_bullet(50)                                 #注意这里引用的装填和发射的方法！！！
        #4.射击                                                     #self.gun作为对象，调用封装好的方法
            self.gun.shoot()



class Gun:

    def __init__(self,model):      #这里需要定义出来的属性是型号，（即型号需要根据外界传入参数定义）
                                   # 因为初始化时枪内的子弹数量为0，这个是不需要外界定义就已知的
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):


        self.count = count
        self.bullet_count += count
        print("装填%d发子弹，当前余量%d发子弹"%(count,self.bullet_count))
    def shoot(self):

        self.shoot = 1
        if self.bullet_count < 1:
            print("当前%s子弹数量不足，请补充弹药后再进行射击"%(self.model))
            return
        else:
            self.bullet_count -= self.shoot
            print("每次开启发射%d颗子弹，当前余量%d发子弹"%(self.shoot,self.bullet_count))

ak47 = Gun("AK47")


maliao = Soldier("马里奥")
maliao.gun = ak47
maliao.fire()
print(maliao.gun)
