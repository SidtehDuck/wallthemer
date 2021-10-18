from colorthief import ColorThief
color_thief = ColorThief('eva01red.png')

# get the dominant color
dominant_color = color_thief.get_color(quality=1)

palette = color_thief.get_palette(color_count=6)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

for i in range(len(palette)):  
    text = palette[i]
    colored_text = colored(palette[i][0], palette[i][1], palette[i][2], text)
    print(colored_text)