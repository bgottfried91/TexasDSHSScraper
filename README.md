# TexasDSHSScraper
This is a script to help assist in retrieving data related to COVID-19.

## Current behavior
The script will download all xlsx files from https://dshs.texas.gov/coronavirus/AdditionalData.aspx and place them inside dataDir/\<current date\>/.
  
## Requirements
You must have Python 3 installed. [This link should provide you with the correct link for installing Python](https://www.python.org/downloads/). If you're on MacOS or Linux, it may already be installed. To test if it's installed, run `python -h` in a terminal window.

You'll also need to install the Python package installer pip if it didn't come packaged with your Python installation. [Instructions for doing so here if necessary](https://www.makeuseof.com/tag/install-pip-for-python/); again, if on MacOS or Linux it may already be installed. To test if it's installed, just run `pip -v` in your terminal window.
  
## Setup
[Git clone the repo](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) or download the zip archive of it and unzip it.

Open a command prompt window (on Windows) or terminal (MacOS/Linux) and navigate to the directory containing the files (the directory created by your git clone or the unzipped archive directory). Run `pip install -r requirements.txt`. You're now all set up!

To run the script, simply run `python app.py`. If you want more information on what the script is doing, you can see the debug-level logging with `python app.py -v`.
