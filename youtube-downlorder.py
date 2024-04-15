from pytube import YouTube

# ダウンロードしたいYouTube動画のURLを指定
video_url = ""  # VIDEO_IDはダウンロードしたい動画のIDに置き換えてください

# YouTube動画をダウンロード
yt = YouTube(video_url)
video_title = yt.title

# 利用可能なすべてのストリームを出力
streams = yt.streams.filter(file_extension='mp4')
for stream in streams:
    print(stream)

# 動画ストリームをフィルタリングしてHD品質（720p以上）を取得
video_stream = yt.streams.filter(file_extension='mp4', resolution='720p').first()

# ダウンロードされたファイル名を設定
output_file = f"{video_title}.mp4"

# 動画をMP4フォーマットでダウンロード
if video_stream:
    video_stream.download(filename=output_file)
else:
    print("指定された解像度のストリームが見つかりませんでした。")
