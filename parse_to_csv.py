import sys, json, csv

if len(sys.argv) < 2:
    print('usage: python parse_to_csv.py <YYYYMM>')
    sys.exit(-1)
month = sys.argv[1]

rows = []
rows.append(['Month', 'Category', 'Actual', 'Budget', 'Diff']) # only need this for first export
with open('out.json') as json_file:
    data = json.load(json_file)
    month_budget = data[month]
    for x in ['income', 'spending']:
        for budget_cat in month_budget[x]:
            rows.append([month, budget_cat['cat'], budget_cat['amt'], budget_cat['bgt'], budget_cat['rbal']])

with open('out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)