#pip install emoji

import emoji

# Function to convert emoji to text
def emoji_to_text(input_text):
    return emoji.demojize(input_text)

# Example input with emoji
input_text = "I love programming! 😍💻👍"
# To Type emojis : Press Windows Key + . (period) or Windows Key + ; (semicolon)

# Convert emoji to text and display the result
converted_text = emoji_to_text(input_text)
print("Original text:", input_text)
print("Converted text:", converted_text)
