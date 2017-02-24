"""
energizect
~~~~~~~~~~

Script which, using BeautifulSoup4 and LXML's HTML parser, scrapes current
energy company prices per kilowatt-hour and displays relevant information in
the JSON serialization format.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
import requests
import re
from bs4 import BeautifulSoup as BS
from pprint import pprint


def get_prices():
    """ Source: 1

    Below are the keys of the individual dictionaries which comprise the list:

    1. "phone_number" - Company's main contact phone number.
    2. "cycle" - Billing cycle in months.
    3. "supply_rate" - Cost per kilowatt-hour.
    4. "type" - Fixed or Tiered pricing.
    5. "renewable" - Percentage of CT's Renewable Energy standard met.
    6. "img" - URL to small company logo PNG.
    7. "enrollment" - Enrollment fee.
    8. "cancellation" - Cancellation fee.
    9. "name" - The name of the company.

    :return: dict containing all company data in specific format
    """
    commercial = '_bus'
    residential = "_res"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {
        'choose_your_uility': 'clp',
        'account_type': commercial,
        'type': 'clp_res',
        'submit': 'COMPARE+NOW'
    }
    url = "http://www.energizect.com/compare-energy-suppliers/compare-supplier-options"

    s = requests.Session()
    res = s.post(
        url,
        headers=headers,
        data=payload
    )

    soup = BS(res.content, 'lxml')
    raw_companies = soup.find_all('tr', attrs={'id': re.compile("plan-[0-9]{5}")})
    companies = []

    for company in raw_companies:
        data = {}
        row_cells = company.find_all("td", {'rel': True, 'class': re.compile("col_[0-9]")})

        for col, td in enumerate(row_cells):
            row_data = [a.strip() for a in td.get_text().splitlines() if a.strip()]
            if col == 0:
                data['img'] = str(td.select("img:nth-of-type(1)")[0]['src']).strip()
                data['phone_number'] = row_data[0]
                data['name'] = row_data[1]
            elif col == 1:
                data['type'] = row_data[0]
                data['cycle'] = row_data[1][:-1]
                data['cancellation'] = row_data[2][:-1]
                data['enrollment'] = row_data[3]
            elif col == 2:
                data['renewable'] = row_data[0].split(" Renewable")[0]
            elif col == 3:
                data['supply_rate'] = float(row_data[0][:-1])
        companies.append(data)

    return companies


if __name__ == "__main__":
    pprint(get_prices())
