import pyfiglet


for fnt in ['banner','block', 'bubble', 'digital', 'doh', 'isometric1', 'letters', 'larry3d', 'rectangles', 'slant', 'speed', 'starwars']:
    text = pyfiglet.figlet_format('Femke', font=fnt)

    print(text)
