from typing import List
import pytube

def download_video(url: str, path: str):
    video = pytube.YouTube(url=url)
    stream = video.streams.get_highest_resolution()
    print(f"Downloading URL titled {video.title} with resolution {stream.resolution}")
    stream.download(output_path=path)


def batch_download(url_list: List[str], path: str):
    for url in url_list:
        download_video(url, path)

def download_playlist(url: str, path:str):
    p = pytube.Playlist(url)
    print(p.videos)
    #batch_download(p.videos,path)


#download_video("https://www.youtube.com/watch?v=nxFG5xdpDto&list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe&index=59&ab_channel=KrishNaik","C:\\Users\\sudhanthiran.b\\Desktop\\ML\\Krish\\ML Playlist")
download_playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9ah6WZeQtPbgVG4QrpESVaNA","C:\\Users\\sudhanthiran.b\\Desktop\\ML\\Krish\\ML Playlist")

# url = 'https://www.youtube.com/watch?v=onRYjVd5oHU&feature=youtu.be&ab_channel=iNeuroniNtelligence'
#
# download_video(url, '/sudhan')
# print(stream)
# stream.download(filename=video.title)


'''
for stream in video.streams:
    print(stream)

'''
