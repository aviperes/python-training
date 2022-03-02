from googleapiclient.discovery import build
import csv
api_key = 'AIzaSyA_wANK9uOX1S8RkJtP-5qaMnV2luqDraY'
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.search().list(
    part="snippet",
    q="NBA"+"מכבי חיפה",
    order='title',
    publishedAfter='2022-02-22T00:00:00Z',
)
response = request.execute()

# export to csv file:
with open("video_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(response)
print(response)

