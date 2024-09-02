mountain_heights = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]


for i in mountain_heights: 
    if i < 3000:
        print('low heigh')

    elif i < 6000:
        print ('middle heigh')
    
    else:
        print('high heigh')


