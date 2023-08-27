from lxml import html
import requests
from configparser import ConfigParser
from lxml.html import fromstring, tostring
from datetime import datetime

# proxy for google -- scraperApi (free access)
# xpath (ex. preceeding sibling)
# try more websites

# Q: Difference between focus and keywords
# What to do with parsing titles

config = ConfigParser()
config.read('config/configuration.ini')


# eval

def scrape(website, url):
    # print(website)

    # Request the page
    page = requests.get(url, verify=False)
    if (website == "google"):
        payload = {'api_key': '8433e59abd6def584593acab9c9d2d73', 'url': url}

        page = requests.get('http://api.scraperapi.com', params=payload)
        # print('page text: ', page.text)
    
    # Parsing the page
    # (We need to use page.content rather than
    # page.text because html.fromstring implicitly
    # expects bytes as input.)
    tree = html.fromstring(page.content)
    # print("tree: ", tostring(tree)) 
    
    # set comfig to correct website
    config_data = config[website]








    # # scrape info
    name = ''
    if (config_data['name'] == 'none'):
        name = 'none'
    else:
        name_query = tree.xpath(config_data['name'])
        # print('name query: ', name_query)
        if (len(name_query) == 0):
            # print('cant find name')
            name = 'none'
        else:
            # print(name_query[0].text)
            name = name_query[0].text.strip()

    institution = ''
    if (config_data['institution'] == 'none'):
        institution = 'none'
    else:
        institution_query = tree.xpath(config_data['institution'])
        if (len(institution_query) == 0):
            institution = 'none'
        else:
            institution = institution_query[0].text.strip()


    papers = []
    if (config_data['papers'] == 'none'):
        papers.append('none')
    else:
        papers_query = tree.xpath(config_data['papers'])
        # print('papers query: ', papers_query)
        if (len(papers_query) == 0):
            # print('none')
            papers.append('none')
        else:
            for paper in papers_query:
                if (paper.text is None):
                    continue
                papers.append(paper.text.strip())

    email = ''
    if (config_data['email'] == 'none'):
        email = 'none'
    else:
        email_query = tree.xpath(config_data['email'])
        if (len(email_query) == 0):
            email = 'none'
        else :
            email = email_query[0].text.strip()

    education = []
    if (config_data['education'] == 'none'):
        education.append('none')
    else:
        education_query = tree.xpath(config_data['education'])
        print("edu query: ", education_query)
        if (len(education_query) == 0):
            # print('no edu')
            education.append('none')
        else :
            for e in education_query:
                if (e is None):
                    continue
                education.append(e.strip())

    titles = []
    if (config_data['title'] == 'none'):
        titles.append('none')
    else:
        title_query = tree.xpath(config_data['title'])
        if (len(title_query) == 0):
            # print('no title query')
            titles.append('none')
        else :
            # print('title query: ',  title_query)
            for title in title_query:
                if (title.text is None):
                    continue
                titles.append(title.text.strip())
        

    focus = []
    if (config_data['focus'] == 'none'):
        focus.append('none')
    else:
        focus_query = tree.xpath(config_data['focus'])
        if (len(focus_query) == 0):
            focus.append('none')
        else :
            # print('focus query: ', focus_query)
            for f in focus_query:
                if (f.text is None):
                    continue
                focus.append(f.text.strip())
                # print('yo')

    honors = []
    if (config_data['honors'] == 'none'):
        honors.append('none')
    else:
        honors_query = tree.xpath(config_data['honors'])
        if (len(honors_query) == 0):
            honors.append('none')
        else :
            for honor in honors_query:
                if (honor.text is None):
                    continue
                honors.append(honor.text.strip())

    biography = []
    if (config_data['biography'] == 'none'):
        biography.append('none')
    else:
        biography_query = tree.xpath(config_data['biography'])
        if (len(biography_query) == 0):
            biography.append('none')
        else :
            for bio in biography_query:
                if (bio.text is None):
                    continue
                biography.append(bio.text.strip())

    





    # print(soup)
    # print(config_data['name'].split())


    # store scraped data in dictionary
    data = {}
    data['name'] = name
    data['institution'] = institution
    data['papers'] = papers
    data['email'] = email
    data['education'] = education
    data['titles'] = titles
    data['focus'] = focus
    data['honors'] = honors
    data['biography'] = biography
    
    return data

