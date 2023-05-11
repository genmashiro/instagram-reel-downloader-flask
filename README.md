# Instagram Reel Downloader v2

This is a Flask-based web application that allows you to download Instagram reels. Simply provide a list of reel URLs, and the application will download the reels to your local machine.

## Requirements

- Python 3.x
- Instaloader
- Flask
- pathlib
- concurrent.futures

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/oxygenta/instagram-reel-downloader-flask.git
   ```

2. Install the required dependencies:

   ```bash
   pip3 install instaloader flask pathlib concurrent.futures
   ```

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script with the following command:

   ```bash
   python main.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`.
4. Enter the Instagram reel URLs when prompted, with each URL on a new line.
5. Click the "Download" button to start the download process.
6. After the download completes, the application will display a success message or an error message if any downloads fail.

## Customization

- You can modify the `max_workers` value in the `ThreadPoolExecutor` to adjust the number of concurrent downloads.

## Disclaimer

This script is intended for personal use only. Make sure to respect the intellectual property rights of others when downloading Instagram content.

