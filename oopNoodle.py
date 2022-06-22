#oppNoodle.py

class Noodle:

    def __init__(self,sens,meat,topping,water,tauy):
        self.sens = sens # เส้น
        self.meat = meat # เนื้อวัว/หมู
        self.topping = topping # สด/เปื่อย/ลูกชิ้น
        self.water = water # แห้ง/น้ำ
        self.tauy = tauy #จำนวนชาม

    
    def poay(self): #โพย
        
        print(f'เส้น{self.sens} {self.meat} {self.topping} {self.water} {self.tauy}')#ออเดอร์ที่สั่ง
class SpecNoodle(Noodle):

    def __init__(self,sens,meat,topping,water,tauy,spec):
        super().__init__(sens,meat,topping,water,tauy)
        self.spec = spec
    
    def perm(self):
        print(f'เส้น{self.sens} {self.meat} {self.topping} {self.water} {self.tauy} {self.spec}')
'''
#สร้างตัวสื่บทอดคลาส
class SpecialStudent(Student):
    def __init__(self, name, age, gender,parent):
        super().__init__(name, age, gender) #เรียกตัวแปรของ Student
        self.parent = parent
    
    def hello(self,person = 'เพื่อน'):
        if person == 'เพื่อน':
            print('เฮ้ย! ว่าไงมีขนมกินไหม?')
        else:
            print('รีบหนีดีกว่า ไม่อยากคุย')
#การ Overwrite
    def sawatdee(self):
        print(f'หวัดดี ชื่อ{self.name}')
    
    def myfather(self):
        print('รุ้ไหม? ผมลูกใคร')
        print(f'ผมลูก{self.parent}')
        
'''

class ordering:

    def __init__(self,toa,gab):
        self.toa= toa #โต๊ะ
        self.gab = gab #ถุง
        
    def sang(self): #สั่ง
        if self.toa !=0:
            print(f'โต๊ะ{self.toa}')
        else:
            if self.gab !=0:
                print(f'ใส่ถุง{self.gab}')
            

if __name__ == '__main__':#สำหรับตรวจสอบว่าตอนนี้ไฟล์ที่กำลังรันอยู่เป็นตัวต้นฉบัับของมันหรือไม่ และจะถูกกันไว้ก่อนไม่ให้รันเวลาถูกเรียกเข้าไปใช้ในโปรแกรมอื่น
    ordering1 = ordering(1,0)
    Noodle1 = Noodle('เล็ก','หมู','สด','น้ำ',2)
    Noodle2 = Noodle('บะหมี่','หมู','เปืี่อย','แห้ง',1)
    SpecNoodle1 = SpecNoodle('ใหญ่','เนื้อ','สด','น้ำ',1,'ไม่งอก')
   
    print('----8:30 น.------')
    ordering1.sang()
    Noodle1.poay()
    Noodle2.poay()
    SpecNoodle1.perm()

    ordering2 = ordering(0,'LineMan')
    Noodle3 = Noodle('หมี่ขาว','หมู','สด','น้ำ',3)
    Noodle4 = Noodle('วุ้นเส้น','หมู','เปืี่อย','แห้ง',1)
    SpecNoodle2 = SpecNoodle('ใหญ่','เนื้อ','สด','น้ำ',1,'พิเศษ')
    print('----8:45 น.------')
    ordering2.sang()
    Noodle3.poay()
    Noodle4.poay()
    SpecNoodle2.perm()