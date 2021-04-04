def python():
    width = 80
    text = "sam and eggs"


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep

    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

# with open("menu", mode='w') as menu:

#call the function

print(center_text("spam and eggs"))
print(center_text("spam, spoam and eggs"))
print(center_text("12"))
print(center_text("spam, spam, spam and eggs"))
print(center_text("first", "second", "Third", sep=":"))



