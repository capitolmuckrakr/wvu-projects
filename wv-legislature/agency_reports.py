import requests
from bs4 import BeautifulSoup
import csv

with open('all_reports.csv', 'r') as existing_reports:
    reader = csv.DictReader(existing_reports)
    previous_urls = [x['url'] for x in reader if x['url'] != 'No Report']

r = requests.get("http://www.wvlegislature.gov/Reports/Agency_Reports/agencylist_all.cfm")
soup = BeautifulSoup(r.text, 'html.parser')
results = []
reports = soup.find_all('tr')[1:-1]

for report in reports:
    agency, title, year, filler = [x.text for x in report.find_all('td')]
    if report.find('a'):
        results.append([agency, title, year, "http://www.wvlegislature.gov"+report.find('a')['href']])
    else:
        results.append([agency, title, year, "No Report"])

all_report_urls = [x[3] for x in results if x[3] != 'No Report']
new_report_urls = list(set(all_report_urls) - set(previous_urls))

new_reports = [x for x in results if x[3] in new_report_urls]

with open('new_reports.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['agency', 'title', 'year', 'url'])
    writer.writerows(new_reports)

with open("all_reports.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['agency', 'title', 'year', 'url'])
    writer.writerows(results)
