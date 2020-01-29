from pytube import YouTube
import os

class download:
    def setUp(self, url):
        self.yt = YouTube(url)
        self.createDir()
        self.description()
    def createDir(self):
        try:
            os.mkdir('./Download')
        except FileExistsError as e:
            print('Pasta já criada!')

    def description(self):
        print(f' -- Title: {self.yt.title}')
        print(f' -- Author: {self.yt.author}')
        import ipdb; ipdb.set_trace()
    
    def loading(self):
        self.yt.streams.get_by_itag(140).download('./Download')
        
        
link = input('Digite o link para download: ')
d = download()
d.setUp(link)
