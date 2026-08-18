from openpyxl import Workbook
ws=Workbook()
wsa=ws.active
#wsa['A1']="first"
# sample_list = [["name","city"],["kavya","Andhra Pradesh"],["Surya", "Banglore"],["Surya Prakash","Andhra Pradesh"]]
# for data in sample_list:
#     wsa.append(data)

for i in range(1,8):
    for j in range(1,8):
        wsa.cell(row=i, column=j).value=i+j

ws.save("demoexcelsheet.xlsx")