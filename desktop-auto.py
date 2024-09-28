import pyautogui


# Move the mouse cursor to the specified coordinates
pyautogui.moveTo(500, 300)

# Click the left mouse button
pyautogui.click()

# Type a string of text
pyautogui.typewrite("Hello, World!")

# Take a screenshot and save it to a file
# screenshot = pyautogui.screenshot()
# screenshot.save("screenshot.png")

# Press the 'enter' key
pyautogui.press('enter')

# Press the combination of 'ctrl' and 'c' to copy
pyautogui.hotkey('ctrl', 'c')

# Drag the mouse to (400, 400) over 2 seconds
pyautogui.dragTo(400, 400, duration=2)



