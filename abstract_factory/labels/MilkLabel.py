from labels.Labels import Labels


class MilkLabel(Labels):
    def print_label(self):
        return "100% Pesturised Milk"
    
    def __str__(self):
        return "100% Pesturised Milk"