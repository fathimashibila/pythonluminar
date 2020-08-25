#same method name but different number of arguments
class Math:
    def add(self):
        num1=15
        num2=15
        print(num1+num2)

    def add(self,num1,num2):
        print(num1+num2)

    def add(self,num1):    #only support last method otherwise error
        num2=4
        print(num1+num2)
m=Math()
m.add(4)
