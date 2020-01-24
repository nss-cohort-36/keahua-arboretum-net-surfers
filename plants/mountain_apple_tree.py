from .plant import Plant
from interfaces.lives_in import IMountain

class Mountain_Apple_Tree(Plant, IMountain):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Partial", 17, "High")
        IMountain.__init__(self)