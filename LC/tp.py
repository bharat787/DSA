texts = []

    count = 0
    current_text = []
    for word in reply.split():
    if count + len(word) < (160 if len(texts) % 2 == 0 else (160-17)):
        current_text.append(word)
        count += (len(word) + 1)
    else:
        count = 0
        if len(texts) % 2 != 0):
            #odd-numbered text gets additional message...
            texts.append(" ".join(current_text) + "\nreply m for more")
        else:
            texts.append(" ".join(current_text))
    current_text = []