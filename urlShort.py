import pyshorteners
def shorten(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)
if __name__ == '__main__':
    url = input("Enter the URL: ")
    shortUrl = shorten(url)
    print(shortUrl)