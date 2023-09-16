#!/usr/bin/env python3

#class Book:
    #def __init__(self,title,page_count):
       # if not isinstance(page_count, int):
           # raise ("page_count must be an integer")
        #self.title = title
       # self.page_count = page_count


class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

  
    def page_count(self):
        return self._page_count

   
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value


      





