import csv
from pathlib import Path
from pprint import pprint
from datetime import datetime


def reconcile_accounts(transactions1, transactions2):

    def to_date(s):
        return datetime.strptime(s, "%Y-%m-%d").date()


    t1 = [row[:] for row in transactions1]
    t2 = [row[:] for row in transactions2]
    n1, n2 = len(t1), len(t2)


    rec1 = [
        {'idx': i, 'date': to_date(r[0]), 'dept': r[1], 'amt': r[2], 'ben': r[3]}
        for i, r in enumerate(t1)
    ]
    rec2 = [
        {'idx': i, 'date': to_date(r[0]), 'dept': r[1], 'amt': r[2], 'ben': r[3]}
        for i, r in enumerate(t2)
    ]
    matched1 = [False] * n1
    matched2 = [False] * n2
    matched_keys = set()  


    for r1 in sorted(rec1, key=lambda x: x['date']):
        group_key = (r1['dept'], r1['amt'], r1['ben'], r1['date'])

        if group_key in matched_keys:
            continue

        candidates = []
        for r2 in rec2:
            if matched2[r2['idx']]:
                continue
            if (r2['dept'], r2['amt'], r2['ben']) == (r1['dept'], r1['amt'], r1['ben']):
                delta = (r2['date'] - r1['date']).days
                if abs(delta) <= 1:
                    candidates.append((abs(delta), r2['date'], r2))
        if not candidates:
            continue

        candidates.sort(key=lambda x: (x[0], x[1]))
        _, _, chosen = candidates[0]

        matched1[r1['idx']] = True
        matched2[chosen['idx']] = True
        matched_keys.add(group_key)

  
    out1 = [row + (["FOUND"] if matched1[i] else ["MISSING"]) for i, row in enumerate(t1)]
    out2 = [row + (["FOUND"] if matched2[i] else ["MISSING"]) for i, row in enumerate(t2)]
    return out1, out2

#------------------------------------------------------------------------------------------------------------------------

#Exemplo de dados do enunciado
data1 = [
    ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
    ["2020-12-04", "Jurídico",   "60.00", "LinkSquares"],
    ["2020-12-05", "Tecnologia", "50.00", "AWS"],
]
data2 = [
    ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
    ["2020-12-05", "Tecnologia", "49.99", "AWS"],
    ["2020-12-04", "Jurídico",   "60.00", "LinkSquares"],
]


#Criação dos arquivos csv
with open('transactions1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data1)
with open('transactions2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data2)
    
    


transactions1 = list(csv.reader(Path('transactions1.csv').open(encoding='utf-8')))
transactions2 = list(csv.reader(Path('transactions2.csv').open(encoding='utf-8')))



#------------------------------------------------------------------------------------------
out1, out2 = reconcile_accounts(transactions1, transactions2)
pprint(out1)
pprint('---------------------------------------------------------')
pprint(out2)

pprint('================================================================================')

#Casos Duplicados

tx1_dup = [
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],  
    ["2021-01-02", "Vendas", "150.00", "ClienteB"],
]
tx2_dup = [
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],
]

o1, o2 = reconcile_accounts(tx1_dup, tx2_dup)
pprint(o1)
pprint(o2)



tx1_dup = [
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],  
    ["2021-01-02", "Vendas", "150.00", "ClienteB"],
]
tx2_dup = [
    ["2021-01-01", "Vendas", "100.00", "ClienteA"],
]

o1, o2 = reconcile_accounts(tx1_dup, tx2_dup)
pprint(o1)
pprint(o2)


pprint('================================================================================')

# Exemplo data mais recente
tx1_multi = [["2020-12-25", "RH", "300.00", "EmpresaY"]]
tx2_multi = [
    ["2020-12-24", "RH", "300.00", "EmpresaY"],  
    ["2020-12-28", "RH", "300.00", "EmpresaY"],  
    ["2020-12-26", "RH", "300.00", "EmpresaY"],  
]

o1, o2 = reconcile_accounts(tx1_multi, tx2_multi)
pprint(o1)
pprint(o2)
