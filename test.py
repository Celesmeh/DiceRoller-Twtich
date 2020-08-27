# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('aio_zoXp53WTh0Ayp7iOtSfuTco9lQmN')

# Get list of feeds.
feeds = aio.feeds()

# Print out the feed names:
for f in feeds:
    print('Feed: {0}'.format(f.name))

dataRoll = aio.receive('diceRoll').value
dataType = aio.receive('diceType').value
print(dataRoll, dataType)
