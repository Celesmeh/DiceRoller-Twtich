# Import library and create instance of REST client.
from Adafruit_IO import Client, Feed

aio = Client('Celesmeh', 'aio_zoXp53WTh0Ayp7iOtSfuTco9lQmN')

# Get list of feeds.
feeds = aio.feeds()

print(feeds)
