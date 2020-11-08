import xlsxwriter
import re

pattern = re.compile(r'\d\d\.\d\d.\d\d')

workbook = xlsxwriter.Workbook('aes_data.xlsx')
worksheet = workbook.add_worksheet()
# worksheet.write(0, 0, 'KKS')
# worksheet.write(0, 1, 'Знач')
# worksheet.write(0, 2, 'Ед. изм')
# worksheet.write(0, 3, 'Дост.')
# worksheet.write(0, 4, 'Описание')

with open("input.txt") as f:
    time_row_counter = 0
    item_counter = 0
    keys = ['10LAB11CP002_XQ01', '10LAB12CP002_XQ01', '10LAB13CP002_XQ01', '10LAB14CP002_XQ01', '10LAB15CP002_XQ01',
            '10LAB11CP003_XQ01', '10LAB12CP003_XQ01', '10LAB13CP003_XQ01', '10LAB14CP003_XQ01', '10LAB15CP003_XQ01',
            '10LAB11CF001_XQ01', '10LAB12CF001_XQ01', '10LAB13CF001_XQ01', '10LAB14CF001_XQ01', '10LAB15CF001_XQ01',
            '10LAB00FT902_XQ01', '10LAC11CE021_XQ01', '10LAC12CE021_XQ01', '10LAC13CE021_XQ01', '10LAC14CE021_XQ01',
            '10LAC15CE021_XQ01', '10LAC11CS001A_XQ01', '10LAC12CS001A_XQ01', '10LAC13CS001A_XQ01', '10LAC14CS001A_XQ01',
            '10LAC15CS001A_XQ01', '10BBA00CE010_XQ01', '10BBB00CE010_XQ01', '10BBC00CE010_XQ01', '10BBD00CE010_XQ01',
            '10MKA10CE912_XQ01', '10JKS00FU901_XQ01']

    desc_flags = {key: False for key in keys}
    key_rows = {key: 0 for key in keys}

    for ind, key in enumerate(keys):
        worksheet.write(0, ind + 1, key)

    worksheet.set_column(0, len(keys), len(keys[0]) + 3)
    worksheet.write(0, 0, "Время")

    progress = 0

    for line in f:
        for column, key in enumerate(keys):
            if key in line:
                ind = line.index(key)
                splited = line[ind:].split()
                print(f'Progress: {progress}', end='\r')
                progress += 1

                value = splited[1]
                unit = splited[2]
                desc = ' '.join(splited[3:])

                if key_rows[key] == 0:
                    worksheet.write(key_rows[key] + 1, column + 1, 'Дост--Описание')
                    worksheet.write(key_rows[key] + 2, column + 1, desc)
                    worksheet.write(key_rows[key] + 3, column + 1, unit)
                    key_rows[key] += 3

                worksheet.write(key_rows[key] + 1, column + 1, value)
                key_rows[key] += 1

                item_counter += 1

        if bool(pattern.match(line[:8])):
            time_data = ' '.join(line.split()[:2])
            worksheet.write(time_row_counter + 4, 0, time_data)
            time_row_counter += 1


        # if item_counter > 50:
        #     break

workbook.close()

print()
print("Done!")
