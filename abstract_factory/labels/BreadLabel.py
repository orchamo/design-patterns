from labels.Labels import Labels


class BreadLabel(Labels):
    def print_label(self):
        return "Wheat flour, Water, Salt"
    
    def __str__(self):
        return "Wheat flour, Water, Salt"