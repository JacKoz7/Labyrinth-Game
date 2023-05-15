class Player():
    def __init__(self, treasure, way35, cross):
        self.treasure = treasure
        self.way35 = way35
        self.cross = cross
    def print(self):
        print('wspolrzedne skarbu - ' + str(self.treasure))
        print(self.way35)
        print('wspolrzedne iksa - ' + str(self.cross))
    def return_treasure(self):
        x = self.treasure
        return x
    def return_way35(self):
        y =self.way35
        return y
    def return_cross(self):
        z = self.cross
        return z