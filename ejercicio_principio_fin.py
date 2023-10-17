lista_archivo=["datos.txt", "reporte.xlsx", "imagen.jpg", "video.mp4", "audio.mp3"]
contadorD=0
contadorMP4=0
lista_d=[]
lista_mp4=[]

for item in lista_archivo:
    if item.startswith("d"):
        contadorD+=1
        lista_d.append(item)
    if item.endswith(".mp4"):
        contadorMP4+=1
        lista_mp4.append(item)


print("la cantidad de archivos que empiezan con D son :",contadorD, "los cuales son: {}".format(lista_d))
print("la cantidad de archivos que terminan con '.mp4' son :",contadorMP4, "los cuales son: {}".format(lista_mp4))