import SimpleColors

color = SimpleColors.Colors()

print("FOREGROUND:      ", end=" ")
print(color.F_AQUA + "AQUA", end=" ")
print(color.F_BLACK + "BLACK", end=" ")
print(color.F_BLUE + "BLUE", end=" ")
print(color.F_GREEN + "GREEN", end=" ")
print(color.F_PURPLE + "PURPLE", end=" ")
print(color.F_RED + "RED", end=" ")
print(color.F_WHITE + "WHITE", end=" ")
print(color.F_YELLOW + "YELLOW" + color.S_CLEAR)
print("BACKGROUND:      ", end=" ")
print(color.B_AQUA + "AQUA", end=" ")
print(color.B_BLACK + "BLACK", end=" ")
print(color.B_BLUE + "BLUE", end=" ")
print(color.B_GREEN + "GREEN", end=" ")
print(color.B_PURPLE + "PURPLE", end=" ")
print(color.B_RED + "RED", end=" ")
print(color.B_WHITE + "WHITE", end=" ")
print(color.B_YELLOW + "YELLOW" + color.S_CLEAR)
print("STYLES:          ", end=" ")
print(color.S_CLEAR + "CLEAR", end=" ")
print(color.S_BOLD + "BOLD" + color.S_CLEAR, end=" ")
print(color.S_PALE + "PALE" + color.S_CLEAR, end=" ")
print(color.S_ITALIC + "ITALIC" + color.S_CLEAR, end=" ")
print(color.S_UNDERLINE + "UNDERLINE" + color.S_CLEAR, end=" ")
print(color.S_FLASH + "FLASH" + color.S_CLEAR, end=" ")
print(color.S_HIDE + "HIDE" + color.S_CLEAR + "<- hidden text :)", end=" ")
print(color.S_CROSS + "CROSS" + color.S_CLEAR, end=" ")
print(color.S_DOUBLEUL + "DOUBLEUL" + color.S_CLEAR, end=" ")
print(color.S_FRAME + "FRAME" + color.S_CLEAR, end=" ")
print(color.S_SURROUND + "SURROUND" + color.S_CLEAR, end=" ")
print(color.S_CROSSOUT + "CROSSOUT" + color.S_CLEAR)
print("CUSTOM COLORS:   ", end=" ")
print(color.custom(255, 161, 91, False) + "LIGHT-ORANGE FOREGROUND" + color.S_CLEAR, end=" ")
print(color.custom(144, 77, 48, True) + "TERRACOTTA BACKGROUND" + color.S_CLEAR, end=" ") 
print(color.custom(186, 219, 173, False) + "DARK-GREEN TEA" + color.S_CLEAR)

while True:
    pass