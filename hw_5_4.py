with open(r'for_hw_5_4.txt', 'r', encoding='utf-8') as file:
    line = file.readlines()
    new_line = []
    for el in line:
        if 'One' in el:            
            new_line.append(el.replace('One', 'Один'))
        elif 'Two' in el:
            new_line.append(el.replace('Two', 'Два'))
        elif 'Three' in el:
            new_line.append(el.replace('Three', 'Три'))
        elif 'Four' in el:
            new_line.append(el.replace('Four', 'Четыре'))
    with open(r'for_hw_5_4_new.txt', 'w', encoding='utf-8') as new_file:
        for el in new_line:
            new_file.write(el)