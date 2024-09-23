import random

# story generator

main_char = ['Alice','Bob','Charlie','David','Emmette']
side_char = ['Tom','Zoro','Jenna','Elena','Michael']
place = ['forest','village','town','seashore','island']
theme = ['discovered a valuable treasure','solved a hidden mystery','went to a movie together','solved a mathematical problem']

person1 = random.choice(main_char)
person2 = random.choice(side_char)
pl = random.choice(place)
th = random.choice(theme)

story = "Once upon a time " + person1 + " and " + person2 + " lived in a " +pl + "." + "\nOne fine day, they " + th
print(story)
