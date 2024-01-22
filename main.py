from pymongo import MongoClient
import qrcode
from PIL import Image
import random

client = MongoClient(
    'mongodb+srv://swoyam:advaita@cluster0.pjlgcs3.mongodb.net/')
db = client['test']


n = int(input("Enter the number of Tickets codes you want to generate: "))
for i in range(n):
    # Generating the qr code
    num = random.randint(0, 9999999999999999999)
    num2 = random.randint(0, 9999999999999999999)
    qr = qrcode.make(f'{str(num2)}advaita2024{str(num)}')
    qr.save(f'./result/myQr{str(num)+str(num2)}.png')
    db.tickets.insert_one(
        {"qr": f'{str(num2)}advaita2024{str(num)}', "checkIn": False})
    # joining the two images
    img1 = Image.open(f'./result/myQr{str(num)+str(num2)}.png')
    img2 = Image.open("./pass.png")
    w1, h1 = img1.size
    w2, h2 = img2.size
    newHeight = max(h1, h2)
    newWidth = w1 + w2
    newImage = Image.new('RGB', (newWidth, newHeight), (255, 255, 255))
    newImage.paste(img1, (0, (newHeight-h1)//2))
    newImage.paste(img2, (w1, (newHeight-h2)//2))
    newImage.save(f'./output/myQr{str(num)+str(num2)}.png')
    print(f"Ticket {i+1} Generated")
