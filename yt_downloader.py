import os
import yt_dlp

def yt(url):
    
    ydl_opts = {
        
        'format' : 'best',
        'outtmpl': os.path.join("./downloads", '%(title)s.%(ext)s'),
    }

    print("-------Initializing connection and downloading-------")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f'An error oocured: {e}')


if __name__ == "__main__":
    link = input("Enter Youtube URL: ").strip()
    if link:
        yt(link)
    else:
        print("URL cannot be empty.")
