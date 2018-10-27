from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def load_videos(api_key, channels):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)

    videos = []
    for channel in channels:
        videos += _get_channel_videos(youtube, channel)

    return videos

def _get_channel_videos(youtube, channel_id):
    videos = []

    while True:
        try:
            search_response = _execute_request(youtube, channel_id)
        except HttpError as e:
            print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
            break

        videos += _parse(search_response)

        if 'nextPageToken' not in search_response:
            break

    return videos

def _execute_request(youtube, channel_id):
    return youtube.search().list(
        part='id,snippet',
        maxResults=50,
        channelId=channel_id
    ).execute()

def _parse(search_response):
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({'Id': search_result['id']['videoId'],
                           'Title': search_result['snippet']['title'],
                           'PublishedAt': search_result['snippet']['publishedAt']})
    return videos