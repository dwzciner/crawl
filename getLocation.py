import requests;
import json;
import pandas as pd;

def coords(city , lon_list , lat_list):

    url = 'https://restapi.amap.com/v3/geocode/geo';

    # todo 将两个参数放入字典
    params = {'key' : 'xxxxxxxxx' , 'address' : city};

    # todo 调用高德API获取经纬度信息
    res = requests.get(url , params);
    jd = json.loads(res.text);

    # todo 经纬度信息清理
    info = jd['geocodes'][0]['location'];
    info = info.split(',');
    lon_list.append(float(info[0]));
    lat_list.append(float(info[-1]));

    return info;

# todo 主函数入口
if __name__ == '__main__':

    # todo 从文件中获取城市信息
    # 打开文件
    file_read = open('analysis_result/city_analysis.csv' , mode = 'r' , encoding = 'utf-8' , newline = "");
    # 文件内容处理
    data = pd.read_csv(file_read);
    citys = data['城市'].to_list();
    counts = data['数量'].to_list();
    # 关闭文件
    file_read.close();

    # todo 经纬度列表
    lat_list = [];
    lon_list = [];

    # todo 获取经纬度信息
    for ch in citys:
        location = coords(ch , lon_list , lat_list);
        print(type(location));
        print(location);

    # todo 输出结果
    print(lat_list);
    print(lon_list);

    # todo 将信息存储到dataframe类型变量中
    dictionary = dict();
    dictionary['城市'] = citys;
    dictionary['岗位数量'] = counts;
    dictionary['lon'] = lon_list;
    dictionary['lat'] = lat_list;
    data = pd.DataFrame.from_dict(dictionary);
    print(data);

    # todo 将经纬度信息存储到文件中
    # 打开文件
    file = open('Location/location.csv' , mode = 'w' , encoding = 'utf-8' , newline = "");
    # 输入内容
    data.to_csv(file);
    # 关闭文件
    file.close();