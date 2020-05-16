#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides

    def inputSides(self):
        self.sides = [float(input("Enter the side: " )) for i in range(self.n)]

            
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a,b,c = self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
        
t=Triangle()
t.inputSides()
t.findArea()


# In[ ]:




