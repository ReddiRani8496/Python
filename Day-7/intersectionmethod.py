colors1 = {'white','red','green','yellow'}

colors2 = {'blue','purple','red','white'}

colors3 = colors1.intersection(colors2);

print(colors3) # intersection of colors1 and colors2

colors4 = colors1 & colors2

print(colors4);

colors1.intersection_update(colors2);

print(colors1)