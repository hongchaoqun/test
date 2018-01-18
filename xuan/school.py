import json

class School:
    def __init__(self,locale):
        self.course = {"course_name":"",'cycle':'','price':'','locale':locale}
        self.p_class={}
    def create_course(self):
        city = raw_input("place choose your city:\n")
        self.course['locale'] = city

        if city=='shanghai':
            self.course['course_name'] = 'go'
        else:
            while True:
                course_name = raw_input("place choose your course:\n")
                if course_name!='go':
                    break
                print "no go in beijing"
            self.course['course_name'] = course_name

        price=raw_input("place choose the price of course:\n")
        self.course['price'] = price

        cycle=raw_input("place choose the cycle of course:\n")
        self.course['cycle'] = cycle

        print 'course create success'

    def create_class(self):
        pass
        
        

        
            
a=School('beijin')
        
        
        


