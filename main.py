from jobKorea import get_companies
from save import save_to_file

companies = get_companies("https://www.jobkorea.co.kr/recruit/joblist#anchorGICnt_1")
# print(companies)
save_to_file(companies)