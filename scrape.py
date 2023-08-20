from configparser import ConfigParser
from bs4 import BeautifulSoup
from lxml import etree
import requests

# proxy for google -- scraperApi (free access)
# xpath (ex. preceeding sibling)
# try more websites

config = ConfigParser()
config.read('configuration.ini')


def scrape(website, url):
    # Make a GET request to fetch the raw HTML content

    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
    
    # html_content = requests.get(url).text
    html_content = requests.get(url, headers=HEADERS)

    # Parse the html content
    # soup = BeautifulSoup(html_content, "lxml")
    soup = BeautifulSoup(html_content.content, "lxml")
    

    # print(soup)

    dom = etree.HTML(str(soup))
    # print("yoyoyo: ", dom.xpath('//span[@class="name"]'))
    print("yoyoyo: ", dom.xpath('//*[@id="firstHeading"]')[0].text)


    # set comfig to correct website
    config_data = config[website]






    # # scrape info
    name = ''
    if (config_data['name'] == 'none'):
        name = 'none'
    else:
        name = soup.select(config_data['name'])[0].get_text().strip()
    
    # name = soup.find(attrs={config_data['name'].split()[0]: config_data['name'].split()[1]}).get_text()
    institution = ''
    if (config_data['institution'] == 'none'):
        institution = 'none'
    else:
        institution - soup.select(config_data['institution'])[0].get_text().strip()
        # institution = soup.find(attrs={config_data['institution'].split()[0]: config_data['institution'].split()[1]}).get_text()

    # # institution = soup.find(attrs={config_data['institution'].split()[0]: config_data['institution'].split()[1]}).get_text()
    keywords = []
    if (config_data['keywords'] == 'none'):
        keywords.append('none')
    else:
        keywords_query = soup.select(config_data['keywords'])
        for keyword in keywords_query:
            keywords.append(keyword.get_text().strip())

    # but this doesn't work for uiuc
    papers = []
    if (config_data['papers'] == 'none'):
        papers.append('none')
    else:
        papers_query = soup.select(config_data['papers'])
        # papers_query = soup.find_all(attrs={config_data['papers'].split()[0]: config_data['papers'].split()[1]})
        for paper in papers_query:
            papers.append(paper.get_text().strip())

    email = ''
    if (config_data['email'] == 'none'):
        email = 'none'
    else:
        email = soup.select(config_data['email'])[0].get_text().strip()

    education = ''
    if (config_data['education'] == 'none'):
        education = 'none'
    else:
        education = soup.select(config_data['education'])[0].get_text().strip()

    title = ''
    if (config_data['title'] == 'none'):
        title = 'none'
    else:
        title = soup.select(config_data['title'])[0].get_text().strip()

    focus = []
    if (config_data['focus'] == 'none'):
        focus.append('none')
    else:
        focus_query = soup.select(config_data['focus'])
        # papers_query = soup.find_all(attrs={config_data['papers'].split()[0]: config_data['papers'].split()[1]})
        for f in focus_query:
            focus.append(f.get_text().strip())

    honors = []
    if (config_data['honors'] == 'none'):
        honors.append('none')
    else:
        honors_query = soup.select(config_data['honors'])
        # papers_query = soup.find_all(attrs={config_data['papers'].split()[0]: config_data['papers'].split()[1]})
        for honor in honors_query:
            honors.append(honor.get_text().strip())
    





    # print(soup)
    # print(config_data['name'].split())


    # store scraped data in dictionary
    data = {}
    data['name'] = name
    data['institution'] = institution
    data['keywords'] = keywords
    data['papers'] = papers
    data['email'] = email
    data['education'] = education
    data['title'] = title
    data['focus'] = focus
    data['honors'] = honors
    # data['biography'] = biography
    
    return data



# print(scrape('uiuc', 'https://cs.illinois.edu/about/people/all-faculty/kcchang'))
# print(scrape('dblp', 'https://dblp.org/pid/276/8006.html'))
print(scrape('nike', "https://en.wikipedia.org/wiki/Nike"))
# print(scrape('google', 'https://scholar.google.com/citations?user=sugWZ6MAAAAJ&hl=en&oi=ao'))


# name, email, institution, title, focus area, education, honors, keywords, paper