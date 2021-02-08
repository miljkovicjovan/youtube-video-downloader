from pytube import YouTube 

link = input("Enter link of video: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length,"seconds")
print("Ratings: ", yt.rating)


ys = yt.streams.get_highest_resolution()
ys.download()