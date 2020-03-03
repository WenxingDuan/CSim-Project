import random,time

class Role():
    def __init__(self,name='【角色】'):
        self.name=name
        self.life=random.randint(100,150)
        self.attack=random.randint(30,50)

class Knight(Role):
    def __init__(self,name='【圣光骑士】'):
        Role.__init__(self,name)
        self.life=self.life*5
        self.attack=self.attack*3

    def fight_buff(self,opponent,str1,str2):
        if opponent.name=='【暗影刺客】':
            self.attack=int(self.attack*1.5)
            print('【%s】【圣光骑士】对【%s】【暗影刺客】说：“让无尽光芒制裁你的堕落！”'%(str1,str2))

class Assassin(Role):
    def __init__(self,name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life=self.life*3
        self.attack=self.attack*5
        
    def fight_buff(self,opponent,str1,str2):
        if opponent.name=='【精灵弩手】':
            self.attack=int(self.attack*1.5)
            print('【%s】【暗影刺客】对【%s】【精灵弩手】说：“主动找死，就别怪我心狠手辣。”'%(str1,str2))

class Bowman(Role):
    def __init__(self,name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life=self.life*4
        self.attack=self.attack*4

    def fight_buff(self,opponent,str1,str2):
        if opponent.name=='【圣光骑士】':
            self.attack=int(self.attack*1.5)
            print('【%s】【精灵弩手】对【%s】【圣光骑士】说：“骑着倔驴又如何？你都碰不到衣服。”'%(str1,str2))

class Game:
    def __init__(self):
        self.players=[]
        self.enemies=[]
        self.score=0
        self.i=0

        self.game_start()
        self.born_role()
        self.show_role()
        self.order_role()
        self.pk_role()
        self.show_result()

    def game_start(self):
        print('------------ 欢迎来到“炼狱角斗场” ------------')
        print('在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。')
        print('鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！')
        print('今日，只要你【你的队伍】能取得胜利，你将获得一笔够花500年的财富。')
        time.sleep(2)
        print('将随机生成【你的队伍】和【敌人队伍】！')
        input('\n狭路相逢勇者胜，请按任意键继续。\n')

    def born_role(self):
        for i in range(3):
            self.players.append(random.choice(Knight(),Assassin(),Bowman()))
            self.enemies.append(random.choice(Knight(),Assass(),Bowman()))

    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('【我方】%s 血量：%s 攻击：%s'%
            (self.players[i].name,self.players[i].life,self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('【敌方】%s 血量：%s 攻击：%s'%
            (self.enemies[i].name,self.enemies[i].life,self.enemies[i].attack))
        print('--------------------------------------------')

    def order_role(self):
        order_dict={}
        for i in range(3):
            order=int(input('你想将%s放在第几个上场？（输入数字1~3）'%self.players[i].name))
            order_dict[str(order)]=self.players[i]
        self.players=[]
        for i in range(1,4):
            self.players.append(order_dict[i])
        print('\n你的队伍出场顺序是：%s、%s、%s'
        %self.players[0].name,self.players[1].name,self.players[2].name)
        print('敌人的队伍出场顺序是：%s、%s、%s'
        %self.enemies[0].name,self.enemies[1].name,self.enemies[2].name)

    def pk_role(self):
        for i in range(3):
            print('\n----------------- 【第%s轮】 -----------------'%(i+1))
            self.players[i].fight_buff(self.enemies[i],'我方','敌方')
            self.enemies[i].fight_buff(self.players[i],'敌方','我方')
            input('\n战斗双方准备完毕，请按回车键继续。')
            print('--------------------------------------------')

            while self.players[i].life>0 and self.enemies[i].life>0:
                self.enemies[i].life-=self.players[i].attack
                self.players[i].life-=self.enemies[i].attack
                print('我方%s 发起了攻击，敌方%s 剩余血量%s'%
                self.players[i].name,self.enemies[i].name,self.enemies[i].life)
                print('敌方%s 发起了攻击，我方%s 剩余血量%s'%
                self.enemies[i].name,self.players[i].name,self.players[i].life)
                print('--------------------------------------------')
                time.sleep[1]
            #if self.players[i].life<=0 and self.enemies