from selenium import webdriver;
from selenium.webdriver.common.by import By;
import csv;
from time import sleep;

# 信息获取
query = input("请输入待爬取的岗位");
max_page = int(input("请输入待爬取的页数"));

# todo 1.打开浏览器
driver = webdriver.Chrome();

# 打开文件
file = open('data.csv', mode='w', encoding='utf-8', newline='');
csv_writer = csv.writer(file);
# 构建表头
name = ['职位', '地区', '薪资', '经历要求', '学历', '公司名称', '其余信息'];
csv_writer.writerow(name);

for page in range(1 , min(11 , max_page + 1)):
    sleep(3);
    # todo 2.打开网站
    url = f'https://www.zhipin.com/web/geek/job?query={query}&city=100010000&page={page}';
    driver.get(url);

    # 网站为动态加载，需要一定的加载时间
    # 打开网站设置一定时间延迟
    driver.implicitly_wait(10);

    # todo 3.提取数据

    # todo a.针对每个大的职位信息提取
    lis = driver.find_elements(By.XPATH, "//ul[@class='job-list-box']/li");
    # todo b.二次提取：对岗位的详细信息提取
    for li in lis:
        job_name = li.find_element(By.XPATH, './/span[@class="job-name"]').text;
        job_area = li.find_element(By.XPATH, './/span[@class="job-area"]').text;
        job_salary = li.find_element(By.XPATH, './/span[@class="salary"]').text;
        info_list = li.find_elements(By.XPATH, ".//div[@class='job-info clearfix']/ul[@class='tag-list']/li");
        experience = info_list[0].text;
        education = info_list[-1].text;
        company_name = li.find_element(By.XPATH, './/h3[@class="company-name"]/a').text;
        company_tag_list = li.find_element(By.XPATH, './/ul[@class="company-tag-list"]/li').text;
        print(job_name, job_area, experience, education, company_name, company_tag_list);
        # 存文件
        csv_writer.writerow([job_name, job_area, job_salary, experience, education, company_name, company_tag_list]);

#关闭文件
file.close();
