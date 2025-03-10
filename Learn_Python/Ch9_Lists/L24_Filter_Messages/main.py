def filter_messages(messages):
    # Initialize variables
    filtered_messages = []
    filter_count = []
    # For each message in the input list:
    for message in messages:
        # Split the message into a list of words using the .split() string method (see below for help).
        words = message.split()
        # Create a new empty list for all the non-bad words for this message.
        good_words = []
        # Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
        counter = 0
        # For each word in the message:
        for word in words:
            # If the word is dang, increment the counter
            if word == "dang":
                counter += 1
            # If it is not dang, add the word to the non-bad word list you created
            else:
                good_words.append(word)
        # Join the list of non-bad words into a single string using the .join() method (see below for help)
        sentence = " ".join(good_words)
        # Append the new clean message to the final list of filtered messages
        filtered_messages.append(sentence)
        # Append the count of bad words removed to its list
        filter_count.append(counter)
    return filtered_messages, filter_count
