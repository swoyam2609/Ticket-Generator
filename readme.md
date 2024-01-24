# Ticket QR Code Generator
This Python script generates a specified number of ticket QR codes, saves them as PNG images, and stores the QR code data in a MongoDB database.

## Dependencies
- pymongo
- qrcode
- PIL
- random
- mongo
## How it works
- Connects to a MongoDB database using the MongoClient from the pymongo library.
- Asks the user to input the number of ticket codes they want to generate.
- For each ticket code:
    - Generates two random numbers and combines them with a string to create a unique QR code.
    - Saves the QR code as a PNG image in the `./result` directory.
    - Inserts a document into the tickets collection in the MongoDB database. The document contains the QR code and a `checkIn` field set to `False`.
    - Opens the QR code image and another image `(./pass.png)`, and combines them into a new image.
    - Saves the new image in the `./output` directory.
    - Prints a message indicating that the ticket has been generated.
## Usage
Run the script with Python 3. Make sure to have a MongoDB instance running and replace the `mongo.mongoURL` with your MongoDB connection string.
```py
python3 main.py
```


You will be prompted to enter the number of ticket codes you want to generate. After entering a number, the script will generate the ticket codes, save the images, and store the data in the database.

## Note
This script assumes that the `./result` and `./output` directories exist in the same location as the script. If they do not exist, you will need to create them, or modify the script to create them.