class Singelton():

    instance = ""
    
    def instanciator(self):
        if self.instance == "":
           print("new")
           self.instance = Singelton()
        else:
            print("existing")
            return self.instance
        
    def hello(self):
        print ("hello")
    
# how to attend to Singelton which have one instance, while not assigning it to a variable.?
s= Singelton.instanciator()
