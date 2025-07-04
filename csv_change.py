import csv, math

input_list = []
with open('node/info8.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        input_list.append(row)

with open('csv/node_detail.csv', 'a', newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for index in range(len(input_list)):
        add_list = []
        nowNode = input_list[index]
        xnow = int(nowNode[3])
        ynow = int(nowNode[4])
        for next in range(len(nowNode)):
            if next >= 5:
                nextIndex = int(nowNode[next]) - 1
                xnext = int(input_list[nextIndex][3])
                ynext = int(input_list[nextIndex][4])
                distance = round(math.sqrt((xnow-xnext)**2 + (ynow-ynext)**2) / 50, 1)
                # distance = math.ceil(math.sqrt((xnow-xnext)**2 + (ynow-ynext)**2) / 100)
                add_list.append(input_list[nextIndex][1] + "_" + str(distance))
            else:
                add_list.append(nowNode[next])
        writer.writerow(add_list)