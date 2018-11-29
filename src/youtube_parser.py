from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def load_videos(api_key, channels):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api_key)

    videos = {}
    for channel in channels:
        videos.update(_get_channel_videos(youtube, channel))

    return videos


def _get_channel_videos(youtube, channel_id):
    videos = {}

    page_token = ''
    while True:
        try:
            search_response = _execute_request(youtube, channel_id, page_token)
        except HttpError as e:
            print(
                'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
            break

        videos.update(_parse(search_response))

        if 'nextPageToken' not in search_response:
            break
        else:
            page_token = search_response['nextPageToken']

    return videos


def _execute_request(youtube, channel_id, page_token=''):
    return youtube.search().list(
        part='id,snippet',
        maxResults=50,
        channelId=channel_id,
        pageToken=page_token).execute()


def _parse(search_response):
    videos = {}
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video = {
                'Id': search_result['id']['videoId'],
                'Title': search_result['snippet']['title'],
                'PublishedAt': search_result['snippet']['publishedAt'],
                'ChannelId': search_result['snippet']['channelId']
            }
            videos[video['Id']] = video
    return videos
