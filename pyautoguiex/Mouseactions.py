import pyautogui

# pyautogui.moveTo(960,540,duration=3)
# print(pyautogui.size())
# print(pyautogui.position())
# pyautogui.moveRel(xOffset=10,yOffset=30,duration=2)
# pyautogui.click(960,540,clicks=3,button="right",interval=1)
# pyautogui.doubleClick(960,540,button="right",interval=1)
# pyautogui.dragTo(960,540,duration=2)
# pyautogui.dragRel(25,300,duration=3)
#pyautogui.scroll(-1500,x=None,y=None)


# pyautogui.write('https://youtube.com/teluguvideosongs',interval=0.1)
# pyautogui.press('enter')

# a=257
# b=257
# print(hex(id(a)))
# print(hex(id(b)))


"""def reverse_with_spaces(input_str):
    words = input_str.split(' ')  # Split the input string by spaces
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    return ' '.join(reversed_words)  # Join the words with a single space

# Example usage:
input_str = "hello my name is bharath"
output_str = reverse_with_spaces(input_str)
print(output_str)"""


def reverse_with_spaces(input_str):
    words = input_str.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# Example usage
input_str = "hello my name is bharath"
output_str = reverse_with_spaces(input_str)
print(output_str)
