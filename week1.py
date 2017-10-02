#first question
class user()
    def _init_(self,user_name,user_pin,user_profile):
        self.name=user_name
        self.pin=user_pin
        self.profile=user_profile

    def default(self):
        self.name="zjzk99"
        self.pin="a2358686b"
        self.profile="male"

    def custom(self,user_profile):
        self.profile=user_profile

#second question
class activity()
    def _init_(self,title,matter,data,num):
        self.title=title
        self.matter=matter
        self.data=data
        self.num=num

    def add_num(self,plus):
        self.num=num+"%s" % plus
        
    def reduce_num(self,minus):
        self.num=num-"%s" % minus

    def custom(self,matter):
        self.matter=matter

#third question
list=[1,2,3,4,5]
for item in range(6,11)：
    list.append(item)
list.remove(4)
print(list)

#forth question
dic={key:"Kai_Zhang",
    value:"10430213"
     }
print "key: %s" % dic.get("key")
print "value: %s" % dic.get("value")
