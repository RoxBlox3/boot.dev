def filter_messages(messages):
    #Initialize variables
    filtered_messages = []
    filter_count = []
    # For each message in the input list:
    for message in messages:
    # Split the message into a list of words using the .split() string method (see below for help).
    # Create a new empty list for all the non-bad words for this message.
    # Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
    # For each word in the message:
    #     If the word is dang, increment the counter
    #     If it is not dang, add the word to the non-bad word list you created
    # Join the list of non-bad words into a single string using the .join() method (see below for help)
    # Append the new clean message to the final list of filtered messages
    # Append the count of bad words removed to its list
