# Whatsapp message count per member

This simple scripts shows the count of messages sent by each member, sorted by the number of messages sent.

## Usage
Export the chat via your phone, click on the group chat and select "export chat". Select without media. It will be a .zip file, containing a file _chat.txt. Copy that file in the cwd. On that same folder, run
```bash
git clone https://github.com/nicolello-dev/whatsappMessageCount.git .
```
Then, to run the script, run
```bash
python3 main.py
```
If it doesn't work, `python` by itself might.
```bash
python main.py

```
If this still doesn't, make sure you have Python installed on your machine.