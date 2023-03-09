from index import Client
import os

client = Client()


def startup():
    server = input("Server address: ")
    success = client.connect(server)

    if not success:
        startup()

    videoType = input("Video type (0: camera; 1: video): ")
    if (videoType == 0):
        # TODO:
        print("A FAZER")
    else:
        videoPath = input("Video path: ")

        # Verificar se o arquivo existe
        if not os.path.isfile(videoPath):
            print("Arquivo não encontrado")
            startup()

        client.startRecognition(videoPath)


startup()
