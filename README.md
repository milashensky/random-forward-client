# random-forward-client

My friend asked me for an automation to forward a random message from a channel to another channel. so here it is. not planning to host it anywhere yet, just a manual script.


## Install

1. install dependencies
```
pip install -r requirements.txt
```

2. populate .env.

`API_ID` and `API_HASH` are issued by telegram at https://my.telegram.org/apps.

`TO_CHANNEL` and `FROM_CHANNEL` can be invite links, or chat/channel ids.

`SESSION_PATH` file name/path to store session. if not specified, login will be prompted on each run.

## Run

run `./main.py` or `python3 ./main.py`