test = [
        ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/kcchang'],
        ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/angrave'],
        ['dblp', 'https://dblp.org/pid/276/8006.html'],
        ['dblp', 'https://dblp.org/pid/341/0850.html'],
        ['google', 'https://scholar.google.com/citations?user=sugWZ6MAAAAJ&hl=en&oi=ao'],
        ['google', 'https://scholar.google.com/citations?user=VS9wzBsAAAAJ&hl=en&oi=ao'],
        ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/asanovic.html'],
        ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/amalaa.html'],
        ['usc', 'https://www.cs.usc.edu/directory/faculty/profile/?lname=Adleman&fname=Leonard'],
        ['carnegie', 'https://csd.cmu.edu/people/faculty/umut-acar'],
        ['carnegie', 'https://csd.cmu.edu/people/faculty/anil-ada'],
        ['mit', 'https://www.eecs.mit.edu/people/hal-abelson/'],
        ['harvard', 'https://crcs.seas.harvard.edu/people/flavio-du-pin-calmon'],
        ['uchicago', 'https://cs.uchicago.edu/people/t-andrew-binkowski/'],
        ['uchicago', 'https://cs.uchicago.edu/people/laszlo-babai/'],
        ['johns_hopkins', 'https://www.cs.jhu.edu/faculty/yair-amir/'],
        ['upenn', 'https://directory.seas.upenn.edu/sebastian-angel/'],
        ['caltech', 'https://www.cms.caltech.edu/people/adames'],
        ['caltech', 'https://www.cms.caltech.edu/people/yaser'],
        ['duke', 'https://scholars.duke.edu/person/robert.calderbank'],
        ['northwestern', 'https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/khuller-samir.html'],
        ['dartmouth', 'https://web.cs.dartmouth.edu/people/michael-casey'],
        ['dartmouth', 'https://web.cs.dartmouth.edu/people/andrew-thomas-campbell'],
        ['brown', 'https://cs.brown.edu/people/faculty/nayanian/'],
        ['brown', 'https://cs.brown.edu/people/faculty/ugur/'],
        ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/thomas-beckers'],
        ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/gautam-biswas'],
        ['rice', 'https://profiles.rice.edu/faculty/vladimir-braverman'],
        ['rice', 'https://profiles.rice.edu/faculty/michael-burke'],
        ['wash_u', 'https://engineering.wustl.edu/faculty/Kunal-Agrawal.html'],
        ['wash_u', 'https://engineering.wustl.edu/faculty/Ian-Bogost.html'],
        ['nortre_dame', 'https://cse.nd.edu/faculty/karla-badillo-urquiola/'],
        ['nortre_dame', 'https://cse.nd.edu/faculty/kevin-bowyer/'],
        ['emory', 'https://www.cs.emory.edu/people/faculty/individual.php?NUM=24'],
        ['emory', 'https://www.cs.emory.edu/people/faculty/individual.php?NUM=350'],
        # ['virginia', 'https://engineering.virginia.edu/faculty/nada-basit']

        # ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/kcchang'],
        # ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/angrave'],
        # ['dblp', 'https://dblp.org/pid/276/8006.html'],
        # ['dblp', 'https://dblp.org/pid/341/0850.html'],
        # ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/asanovic.html'],
        # ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/amalaa.html'],
        # ['usc', 'https://www.cs.usc.edu/directory/faculty/profile/?lname=Adleman&fname=Leonard'],
        # ['carnegie', 'https://csd.cmu.edu/people/faculty/umut-acar'],
        # ['carnegie', 'https://csd.cmu.edu/people/faculty/anil-ada'],
        # ['mit', 'https://www.eecs.mit.edu/people/hal-abelson/'],
        # ['harvard', 'https://crcs.seas.harvard.edu/people/flavio-du-pin-calmon'],
        # ['uchicago', 'https://cs.uchicago.edu/people/t-andrew-binkowski/'],
        # ['uchicago', 'https://cs.uchicago.edu/people/laszlo-babai/'],
        # ['johns_hopkins', 'https://www.cs.jhu.edu/faculty/yair-amir/'],
        # ['upenn', 'https://directory.seas.upenn.edu/sebastian-angel/'],
        # ['caltech', 'https://www.cms.caltech.edu/people/adames'],
        # ['caltech', 'https://www.cms.caltech.edu/people/yaser'],
        # ['duke', 'https://scholars.duke.edu/person/robert.calderbank'],
        # ['northwestern', 'https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/khuller-samir.html'],
        # ['dartmouth', 'https://web.cs.dartmouth.edu/people/michael-casey'],
        # ['dartmouth', 'https://web.cs.dartmouth.edu/people/andrew-thomas-campbell'],
        # ['brown', 'https://cs.brown.edu/people/faculty/nayanian/'],
        # ['brown', 'https://cs.brown.edu/people/faculty/ugur/'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/thomas-beckers'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/gautam-biswas'],
        # ['rice', 'https://profiles.rice.edu/faculty/vladimir-braverman'],
        # ['rice', 'https://profiles.rice.edu/faculty/michael-burke'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Kunal-Agrawal.html'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Ian-Bogost.html'],

        # ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/kcchang'],
        # ['uiuc', 'https://cs.illinois.edu/about/people/all-faculty/angrave'],
        # ['dblp', 'https://dblp.org/pid/276/8006.html'],
        # ['dblp', 'https://dblp.org/pid/341/0850.html'],
        # ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/asanovic.html'],
        # ['berkeley', 'https://www2.eecs.berkeley.edu/Faculty/Homepages/amalaa.html'],
        # ['usc', 'https://www.cs.usc.edu/directory/faculty/profile/?lname=Adleman&fname=Leonard'],
        # ['carnegie', 'https://csd.cmu.edu/people/faculty/umut-acar'],
        # ['carnegie', 'https://csd.cmu.edu/people/faculty/anil-ada'],
        # ['mit', 'https://www.eecs.mit.edu/people/hal-abelson/'],
        # ['harvard', 'https://crcs.seas.harvard.edu/people/flavio-du-pin-calmon'],
        # ['uchicago', 'https://cs.uchicago.edu/people/t-andrew-binkowski/'],
        # ['uchicago', 'https://cs.uchicago.edu/people/laszlo-babai/'],
        # ['johns_hopkins', 'https://www.cs.jhu.edu/faculty/yair-amir/'],
        # ['upenn', 'https://directory.seas.upenn.edu/sebastian-angel/'],
        # ['caltech', 'https://www.cms.caltech.edu/people/adames'],
        # ['caltech', 'https://www.cms.caltech.edu/people/yaser'],
        # ['duke', 'https://scholars.duke.edu/person/robert.calderbank'],
        # ['northwestern', 'https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/khuller-samir.html'],
        # ['dartmouth', 'https://web.cs.dartmouth.edu/people/michael-casey'],
        # ['dartmouth', 'https://web.cs.dartmouth.edu/people/andrew-thomas-campbell'],
        # ['brown', 'https://cs.brown.edu/people/faculty/nayanian/'],
        # ['brown', 'https://cs.brown.edu/people/faculty/ugur/'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/thomas-beckers'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/gautam-biswas'],
        # ['rice', 'https://profiles.rice.edu/faculty/vladimir-braverman'],
        # ['rice', 'https://profiles.rice.edu/faculty/michael-burke'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Kunal-Agrawal.html'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Ian-Bogost.html'],

        # ['brown', 'https://cs.brown.edu/people/faculty/ugur/'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/thomas-beckers'],
        # ['vanderbilt', 'https://engineering.vanderbilt.edu/bio/gautam-biswas'],
        # ['rice', 'https://profiles.rice.edu/faculty/vladimir-braverman'],
        # ['rice', 'https://profiles.rice.edu/faculty/michael-burke'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Kunal-Agrawal.html'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Ian-Bogost.html'],
        # ['rice', 'https://profiles.rice.edu/faculty/vladimir-braverman'],
        # ['rice', 'https://profiles.rice.edu/faculty/michael-burke'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Kunal-Agrawal.html'],
        # ['wash_u', 'https://engineering.wustl.edu/faculty/Ian-Bogost.html']
        ]

def scrape_test(testing_batch):
    start = datetime.now()
    for test in testing_batch:
        print(scrape(test[0], test[1]))
        # scrape(test[0], test[1])
    end = datetime.now()
    duration = (end - start).total_seconds()
    print(duration)

scrape_test(test)


# test 100 univerity faculty
# average time it takes for each website

# Princeton weird - can't find text?
# Yale impossible...in a paragraph form
# Caltech email protected against scraping, different tab for paper info
# Duke biography has "more" button
# Northwestern name formatted weridly (div inside h1) so cannot scrape name, scraping only edu hard because cannot isolate edu p tag with the following p tag, publicaitons formatted in a weird way so that it's hard to get all paper info
# Dartmouth has the same problem as Northwestern name, cannot get title, focus has backslash I cannot seem to get off
# Brown email has the similar problem as Dartmouth title 

# with warnings duration = 49.982304 sec

