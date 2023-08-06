import requests
from bs4 import BeautifulSoup

'''
Goal: Scrape all necessary MLBTradeRumors links to return arbitration data
      into a dataframe (data not readily/easily available)
--------------------------------------------------------------------------------
Inputs: link (string for website link)

Returns: N/A, but exports scraped data to csv, downloaded for additional data
         gathering performed outside code
'''
def scrape_mlbtr(link):
    # Making a GET request
    r = requests.get(link)

    # check status code for response received
    #print(r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Scrapes the table linked in url
    s = soup.find('body', class_ = 'mlbtr').find('div', id = 'widget').find('div', id = 'widget_inner').find_all('table')
    df = pd.read_html(str(s))[0]

    # Names df according to the offseason, a.k.a. the year in the url + 1
    # e.g. 2016 data goes towards the 2017 offseason arbitration class
    df_name = 'mlbtr_arb' + str(int(link[-5:-1]) + 1) + '.csv'
    scraped_df = df.to_csv(df_name, index= True)

# Saves to local runtime, would then download each csv and add additional data on position

# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2016/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2015/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2014/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2013/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2012/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2011/')
# scrape_mlbtr('https://transactions.mlbtraderumors.com/widget/arbitration-submissions/2010/')
