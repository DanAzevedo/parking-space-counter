import cv2
import pickle

img = cv2.imread('park.png')
counters = []

# Percorremos no range de 69, pois se contarmos na imagem, há 69 vagas
# Recortamos vaga por vaga e guardamos para veirificação
for x in range(69):
    counter = cv2.selectROI('Parking Space Counter', img, False)
    cv2.destroyWindow('Parking Space Counter')
    counters.append((counter))

    for x, y, w, h in counters:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

with open('lot.pkl', 'wb') as archive:
    pickle.dump(counters, archive)
