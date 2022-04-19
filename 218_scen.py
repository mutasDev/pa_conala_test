#Sort dictionary `o` in ascending order based on its keys and items


o = {2: 6, 1: 5, 3: 7, 4: 8}

sorted(o.items(), key=lambda x: x[0])