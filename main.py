import os
from pytube import YouTube 

link = input("Enter link of video: ")
yt = YouTube(link)
os.system('cls')

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length,"seconds")
print("Ratings: ", yt.rating)

while True:
    choice = input('\nChoose download format (video/audio): ').upper()
    if choice == "VIDEO":
        video = yt.streams.get_highest_resolution()
        video.download()
        break
    elif choice == "AUDIO":
        audio = yt.streams.get_by_itag(140)
        audio.download()
        break
    else:
        print("Wrong input try again!")
        print("Enter 'audio' for audio only download")
        print("Enter 'video' for video download")