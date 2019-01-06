# cannabis-strains

Scraping of online reviews of cannabis strains and performing exploratory data analysis, including data cleaning, data transformations, and unsupervised association rule learning to mine associations between strain flavours and their medicinal properties.

Uses a combination of `Selenium` and `BeautifulSoup` + `requests` to do the scraping portion, followed by data manipulation and visualization with `pandas` and `Plotly`, and association rule learning with `apriori`.

To reproduce:

1. Clone the repository or download as ZIP and unzip it somewhere. 

2. Run `link_crawl.py` using Python 3. You'll need the [Selenium Python bindings](https://selenium-python.readthedocs.io/#) as well as [the latest version of Chromedriver](http://chromedriver.chromium.org/).

3. Then run `strain_scrape_standard.py` to produce a CSV file with all the strain data nicely organized into columns and labelled.

4. Finally, use [Jupyter notebook](https://jupyter.org/) to run `cannabis_strains_EDA.ipynb`, where you can run individual cells, the entire notebook, or save the output to HTML. The HTML version of the notebook is [available on my site](https://www.intelligencerefinery.io/portfolio/cannabis-eda/).
