# Black Metal Cat Bot

Black Metal Cat Bot for Telegram.

## Build Status
[![Build Status](https://travis-ci.com/Evalle/bm-cat.svg?branch=master)](https://travis-ci.com/Evalle/bm-cat)

## Whoami

<img src="https://user-images.githubusercontent.com/2839811/47450333-4589fb80-d7c5-11e8-85e9-9d242fc01063.jpg" alt="BM cat" width="200" height="200">  

- Telegram Bot
- Written in Python 3
- you can ask me for some new black metal album via "BM!" message
- I will search the YouTube channels ([Black Metal Promotion](https://www.youtube.com/channel/UCzCWehBejA23yEz3zp7jlcg) and [Atmospheric Black Metal](https://www.youtube.com/channel/UCDLkzWN1rHY4eYkGnVruHVw))
- ... and I will paste the link to the new black metal album into Telegram Channel
- ... together with a funny random Black Metal quote, like *"The problem with most Norwigian bands is that their singers sound like Popay"* - **Cronos from Venom shared his thoughts in 1999**, see more [here](https://steemit.com/music/@worldofmusic/black-metal-most-creepy-quotes)

## Quickstart guide

### Prerequisites

- `python` version 3.7+
- `pip3` version 18.1+
- `docker` version 18.06.1-ce+

### Environment Variables

Name                        | Description
----------------------------|--------------------------------------------------------------------------------------
BM_CAT_SSL_CERTIFICATE_PATH | The path to a SSL certificate inside of a container (for example: `/etc/ssl/certs/public.pem`)
BM_CAT_PRIVATE_KEY_PATH     | The path to a private key (for example: `/etc/ssl/private/privkey.pem`)
PORT                        | The port on which container should run (container port), (for example: `5000`)
BM_CAT_HOST                 | The name of the host on which BM-cat bot is running (for example: `example.com`)
BM_CAT_PORT                 | The host port (for example: `8443`)
BM_CAT_API_KEY              | Telegram API KEY (see more [here](https://core.telegram.org/api/obtaining_api_id))
BM_YOUTUBE_API_KEY          | YouTube API KEY (see more [here](https://developers.google.com/youtube/v3/getting-started))

### Installation

1. Clone this repository and change the current directory to `bm-cat`

    ```bash
    git clone https://github.com/Evalle/bm-cat.git
    ```

1. Install all python dependencies via:

    ```bash
    pip install -r requirements.txt
    ```

1. Generate self-signed certificate pair, (see more [here](https://core.telegram.org/bots/self-signed))

    ```bash
    openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 365 \
                -out public.pem \
                -subj "/C=US/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=YOURDOMAIN.EXAMPLE"
    ```

1. Build docker image

    ```bash
    docker build --build-arg BM_CAT_SSL_CERTIFICATE_PATH=/etc/ssl/certs/public.pem \
                 --build-arg BM_CAT_PRIVATE_KEY_PATH=/etc/ssl/private/privkey.pem \
                 --build-arg PORT=5000 --build-arg BM_CAT_HOST=example.com \
                 --build-arg BM_CAT_PORT=8443 \
                 --build-arg BM_CAT_API_KEY=<your_telegram_api_key> \
                 --build-arg BM_YOUTUBE_API_KEY=<your_youtube_api_key> \
                 -t bm-cat:0.0.1 .
    ```

1. Finally, run docker container

    ```bash
    docker run -d --restart=always --privileged -p 8443:5000/tcp bm-cat:0.0.1
    ```
