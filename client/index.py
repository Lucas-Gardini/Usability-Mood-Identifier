import socketio
from utils.colors import bgcolor
from recognizer import Recognizer


class Client:
    sio = None
    recognizer = None
    connected = False

    def __init__(self):
        print(bgcolor.OKCYAN + "Aguardando conexão..." + bgcolor.ENDC)

        self.sio = socketio.Client()
        self.recognizer = Recognizer(self.sio)

        @self.sio.event
        def message(data):
            print("I received a message!")

        @self.sio.event
        def connect():
            self.connected = True
            print(bgcolor.OKGREEN + "Conectado!" + bgcolor.ENDC)

        @self.sio.event
        def connect_error(data):
            print(bgcolor.FAIL + "A conexão falhou!" + bgcolor.ENDC)

        @self.sio.event
        def disconnect():
            self.connected = False
            print(bgcolor.OKCYAN + "Disconectado" + bgcolor.ENDC)

    def connect(self, address):
        try:
            self.sio.connect(address)
            return True
        except Exception as e:
            print(bgcolor.FAIL + "Não foi possível conectar ao servidor" + bgcolor.ENDC)
            print(bgcolor.FAIL + "Erro: " + str(e) + bgcolor.ENDC)
            return False

    def disconnect(self):
        return self.sio.disconnect()

    def emit(self, event, message):
        return self.sio.emit(event, message)

    def startRecognition(self, videoPath):
        return self.recognizer.recognize(videoPath)
