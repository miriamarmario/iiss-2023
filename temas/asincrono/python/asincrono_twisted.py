from twisted.internet import reactor, protocol


class HarryPotterProtocol(protocol.Protocol):
    def connectionMade(self):
        print("¡Un nuevo mago ha llegado!")
        self.transport.write(b"Bienvenido a Hogwarts, mago!\n")
        self.transport.write(b"Cual es tu nombre?\n")

    def dataReceived(self, data):
        nombre = data.decode().strip()
        print(f"El mago se llama {nombre}")
        self.transport.write(b"Bienvenido a Hogwarts, " + nombre.encode() + b"!\n")
        self.transport.loseConnection()


class HarryPotterFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return HarryPotterProtocol()



print("Iniciando el servidor...")
reactor.listenTCP(8000, HarryPotterFactory())
reactor.run()
