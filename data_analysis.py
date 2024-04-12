import pandas as pd;

# todo 将列表返回一个百分比列表
def get_percentage(temp_list):
    sum = 0;
    list_new = [];
    for x in temp_list:
        sum += x;
    for i in range(0 , len(temp_list)):
        list_new.append(temp_list[i] / sum);
    return list_new;

# todo 统计薪资区间
def analysis_salary(data):

    # 取data中最大值与最小值
    data_max = data['薪资'].max();
    data_min = data['薪资'].min();

    # 将薪资区间划分为五个区间
    # 确定薪资区间上界/下界
    area_min = int(data_min / 1000) * 1000;
    area_max = (int(data_max / 1000) + 1) * 1000;
    while True:
        if int((area_max - area_min) / 6000) == ((int(area_max) - int(area_min)) / 6000):
            break;
    delta = int(area_max - area_min) / 6;

    # todo 创建一个新的表
    new_data = pd.DataFrame(index = [f'{area_min} , {area_min + delta}' , f'{area_min + delta} , {area_min + delta * 2}' , f'{area_min + delta * 2} , {area_min + delta * 3}' , f'{area_min + delta * 3} , {area_min + delta * 4}'] , columns = ['count' , 'percentage']);

    # todo 对薪资信息进行计数
    segments = pd.cut(data['薪资'] , [area_min , area_min + delta , area_min + delta * 2 , area_min + delta * 3 , area_max + 1] , right = False);
    counts = pd.value_counts(segments , sort = False);
    print(counts);
    temp = counts.to_list();

    # 求每个区间的占比信息
    temp_percent = get_percentage(temp);

    # 将list信息填入new_data中
    new_data['count'] = temp;
    new_data['percentage'] = temp_percent;
    print(new_data);

    return new_data;

# todo 统计学历频率
def analysis_degree(data):

    # 待返回的新DataFrame对象
    new_data = pd.DataFrame(index = ['本科' , '大专' , '不限' , '硕士' , '博士'] , columns = ['数量' , '百分比']);

    # 统计种类个数
    temp = data['学历'].value_counts();

    # 对series进行修正
    temp['不限'] = temp['不限'] + temp['学历不限'];
    temp = temp.drop(['学历不限']);
    print(temp);

    # 将series转为list
    temp_list = temp.to_list();
    print(temp_list);

    # 求百分比
    list_percentage = get_percentage(temp_list);

    # 更新new_data信息
    new_data['数量'] = temp_list;
    new_data['百分比'] = list_percentage;

    return new_data;

# todo 统计经验频率
def analysis_experience(data):

    # 待返回的新DataFrame对象
    new_data = pd.DataFrame(index = ['3-5年' , '1-3年' , '5-10年' , '在校/应届' , '经验不限' , '10年以上' , '1年以内'] , columns = ['数量' , '百分比']);

    # 统计种类个数
    temp = data['经验'].value_counts();

    # todo 修正数据
    # 修正1年以内
    temp['1年以内'] = temp['1年以内'] + temp['1年以下'];
    temp = temp.drop(['1年以下']);
    # 修正经验不限
    temp['经验不限'] = temp['经验不限'] + temp['不限'];
    temp = temp.drop(['不限']);
    temp = temp.drop(['5天/周']);
    temp = temp.drop(['4天/周']);
    temp = temp.drop(['3天/周']);

    # 将series转为list
    temp_list = temp.to_list();

    # 求百分比
    list_percentage = get_percentage(temp_list);

    # 更新new_data信息
    new_data['数量'] = temp_list;
    new_data['百分比'] = list_percentage;

    return new_data;

# todo 统计城市频率
def analysis_city(data):

    # todo 统计频率
    temp = data['城市'].value_counts();

    # todo series转换为dataframe
    new_data = temp.to_frame();
    print(new_data);

    return new_data;

# todo 城市薪资水平统计
def city_salary(data):

    # todo 从city_analysis.csv中筛选出合适的(岗位数>40)城市
    # 打开文件
    file_temp = open('analysis_result/city_analysis.csv' , mode = 'r' , encoding = 'utf-8' , newline = "");
    data_temp = pd.read_csv(file_temp);
    # 整理数据
    target_city_series = data_temp[data_temp.数量 > 40];
    target_city = target_city_series['城市'].to_list();
    # print(target_city);     # 测试结果
    # 关闭文件
    file_temp.close();

    # todo 计算选中城市的平均薪资水平
    dictionary = dict();
    aver_list = [];
    # todo 选择对应的行
    for ch in target_city:
        city_series = data['薪资'][data.城市 == ch];
        aver = city_series.mean();
        aver_list.append(aver);
    dictionary['城市'] = target_city;
    dictionary['平均薪资'] = aver_list;

    # 创建新dataframe存储城市薪资信息
    new_data = pd.DataFrame.from_dict(dictionary);

    # 对数据进行排序
    new_data = new_data.sort_values(by = '平均薪资' , ascending = False);
    print(new_data);

    return new_data;

# todo 岗位薪资水平统计
def job_salary():

    # 所有岗位种类
    job_list = ['android' , 'cpp' , 'ios' , 'java' , 'python'];
    # 平均薪资列表
    aver_list = [];

    for ch in job_list:
        file_name = f'data_{ch}.csv';

        # todo 从文件获取薪资信息
        # 打开文件
        target_file = open(f'cleanData/{file_name}' , mode = 'r' , encoding = 'ANSI' , newline = "");
        data_temp = pd.read_csv(target_file);
        # 关闭文件
        target_file.close();

        # todo 处理数据
        aver = data_temp['薪资'].mean();
        aver_list.append(aver);

    # todo 将数据存储到dataframe类型变量中
    dictionary = dict();
    dictionary['工作岗位'] = job_list;
    dictionary['平均薪资'] = aver_list;
    new_data = pd.DataFrame.from_dict(dictionary);
    new_data = new_data.sort_values(by = '平均薪资' , ascending = False);
    print(new_data);

    return new_data;

# todo 主函数入口
if __name__ == "__main__":

    # todo 读取文件数据
    # 打开文件
    file = open("cleanData/data_all.csv" , mode = 'r' , encoding = "utf-8" , newline = "");
    # 将文件内容存入data中
    data = pd.read_csv(file);
    # 关闭文件
    file.close();

    # todo 处理数据
    # data_save = analysis_salary(data);
    # data_save = analysis_degree(data);
    # data_save = analysis_experience(data);
    # data_save = analysis_city(data);
    # data_save = city_salary(data);
    # data_save = job_salary();

    # # todo 存储文件
    # # 打开文件
    # file_save = open("analysis_result/complex/job_salary.csv" , mode = 'w' , encoding = "utf-8" , newline = "");
    # # 存入数据
    # data_save.to_csv(file_save);
    # # 关闭文件
    # file_save.close();
    #
    # # todo 存储excel可打开的csv文件测试
    # # 打开文件
    # file_save = open("test_result/complex/job_salary.csv" , mode = 'w' , encoding = "ANSI" , newline = "");
    # # 存入数据
    # data_save.to_csv(file_save);
    # # 关闭文件
    # file_save.close();