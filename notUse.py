# URL = f"https://www.jobkorea.co.kr/recruit/joblist"

'''
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', class_='tplPagination')
    links = pagination.find_all('li')
    pages = []
    for link in links:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page
'''

'''
jobs = []
for page in range(last_page):
    print(f'Scrapping Job Korea Page : {page+1}')
    result = requests.get(f"https://www.jobkorea.co.kr/recruit/joblist#anchorGICnt_{page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('tr', class_='devloopArea')
    for result in results:
        job = extract_job(result)
        domain = extract_domain(job['link'])
        #temp = job['company_name'] + domain
        #jobs.append(temp)
    print("\n\n")
return jobs'''

