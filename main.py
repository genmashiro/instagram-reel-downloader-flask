from flask import Flask, request, render_template
import instaloader
import concurrent.futures
from pathlib import Path

app = Flask(__name__)
L = instaloader.Instaloader()

# Define function to download reel
def download_reel(reel_url):
    try:
        post = instaloader.Post.from_shortcode(L.context, reel_url.split("/")[-2])
        L.download_post(post, target=str(Path(post.owner_username)))

        # Delete all files except .mp4 in the post.owner_username directory
        for file in Path(post.owner_username).glob('*'):
            if not file.name.endswith('.mp4'):
                file.unlink()

        return True
    except Exception as e:
        print(f"Error downloading reel: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reel_urls = request.form['urls'].split('\n')
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(download_reel, reel_urls))
        if all(results):
            return render_template('success.html')
        else:
            return render_template('error.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
