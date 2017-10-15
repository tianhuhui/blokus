#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 21:04
# @Author  : Tian Huhui
# @Site    : 
# @File    : json_msg_proc.py
# @Software: PyCharm Community Edition

import json
import os
import sys
import numpy as np

# map size: 20*20
chessboard_size = 20

def find_chessman_index(chessman_list, chessman):
    for i, chessman_i in enumerate(chessman_list):
        if np.array_equal(chessman, chessman_i)
            return i
    return -1

# define chessman id
# 通过旋转和翻折，21类棋子最终可以得到91种棋子
def GetAllChessmanByRotateAndFold():
    chessman_dic = {
        101: [np.array([[1]])],
        201: [np.array([[1, 1]])],
        301: [np.array([[1, 1, 1]])],
        302: [np.array([[1, 1], [1, 0]])],
        401: [np.array([[1, 1, 1, 1]])],
        402: [np.array([[0, 1, 0], [1, 1, 1]])],
        403: [np.array([[1, 1, 0], [0, 1, 1]])],
        404: [np.array([[1, 0, 0], [1, 1, 1]])],
        405: [np.array([[1, 1], [1, 1]])],
        501: [np.array([[1, 1, 1, 1, 1]])],
        502: [np.array([[1, 1, 1], [0, 1, 0], [0, 1, 0]])],
        503: [np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])],
        504: [np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])],
        505: [np.array([[0, 0, 1], [0, 1, 1], [1, 1, 0]])],
        506: [np.array([[1, 1, 1], [0, 1, 1]])],
        507: [np.array([[1, 1, 1, 1], [0, 1, 0, 0]])],
        508: [np.array([[1, 0, 0, 0], [1, 1, 1, 1]])],
        509: [np.array([[1, 1, 1], [1, 0, 1]])],
        510: [np.array([[0, 0, 1, 1], [1, 1, 1, 0]])],
        511: [np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0]])],
        512: [np.array([[1, 1, 0], [0, 1, 1], [0, 1, 0]])],
    }

    for id, chessman_list in chessman_dic.items():
        chessman = chessman_list[0]
        for i in range(8):
            # 逆时针旋转
            chessman = np.rot90(chessman, i)
            if i == 4:
                # 转置
                chessman = np.transpose(chessman)
            if find_chessman_index(chessman_list, chessman) == -1
                chessman_list.append(chessman)
    return chessman_dic


def squareness_proc(squareness):
    coordinate_x = [coordinate['x'] for coordinate in squareness]
    coordinate_y = [coordinate['y'] for coordinate in squareness]
    coordinate_x_min = min(coordinate_x)
    coordinate_y_min = min(coordinate_y)
    coordinate_x_new = [x_i - coordinate_x_min for x_i in coordinate_x]
    coordinate_y_new = [y_i - coordinate_y_min for y_i in coordinate_y]
    chessman = np.zeros((max(coordinate_x_new) + 1, max(coordinate_y_new) + 1))
    for i in range(len(coordinate_x_new)):
        chessman[coordinate_x_new[i]][coordinate_y_new[i]] = 1
    return chessman, coordinate_x_min, coordinate_y_min

def sinlge_json_file_proc(sinlge_json_file):
    with open(sinlge_json_file, 'r') as json_f:
        chessboard_chessman_type = np.zeros((chessboard_size, chessboard_size))

        # 逐行解析json格式的msg
        for line in json_f:
            start_index = line.find('{')
            if start_index == -1
                continue
            line_sub = line[start_index:]
            msg_content = json.loads(line_sub)
            # 不同的消息类型
            if msg_content['msg_name'] == 'game_start':
                pass
            elif msg_content['msg_name'] == 'notification':
                msg_data = msg_content['msg_data']
                player_id = msg_content['player_id']

                chessman = msg_content['chessman']
                if 'id' not in chessman:
                    continue
                chessman_id = chessman['id']
                squareness = chessman['squareness']
                # 解析squareness
                chessman_decode, coordinate_x_min, coordinate_y_min = squareness_proc(squareness)

            elif msg_content['msg_name'] == 'game_over':


# 处理replay文件夹中的文件
def game_json_folder_proc(input_folder):
    """

    :param input_folder:
    :return:
    """
    files = os.listdir(input_folder)
    file_dir = [os.path.join(input_folder, file) for file in files]
    
    for i, file in enumerate(file_dir):

if __name__ == '__main__':
    game_replay_folder = sys.argv[1]
