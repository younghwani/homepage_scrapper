import requests
from bs4 import BeautifulSoup

def extract_company(html):
    company_name = str(html.find('a', class_='link').string)
    soup = BeautifulSoup(str(html), 'html.parser').find_all()
    temp = [item['data-info'] for item in soup if 'data-info' in item.attrs][0]
    company_id = temp.split("|")[0].split(" ")[1]
    return {'company_name':company_name, 'link':f'https://www.jobkorea.co.kr/Recruit/GI_Read/{company_id}'}

def extract_domain(link):
    result = requests.get(f"{link}")
    soup = BeautifulSoup(result.text, 'html.parser')
    if soup.find('a', class_="devCoHomepageLink") == None:
        domain = "nothing"
    else:
        temp = soup.find('a', class_="devCoHomepageLink")
        domain = temp['href']
    return domain
   
def extract_companies(url):
    companies = []
    result = requests.get(f"{url}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('tr', class_='devloopArea')
    for result in results:
        temp = []
        company = extract_company(result)
        domain = extract_domain(company['link'])
        # domain is not 'nothing' -> return
        if domain != "nothing" : 
            temp.append(company['company_name'])
            temp.append(domain)
            companies.append(temp)
    return companies

def get_companies(url):
    # last_page = get_last_page()
    companies = extract_companies(url)
    return companies
