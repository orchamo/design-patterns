from labels.Labels import Labels


class TofuLabel(Labels):
    def print_label(self):
        return "Soy Beans, Water"
    
    def __str__(self):
        return "Soy beans, Water"