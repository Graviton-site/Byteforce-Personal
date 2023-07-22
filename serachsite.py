import json
import googleapiclient.discovery
item = input("What is the query")
with open(r"base/output.txt") as file:
    for item in file:
        api_service_name = "youtube"
        api_version = "v3"
        # ! AIzaSyDwSJT7QoOiI9I_NbcXLrrsd9JDtalBnCo <-- Production key
        DEVELOPER_KEY = 'AIzaSyDQkVnWcwpJ1zeVchO2VBBOHWN3tMbl3_Q'
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)
        request = youtube.search().list(
            part="id,snippet",
            type='video',
            q=str(item + 'basketball'),
            maxResults=1,

        )
        response = request.execute()
        print(response)
        youtubedict = {}
        jsondata = json.load(response)
        videoid = jsondata.items[0].id.videoId
        videotitle = jsondata.items[0].snippet.title
        videothumbnail = jsondata.items[0].snippet.thumbnails.default.url
        youtubedict.update(
            {f"id{item}": videoid},
            {f"title{item}": videotitle},
            {f"id{item}": videothumbnail}
        )
