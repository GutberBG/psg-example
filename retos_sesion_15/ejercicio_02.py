class FrutaNoValidaError(Exception):
    pass
class Canasta:
    def __init__(self):
        self.frutas = []
    def agregar_fruta(self, fruta):
        frutas_permitidas = ['🍅', '🍇', '🍈', '🍉', '🍊', '🍌', '🍍', '🍑']
        if fruta not in frutas_permitidas:
            raise FrutaNoValidaError("La fruta no es válida")
        self.frutas.append(fruta)
class CanastaFrutas:
    def __init__(self):
        self.canasta = Canasta()
    def agregar_fruta(self, fruta):
        try:
            self.canasta.agregar_fruta(fruta)
        except FrutaNoValidaError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e) 
        else:
            print("Fruta agregada con éxito:", fruta)
