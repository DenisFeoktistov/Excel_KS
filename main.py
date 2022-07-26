import os
import pandas as pd
from openpyxl.styles.alignment import Alignment


pd.set_option('display.max_colwidth', None)


EPS = 1e-6


MAIN_FOLDER = "./main_folder"
ITEMS = list(filter(lambda x: x, open("items", encoding="utf-8").read().strip().split("\t")))
CATEGORIES = list(filter(lambda x: x, open("categories", encoding="utf-8").read().split("\n")))
# print(ITEMS)
# print(CATEGORIES)


result = pd.DataFrame(0., columns=["№ КС-2", "ТП/РП"] + ITEMS, index=[""] + list(map(str, range(1, len(os.listdir(MAIN_FOLDER)) + 1))))
result = result.astype({'№ КС-2': 'str', 'ТП/РП': 'str'})

cnt = 0
comp = lambda x: ((int(x.split("_")[0]), int(x.split("_")[1])) if "_" in x else (int(x), 1))
for i, filename in enumerate(sorted(os.listdir(MAIN_FOLDER), key=lambda filename: comp(filename.split()[0]))):
    i += 1
    print(filename)

    xl = pd.ExcelFile(f"{MAIN_FOLDER}/{filename}")
    sheet_name = xl.sheet_names[0]
    df1 = xl.parse(sheet_name)

    result.at[str(i), "№ КС-2"] = filename.split()[0]
    result.at[str(i), "ТП/РП"] = filename.split()[1]

    for j, row in df1.iterrows():
        # -------------------------------------------------------------------------------
        category_index = 1
        item_index = 2
        count_index = 4

        if df1["Unnamed: 3"][30] == "Наименование":
            category_index += 1
            item_index += 1
            count_index += 1
        # -------------------------------------------------------------------------------
        if row[category_index] in CATEGORIES:
            if row[item_index].startswith("Трансформаторы") and "(" in row[item_index]:
                i1 = row[item_index].find("(")
                i2 = row[item_index].find(")")

                row[item_index] = row[item_index][:i1 - 1] + row[item_index][i2 + 1:]

                i3 = row[item_index].find(":")
                row[item_index] = row[item_index][:i3 + 1] + " " + row[item_index][i3 + 1:]

            for item in ITEMS:
                if item in row[item_index]:
                    count = float((str(row[count_index]).split()[0].strip()).replace(",", "."))

                    result.at[str(i), item] += count

result.at["", "№ КС-2"] = ""
result.at["", "ТП/РП"] = ""

for item in ITEMS:
    result.at["", item] = str(round(sum(result[item]), 5))
    if int(float(result.at["", item])) - EPS <= float(result.at["", item]) <= int(float(result.at["", item])) + EPS:
        result.at["", item] = int(float(result.at["", item]))


l = os.listdir("./result")
for i in range(1, 1000):
    if f"result{i}.xlsx" in l:
        continue

    filename = f"result{i}.xlsx"
    sheet_name = f"Sheet1"

    print(f"Сохранено в файл {filename} лист {sheet_name}")

    writer = pd.ExcelWriter(f'result/{filename}', engine='xlsxwriter')
    result.to_excel(writer, sheet_name, index=False)

    workbook = writer.book
    worksheet = writer.sheets[sheet_name]

    header_format = workbook.add_format({'bold': False, 'text_wrap': True, 'fg_color': '#80c0c0', 'border': 1, 'size': 10, 'align': 'center', 'valign': 'vcenter'})
    for col_num, value in enumerate(result.columns.values):
        worksheet.write(0, col_num, value, header_format)

    fmt = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'text_wrap': True})
    worksheet.set_column('A:AAA', None, fmt)

    worksheet.set_column(2, 90, 13)
    worksheet.set_column(1, 2, 10)
    worksheet.set_column(0, 1, 6)

    writer.save()
    break
