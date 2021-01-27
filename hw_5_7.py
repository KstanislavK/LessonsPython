import json
with open(r'for_hw_5_7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    quan_positive_firms = 0 #quantity of firms with positive profit
    total_profit = 0 #for count average profit
    firm_dict = {}
    for el in lines:
        el_list = el.split()
        profit = int(el_list[2]) - int(el_list[3])
        firm_dict[el_list[0]] = profit
        if profit > 0:
            total_profit += profit
            quan_positive_firms += 1
    average_profit = total_profit / quan_positive_firms
    av_pr_dict = {'average_profit': average_profit}
    firm_list = [firm_dict, av_pr_dict]
    with open(r'for_hw_5_7.json', 'w') as obj:
        json.dump(firm_list, obj)