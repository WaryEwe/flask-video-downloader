from flask import Flask, render_template, request, redirect, send_from_directory
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    link = request.form['url_for']
    try:
        yt = YouTube(link)
        mp4_stream = yt.streams.filter(file_extension='mp4').first()
        video_path = f"downloads/{yt.title}.mp4"
        mp4_stream.download(video_path)
        return send_from_directory(
            os.path.dirname(video_path),
            os.path.basename(video_path),
            as_attachment=True
        )
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
