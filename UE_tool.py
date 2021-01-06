import numpy as np
import random
import csv
import os
import matplotlib.pyplot as plt
from PIL import Image

def Create_random_pos(num_total, a_mat):
    cache_list = []
    size = a_mat.shape
    while len(cache_list) < num_total:
        generateddata = [random.randint(0,size[0]-1), random.randint(0,size[1]-1)]
        if a_mat[generateddata[0]][generateddata[1]] > 5:
            if not generateddata in cache_list:
                cache_list.append(generateddata)
    return cache_list

def Get_pic_mat(file_name):
    img = Image.open(file_name).convert('L')
    a_img = np.asarray(img)
    return a_img


def read_csv(addr):
    ue_list = []
    with open(addr, 'r') as f:
        f = csv.reader(f, delimiter=',')
        next(f)
        for row in f:
            ue_list.append(row)
    for i in range(len(ue_list)):
        ue_list[i] = list(map(int, ue_list[i]))
    return ue_list

def Draw_result(ue_list, img_addr):
    img = Image.open(img_addr)
    fig = plt.figure('fig')
    ax = fig.add_subplot(111)
    for i in range(len(ue_list)):
        plt.plot(ue_list[i][1], ue_list[i][0], "xy")
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.invert_yaxis()
    plt.imshow(img)
    fig.show()

def Draw_result_nopic(ue_list):
    fig = plt.figure('fig')
    ax = fig.add_subplot(111)
    for i in range(len(ue_list)):
        plt.plot(ue_list[i][1], ue_list[i][0], "xy")
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.invert_yaxis()
    fig.show()

def csv_save(csv_path, ue_list):
    csv_name = csv_path + r"\ue_list.csv"
    csv_file = open(csv_name, 'w', newline='')
    data = [['row', 'col']]
    for x in ue_list:
        data.append(x)
    writer = csv.writer(csv_file)
    writer.writerows(data)
    csv_file.close()

def mode_Create_csv(pic_addr):
    csv_save_path = os.path.abspath(os.path.join(pic_addr, ".."))
    new_mat = Get_pic_mat(pic_addr)
    
    total_ue = input("输入生成用户总数:")
    total_ue = int(total_ue)

    ue_list = Create_random_pos(total_ue, new_mat)
    csv_save(csv_save_path, ue_list)

def mode_Show_csv(csv_addr):
    ue_list = read_csv(csv_addr)
    print("请将背景图片拖入cmd中(直接回车无背景)：")
    img_addr = input()
    if img_addr == '':
        Draw_result_nopic(ue_list)
    else:
        Draw_result(ue_list, img_addr)


def main():
    print("1.拖入图片生成UE_csv(Recommend：.bmp)")
    print("2.拖入csv文件，将UE数据图形化")
    print("请将图片或csv文件直接拖入cmd中(并按回车键)：")
    
    addr = input()
    if addr.endswith('csv'):
        mode_Show_csv(addr)
    else:
        mode_Create_csv(addr)

    input("完成，回车键关闭窗口...")
    



if __name__ == '__main__':
    main()