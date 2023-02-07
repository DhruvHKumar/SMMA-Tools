from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

def upload_video_to_youtube(video_file_path, video_title, video_description, video_category_id, video_keywords):
    try:
        # Authenticate and construct the YouTube API client
        credentials = Credentials.from_authorized_user_file("path/to/client_secret.json")
        youtube = build('youtube', 'v3', credentials=credentials)
        
        # Define video metadata
        video_metadata = {
            'snippet': {
                'title': video_title,
                'description': video_description,
                'categoryId': video_category_id,
                'tags': video_keywords.split(','),
                'status': {'privacyStatus': 'private'}
            }
        }
        
        # Call the YouTube API's videos.insert method to upload the video
        video_insert_response = youtube.videos().insert(
            part=','.join(video_metadata.keys()),
            body=video_metadata,
            media_body=video_file_path
        ).execute()
        
        return video_insert_response
    except HttpError as error:
        print(f"An HTTP error {error.resp.status} occurred: {error.content}")
        return error
