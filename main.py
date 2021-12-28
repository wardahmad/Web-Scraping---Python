from bs4 import BeautifulSoup
import requests
import time


print('skill that you are not familiar with')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_req_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_req_txt)

    soup = BeautifulSoup(html_req_txt, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        # print(published_date)
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            # print(company_name)
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            # print(skills)
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info} \n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait * 60)