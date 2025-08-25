class tablero:
    def __init__(self):
        self.contenedor = [
            [],[],[],[],[],[],  [],[],[],[],[],[],
            [],[],[],[],[],[],  [],[],[],[],[],[], 
        ]
    
    def tablero_inicial(self):
        self.contenedor[0] = ["blanco"] * 2
        self.contenedor[5] = ["negro"] * 5
        self.contenedor[7] = ["negro"] * 3
        self.contenedor[11] = ["blanco"] * 5
        self.contenedor[12] = ["negro"] * 2
        self.contenedor[17] = ["blanco"] * 5
        self.contenedor[19] = ["blanco"] * 3
        self.contenedor[23] = ["negro"] * 5



