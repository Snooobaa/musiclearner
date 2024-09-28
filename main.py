import yt_dlp

def download_audio(youtube_url):
    """Downloads audio from a YouTube video and converts it to MP3 format.
    
    Args:
        youtube_url (str): The URL of the YouTube video to download audio from.
    
    Returns:
        None: This function doesn't return anything, but saves the audio file locally.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Example usage
download_audio('https://www.youtube.com/watch?v=9bZkp7q19f0')