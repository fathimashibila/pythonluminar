class parent:
    def m1(self):
        print("inside parent1")
                                  #base>>child>>subchild

class child(parent):
    def m2(self):
        print("inside child")


class subchild(child):
    def m3(self):
        print("inside subchild")

sub=subchild()
sub.m3()
sub.m2()
sub.m1()

ch=child()
ch.m2()
ch.m1()

p=parent()
p.m1()





