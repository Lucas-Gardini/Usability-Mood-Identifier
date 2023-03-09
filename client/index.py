import socketio
from utils.colors import bgcolor
from recognizer import Recognizer


class Client:
    sio = None
    recognizer = None
    connected = False

    def __init__(self):
        self.recognizer = Recognizer()
        self.sio = socketio.Client()

        @self.sio.event
        def message(data):
            print('I received a message!')

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
            print(bgcolor.OKCYAN + 'Disconectado' + bgcolor.ENDC)

        print(bgcolor.OKCYAN + 'Aguardando conexão...' + bgcolor.ENDC)

    def connect(self, address):
        try:
            self.sio.connect(address)
            return True
        except:
            print(bgcolor.FAIL + 'Não foi possível conectar ao servidor' + bgcolor.ENDC)
            return False

    def disconnect(self):
        return self.sio.disconnect()

    def emit(self, event, message):
        return self.sio.emit(event, message)

    def startRecognition(self, videoPath):
        self.recognizer.recognize(videoPath)
