from googleapiclient.discovery import build
import csv

api_key = 'AIzaSyA_wANK9uOX1S8RkJtP-5qaMnV2luqDraY'
youtube = build('youtube', 'v3', developerKey=api_key)


# request = youtube.search().list(
#     part="snippet",
#     q="NBA"+"מכבי חיפה",
#     order="title",
#     publishedAfter='2022-02-22T00:00:00Z',
# )
# response = request.execute()


class YoutubeData:

    def get_videos(self, part, q, order, published):
        self.part = part
        self.q = q
        self.order = order
        self.published = published
        request = youtube.search().list(
            part=self.part,
            q=self.q,
            order=self.order,
            publishedAfter=self.published,
        )
        response = request.execute()


data = YoutubeData()
data.get_videos("snippet", "NBA", "title", "2022-02-22T00:00:00Z")
data.get_videos("snippet", "מכבי חיפה", "title", "2022-02-22T00:00:00Z")

# export to csv file:
# with open("video_data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(response)
# print(response)
