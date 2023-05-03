from index import Client
import os
from config import WS_SERVER

client = Client()


def startup():
    server = ""

    if WS_SERVER == "":
        server = input("Server address: ")
    else:
        server = WS_SERVER

    success = client.connect(server)

    if success:
        videoType = int(input("Video type (0: camera; 1: video): "))
        if videoType == 0:
            client.startRecognition(None)
        else:
            # Vídeos existentes disponíveis na pasta ./videos
            print("Videos available:")
            for filename in os.listdir("./client/videos"):
                if filename.endswith(".mp4"):
                    print(filename)

            videoPath = "./client/videos/" + input("Video path: ")

            # Verificar se o arquivo existe
            if not os.path.isfile(videoPath):
                print("Arquivo não encontrado")
                startup()
            else:
                client.startRecognition(videoPath)
                exit()


startup()
