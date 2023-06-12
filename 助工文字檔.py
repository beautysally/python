import requests
import bs4

# 建立 TXT 檔案
file = open('job_data.txt', 'w', encoding='utf-8')

# 要爬取的頁數
start_page = 1
end_page = 5

# 迴圈爬取多頁
for page in range(start_page, end_page + 1):
    url = f"https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E5%8A%A9%E7%90%86%E5%B7%A5%E7%A8%8B%E5%B8%AB&order=1&page={page}&mode=s&jobsource=2018indexpoc"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    jobs = soup.find_all('article', class_='js-job-item')

    for job in jobs:
        company = job.get('data-cust-name')
        company_type = job.get('data-indcat-desc')
        try:
            job_pay = job.find('span', class_='b-tag--default').text
        except:
            job_pay = job.find('a', class_='b-tag--default').text
        job_url = job.find('a')['href']

        # 寫入資料到 TXT 檔案
        file.write(f"公司名稱: {company}\n")
        file.write(f"公司類別: {company_type}\n")
        file.write(f"薪資: {job_pay}\n")
        file.write(f"網址: {job_url}\n")
        file.write("\n")

# 關閉檔案
file.close()

print("爬取完成，結果已保存到 job_data.txt")
