def ascii_sum(text):

    vowels = ["a", "e", "i", "o", "u"]
    adds = 0

    for char in text:
        if char.isalpha() == False:
            pass
        elif char in vowels:
            adds -= ord(char)
        else:
            adds += ord(char)
    return adds

t = """Dealing with failure is easy: Work hard to improve. Success is also easy
to handle: You’ve solved the wrong problem. Work hard to improve."""
print(ascii_sum(t))

