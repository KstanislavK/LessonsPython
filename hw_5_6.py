with open(r'for_hw_5_6.txt', 'r', encoding='utf-8') as obj:
    obj_dict = {}
    lines = obj.readlines()
    for el in lines:
        el_list = el.split()
        total = 0
        for i in range(1, len(el_list)):            
            ind = int(el_list[i].find('('))
            if ind > 0:
                digit = int(el_list[i][:ind])
                total += digit
        obj_dict[el_list[0]] = total 
    print(obj_dict)