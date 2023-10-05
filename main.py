with open('_chat.txt') as f:
    lines = f.readlines()

pplMess = {}

for line in lines:
    # timestamp is between two square brackets like so [9/14/23, 19:13:20]. If it doesn't start this way, ignore.
    # The above can be because of polls or other non-standard messages
    if line[0] != '[' or line[18] != ']':
        continue

    # Remove the time
    line = line[20:]
    # Name ends with :
    endName = line.find(':')
    name = line[:endName].replace('\u202f', ' ')
    if pplMess.get(name) is None:
        pplMess[name] = 1
    else:
        pplMess[name] += 1

sortedMessages = sorted(pplMess.items(), key=lambda item: item[1], reverse=True)

for name, messages in sortedMessages:
    print(f"{name}:{messages}")