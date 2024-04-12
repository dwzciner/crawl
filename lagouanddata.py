import requests
import json
import csv
import time


def get_lagou_data(url):
    # 构建请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Cookie':'RECOMMEND_TIP=true; user_trace_token=20230518150124-2a8dca6c-70c2-4cd4-bd91-eadb921bd50d; LGUID=20230518150124-0ddd3830-7f95-49c1-901f-f8a8a74b2cb5; _ga=GA1.2.1720030881.1684393302; index_location_city=%E5%85%A8%E5%9B%BD; privacyPolicyPopup=false; _gid=GA1.2.574875856.1684633355; __lg_stoken__=b1c9c7bdfbadcbdecb7fee08ea097bd0dcc5ae355979f0530d266dfdad52d8bf805982778c34a23b504a0bb470b867ce5b5120cd2bb4d834a6e0ca50c55e33845f93e2201349; JSESSIONID=ABAAABAABAGABFAE8D36EFF312FAF40BE9BF09F7F0851AB; WEBTJ-ID=20230521193528-1883e17d00c1599-05559577bc44fa-26031a51-1327104-1883e17d00d6c1; _gat=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGSID=20230521193509-065926da-bc40-46d4-bda5-5e5fe5a653b9; PRE_SITE=; LGRID=20230521193509-e3af1c1f-4ff7-43ab-afc4-3c239bd2ae68; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1684393302,1684633355,1684651023,1684668928; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1684668928; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221882daa1844a00-00b5114d7e4379-26031a51-1327104-1882daa18451334%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22113.0.0.0%22%7D%2C%22%24device_id%22%3A%221882daa1844a00-00b5114d7e4379-26031a51-1327104-1882daa18451334%22%7D'
    }

    # 用data进行分页爬取
    for i in range(1, 31):
        data = {
            'first': 'true',
            'pn': i,
            'kd': '数据分析师'
        }

        # 请求网页
        response = requests.post(url=url, headers=headers, data=data, timeout=3)
        print(response.text)
        time.sleep(3)  # 休息一下

        # json.loads 用于解码 JSON 数据。该函数返回 Python字段的数据类型
        response = json.loads(response.content)

        # 获取15条数据
        result_15 = response['content']['positionResult']['result']

        # 获取每条招聘岗位里面的详细信息
        for i in result_15:
            position_id = i['positionId']  # 职位Id
            position_name = i['positionName']  # 职位名称
            company_full_name = i['companyFullName']  # 公司全称
            company_short_name = i['companyShortName']  # 公司简称
            company_size = i['companySize']  # 公司规模
            finance_stage = i['financeStage']  # 融资阶段
            company_label_list = i['companyLabelList']  # 公司标签
            first_type = i['firstType']  # 第一类型
            second_type = i['secondType']  # 第二类型
            third_type = i['thirdType']  # 第三类型
            position_labels = i['positionLables']  # 职位标签
            industry_labels = i['industryLables']  # 行业标签
            create_time = i['createTime']  # 创建时间
            format_create_time = i['formatCreateTime']  # 格式化创建时间
            city = i['city']  # 城市
            district = i['district']  # 地区
            salary = i['salary']  # 薪水
            salary_month = i['salaryMonth']  # 工资月份
            work_year = i['workYear']  # 工作年限
            job_nature = i['jobNature']  # 工作性质
            education = i['education']  # 教育背景
            position_advantage = i['positionAdvantage']  # 岗位优势
            hi_tags = i['hitags']  # 福利标签

            # 存储数据, 先在当前文件下创建一个叫‘lagou_datas.csv’的文件
            # 'a' 追加写入,；encoding设置编码格式，防止乱码 ；newline是为了解决写入时新增行与行之间的一个空白行问题
            with open('./lagou_datas.csv', 'a', encoding='utf_8', newline='') as f:
                # 写入数据
                csv_write = csv.writer(f)
                # 按照以下行顺序写入，是一个列表
                csv_write.writerow([position_id, position_name, company_full_name, company_short_name, company_size,
                                    finance_stage, company_label_list, first_type, second_type, third_type,
                                    position_labels,
                                    industry_labels, create_time, format_create_time, city, district, salary,
                                    salary_month,
                                    work_year, job_nature, education, position_advantage, hi_tags])
        time.sleep(3)  # 休息一下


# 主程序
if __name__ == '__main__':
    # Ajax的URL
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

    # 传入URL，调用函数
    get_lagou_data(url)