# yeji_ForwardData_Research

## Overview

THis module is responsible for getting desired profile information of well-known websites using xpath.

## Setup

1. Python (3.8.8) pip (23.2.1)

2. All the dependencies needed are in the requirements.txt file. To install all the dependencies, run:

```
pip install -r requirements.txt
```

3. To run the scrape function, just run the file scrape2.py with the run button on the to pright corner of VSCode. It should take in the list of websites and run the scrape function. Add any print statements to see the results as needed.

It is very important to also include an overall breakdown of your repo's file structure. Let people know what is in each directory and where to look if they need something specific. This will also let users know how your repo needs to structured so that your module can work properly

yeji-lim-yeji_forwardData_research/ - requirements.txt - config/
-- econfiguration.ini
--- main config file for experiment
-- configurator.py
--- Code for making configuration file - src/
-- scrape2.py
--- scrape function using xpath
-- scrape.py
--- scrape function using beautifulSoup, does not work for most websites. Just for experiment purposes.
-- google.js
--- scrape function using javaScript, does not work for most websites. Just for experiment purposes. - extension/
--- incomplete, preliminary work for web extension
--- For now, just have a web extension for highlighting a line in a webpage.

Note: if this is a second or latter iteration of a module, you may reuse the old iteration's README as a starting point (you should still update it).

## Functional Design (Usage)

- Takes as input two strings, first one describing what sort of webpage the url is from that correlates to the label of config file, second is the url of desired webpage to scrape. Returns dictionary of all the scraped data. Value is empty if failed to scrape the corresponding data.

```python
    def scrape(website, url):
        ...
        return [
            { 'name': name, 'institution': institution, ..., 'papers': [papers] },
            ...
        ]
```

## Demo video

[https://drive.google.com/file/d/1wxBbj6jd-grqguiuFdlkYW-Rf1xea_jE/view?usp=sharing](https://drive.google.com/file/d/1wxBbj6jd-grqguiuFdlkYW-Rf1xea_jE/view?usp=share_link) 

## Algorithmic Design

The goal is to scrape desired information from webpages in the most efficient way possible, with the least amount of repetitive coding. Therefore, it is important to generalize the scraping function to be able to work properly with all websites

Thus, we use a configuration file to dictate the xpath for all the desired webpages and the information we need to scrape from them. Then, pass that configuration file to the scrape function. The scrape function pulls the matching xpath information based on website name given through its argument, and pulls the information from the webpage, also given to the scrape function by its argument.

After all information is scraped, the scrape function reuturns a dictionary with scraped data.

## Issues and Future Work

- Hard to pull correct xpath out from webpages. Need deep analysis of a webpage's source code to construct the correct xpath. This may take a long time if xpath is complicated. Therefore, we need a way to make this process more efficent.
- One idea is to amke a web extension that allows the users to mark up, such as highlight, lines that correspond to information we want to pull. Once the portion is highlighted, either a. create corresponding xpath if xpath doesn't exist already or b. check if existing xpath is correct and update if needed.
- Config fold formatting is not cosistent. Change lines so that it mathces "education = //\*[following-sibling::h4[text()='Contact Information'] and preceding-sibling::h4[text()='Education']]/text()", where we pull the text directly from xpath and change scrape function in accrodance.

## References

include links related to datasets and papers describing any of the methodologies models you used. E.g.

- Webpages used for experimenting scrape function is present in scrape2.py
- https://medium.com/@mariusbongarts/how-to-build-the-medium-text-highlighter-as-a-chrome-extension-with-web-components-b3feccddcd01 for highlighter extension
