// const puppeteer = require("puppeteer");
import puppeteer from "puppeteer";

// use xpath and configuration file (json, csv, plain text) to scrape information using the same lines of code for every website.
// convert to Python
// configParser (python config parser)
async function scrapeGoogle() {
  try {
    // Specify the URL of the dev.to tags web page
    const URL =
      "https://scholar.google.com/citations?user=sugWZ6MAAAAJ&hl=en&oi=ao";
      

    // Launch the headless browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    // Go to the webpage
    await page.goto(URL);

    // Perform a function within the given webpage context
    const data = await page.evaluate(() => {
      const result = {};

      // Select all elements with crayons-tag class
      const name = document.getElementById("gsc_prf_in").textContent;

      const institution =
        document.querySelectorAll(".gsc_prf_ila")[0].textContent;

      const keywords = [];
      const keywords__query = document.querySelectorAll(".gsc_prf_inta");
      keywords__query.forEach((keyword) => {
        // Get innerText of each element selected and add it to the array
        keywords.push(keyword.innerText);
      });

      const papers = [];
      const papers__query = document.querySelectorAll(".gsc_a_at");
      papers__query.forEach((paper) => {
        // Get innerText of each element selected and add it to the array
        papers.push(paper.innerText);
      });

      result.name = name;
      result.institution = institution;
      result.keywords = keywords;
      result.papers = papers;

      return result;
    });

    // Print the result and close the browser
    console.log(data);
    await browser.close();
  } catch (error) {
    console.error(error);
  }
}

async function scrapeDBLP() {
  try {
    // Specify the URL of the dev.to tags web page
    const URL = "https://dblp.org/pid/276/8006.html";

    // Launch the headless browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    // Go to the webpage
    await page.goto(URL);

    // Perform a function within the given webpage context
    const data = await page.evaluate(() => {
      const result = {};

      // Select all elements with crayons-tag class
      const name = document.getElementsByClassName("name")[0].textContent;
      const papers = [];
      const papers__query = document.querySelectorAll(".title");
      papers__query.forEach((paper) => {
        // Get innerText of each element selected and add it to the array
        papers.push(paper.innerText);
      });

      result.name = name;
      result.papers = papers;

      return result;
    });

    // Print the result and close the browser
    console.log(data);
    await browser.close();
  } catch (error) {
    console.error(error);
  }
}

scrapeGoogle();
scrapeDBLP();
