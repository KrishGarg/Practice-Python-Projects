import shutil
import platform
import os

# Takes all the necessary text from the user.
title = input("Enter the Title for the Story:\n")
plot = input("Enter the Plot for the Story:\n")
moral = input("Enter the Moral of the Story:\n")

# Centering the title to the center of the terminal
story = title.center(shutil.get_terminal_size().columns)

# Making the plot of the story bold.
story += "\n" + '\033[1m' + plot + '\033[0m' + "\n"

# Adding the moral to the story.
story += "Moral of the Story: " + moral + "\n"

# Adding the 'The End' line at the end in the middle.
end = "The End".center(shutil.get_terminal_size().columns, "-")
story += end

# Clearing the terminal.
if platform.system().lower() == "windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
clear()

# Printing the story.
print(story)