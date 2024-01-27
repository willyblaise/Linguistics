import pytube


link = input("Please enter a link so we can get busy: ")
yt = pytube.YouTube(link)

print(yt)

print("Title:", yt.title)
print("Author:", yt.author)
print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
print("Number of views:", yt.views)
print("Length of video:", yt.length, "seconds")

yt.streams.get_highest_resolution().download("~/Videos")

print("Video successfullly downloaded from", link)
