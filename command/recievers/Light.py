class Light():
    status = ""
    
    def light_on(self):
        self.status = "On"
        print(self.status)

    def light_off(self):
        self.status = "off"
        print(self.status)