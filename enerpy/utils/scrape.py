import requests
from lxml import html
from pprint import pprint
from lxml.cssselect import CSSSelector


commercial = '_bus'
residential = "_res"


headers = {'User-Agent': 'Mozilla/5.0'}
payload = {
    'choose_your_uility': 'clp',
    'account_type': commercial,
    'type': 'clp_res',
    'submit': 'COMPARE NOW'

}
url = "http://www.energizect.com/compare-energy-suppliers/compare-supplier-options"
tbody_xpath = '//*[@id="supp_results"]/tr'

s = requests.Session()
res = s.post(
    url,
    headers=headers,
    data=payload
)

companies = []

tree = html.fromstring(res.content)
for tr in tree.xpath(tbody_xpath)[1:]: # skip the initial header row
    columns = tr.getchildren()
    companies.append({
        'supplier':columns[0],
        'desc':columns[1],
        'renewable':columns[2],
        'supply_rate':columns[3],
        'monthly_supply_cost':columns[4],
        'savings':columns[5],
        'contact':columns[6],
    })

for i, company in enumerate(companies):
    # Supplier
    companies[i]['supplier'] = company['supplier'].attrib['rel']

    # Plan Description
    desc_list = [i for i in list(map(str.strip, companies[i]['desc'].text_content().replace("\n", "").strip().splitlines())) if i]
    keys = ["type", "billing_cycle", "cancellation_fee", "enrollment_fee"]
    if len(desc_list) == 5:
        keys.append("notes")
    companies[i]['desc'] = dict(zip(keys, desc_list))

    # Renewable Energy
    companies[i]['renewable'] = dict(zip(["percentage", "quality"], list(map(lambda x: x.replace("Renewable", ""), ' '.join([i for i in list(map(str.strip, companies[i]['renewable'].text_content().splitlines())) if i][0].split()[:2]).split()))))

    # Generation Supply Rate
    companies[i]['supply_rate'] = {
        'rough': [i for i in list(map(str.strip, companies[i]['supply_rate'].text_content().replace("\n", "").splitlines())) if i][0],
        'precise': companies[i]['supply_rate'].attrib['rel']
    }

    # Generation Supply Cost Per Month
    #pprint(companies[i]['monthly_supply_cost'].attrib['rel'])
    #pprint(companies[i]['monthly_supply_cost'].attrib)
    companies[i]['monthly_supply_cost'] = None

    # Monthly Savings or Additional Cost
    #pprint(companies[i]['savings'].attrib)
    companies[i]['savings'] = None

    # Monthly Savings or Additional Cost
    #pprint([i for i in list(map(str.strip, companies[i]['contact'].text_content().splitlines())) if i])
    companies[i]['contact'] = None
