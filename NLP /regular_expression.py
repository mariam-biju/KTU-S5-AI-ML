import re

def replace_numbers_greater_than_10(text):
    # Replace numbers greater than 10 using a custom function
    def replacer(match):
        number = int(match.group())
        return "X" if number > 10 else str(number)

    # This regex finds all numbers in the text
    return re.sub(r'\d+', replacer, text)

# Example
sample_text = "I have 5 apples, 12 bananas, and 100 oranges."
result = replace_numbers_greater_than_10(sample_text)
print(result)
