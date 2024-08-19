# Automatic notification of a change in the status of your Steam account

Rename the file `⁡config.py.example` ⁡ -> ⁡`config.py`

Fill in the fields:

- `⁡timeout` ⁡ - time in seconds between account verification

- `tg_token` ⁡ - Bot token received in @BotFather

- `steam_acc` ⁡ - links to accounts (each account is separated by a comma)

- `chat_id` ⁡ - Your User ID (you can get it here - @username_to_id_bot)

Create and activate virtual environment (you can read here - [venv](https://docs.python.org/3/library/venv.html) ) 

Install dependencies using `⁡pip install -r requirements.txt`

Run the script with the command 
```⁡
python main.py
```
