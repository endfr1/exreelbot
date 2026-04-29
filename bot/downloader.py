import yt_dlp
import time


def download_media(url):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': 'video_%(id)s.%(ext)s',
        'quiet': True,
        'noplaylist': False,
        'merge_output_format': 'mp4',
        'http_headers': {
            'User-Agent': 'Mozilla/5.0'
        }
    }

    last_error = None

    for _ in range(3):  # retry
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)

                if 'entries' in info:
                    files = []
                    for e in info['entries']:
                        if e:
                            files.append(ydl.prepare_filename(e))
                    return files
                else:
                    return [ydl.prepare_filename(info)]

        except Exception as e:
            last_error = e
            time.sleep(2)

    raise last_error