from pytube import YouTube
import os

link = input("enter the youtube link: ")
resolution = input("enter resolution or press enter for default: ")
download_folder = os.path.expanduser("~")+"/Downloads/"
print("="*50)
print("downloading to Downloads folder")

stream = YouTube(link).streams 
if "p" in resolution:
    pass
else:
    resolution += 'p'
removed = ''
for i in resolution:
    if i.isdigit():
        removed += i
print("downloding...")
if resolution == '':
    try:
        video = stream.filter(res='720p',progressive=True, file_extension='mp4').first()
    except:
        video = YouTube(link).streams.filter(res='144p',progressive=True, file_extension='mp4').first()
        
elif int(removed) > 720:
    print("Audio may not be downloaded in this resolution")
    try:
        video = stream.filter(res=resolution).first()
    except:
        print("video not available in given resolution")
else:
    try:
        video = YouTube(link).streams.filter(res=resolution,progressive=True, file_extension='mp4').first()
    except:
        print("video not available in given resolution")
size = video.filesize
if size/1000 > 1:
    if size/1000000 > 1:
        if size/1000000000 > 1:
            print("video size: ",size/1000000000,"gb")
        else:
            print("video size: ",size/1000000,"mb")
    else:
        print("video size: ",size/1000,"kb")
else:
    print("video size: ",size,"bytes")
print("downloading...")
video.download(download_folder)
print("done")
