import pandas as pd;

# 处理薪资(不规则文本->整数型)
def cleansals(row : list)->float:
    val = row[1];
    sal = row[0];
    if val[-1] == '万' or val[-1] == 'w' or val[-1] == 'W':
        num = float(sal.strip('万').strip('w').strip('W')) * 10000;
    elif val[-1] == '千' or val[-1] == 'k' or val[-1] == 'K':
        num = float(sal.strip('千').strip('k').strip('K')) * 1000;
    elif val[-1] == '天':
        num = float(sal.strip('天')) * 30;
    elif val[-1] == '薪' and (val[-5] == '万' or val[-5] == 'w' or val[-5] == 'W'):
        num = float(sal.strip('万').strip('w').strip('W')) * 10000;
    elif val[-1] == '薪' and(val[-5] == '千' or val[-5] == 'k' or val[-5] == 'K'):
        num = float(sal.strip('千').strip('K').strip('K')) * 1000;
    elif val[-3] == '元':
        num = float(sal);
    else:
        print(sal , row)
        num = pd.NA;
    return num;

def cleanCity(row : list)->str:
    city = row[0];
    return city;

# todo 主函数入口
if __name__ == '__main__':
    # todo 打开文件
    file = open('data_source/data_python_ansi.csv', mode='r', encoding='ANSI', newline='');
    data = pd.read_csv(file);
    # todo 关闭文件
    file.close();

    # todo 处理数据
    # 处理薪资
    sals = data['薪资'].str.split('-').map(cleansals);
    data['薪资'] = sals;
    print(sals);

    # # 处理城市
    # citys = data['城市'].str.split('·').map(cleanCity);
    # data['城市'] = citys;
    # print(data);

    # # todo 存储文件
    # # 打开文件
    # file_save = open('cleanData/data_android.csv' , mode = 'w' , encoding = 'ANSI' , newline = '');
    # data.to_csv(file_save);
    # # 关闭文件
    # file_save.close();