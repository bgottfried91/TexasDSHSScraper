import os
import re
import sys
import requests
import logging
import pprint
import argparse
from datetime import date
from bs4 import BeautifulSoup

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
    args=parser.parse_args()
    if(args.verbose):
        logLevel="DEBUG"
    else:
        logLevel="INFO"
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logLevel)
    today=date.today()
    todayString=today.strftime("%m-%d-%Y")
    logging.debug(f"Checking for existence of {todayString} directory")
    dataDir=f"dataDir/{todayString}"
    if not os.path.isdir(dataDir):
        logging.debug(f"{dataDir} directory does not exist, creating")
        os.makedirs(dataDir,exist_ok=True)
    os.chdir(dataDir)
    logging.info(f"Files will be written to {os.path.abspath(os.getcwd())}")
    indexUrl="https://dshs.texas.gov/coronavirus/AdditionalData.aspx"
    indexRoot="https://dshs.texas.gov"
    logging.info(f"Retrieving xlxs links from {indexUrl}")
    index=requests.get(indexUrl)
    indexParse=BeautifulSoup(index.content,'html.parser')
    xlsxLinks=indexParse.find_all("a",{"href":re.compile(".*\.xlsx$")})
    logging.debug(f"Following xlxs links found in {indexUrl}: {pprint.pformat(xlsxLinks)}")
    for link in xlsxLinks:
        xlsxUrl=link['href']
        if not re.compile("https://.*").match(xlsxUrl):
            xlsxUrl=indexRoot+xlsxUrl
        fileName=re.compile(".*/(.*\.xlsx)").match(xlsxUrl).group(1)
        logging.debug(f"Filename is {fileName}")
        logging.info(f"Processing link {xlsxUrl}")
        xlsxResponse=requests.get(xlsxUrl,stream=True)
        logging.debug(f"Writing link {xlsxUrl} to {os.path.abspath(os.getcwd())}/{fileName}")
        with open(fileName,"wb") as f:
            for chunk in xlsxResponse.iter_content(chunk_size=16*1024):
                f.write(chunk)

if __name__ == '__main__':
    main()