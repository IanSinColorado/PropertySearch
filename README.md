# Python Tool to Search for Properties with the Datafinity API

This software tool is a property search engine that uses the [Datafinity API](https://developer.datafiniti.co/docs/get-started) more specifically the property data. This tool allows the user to search for properties from Datafinity's API and returns a list of properties and their name, address, date of most recent update, city, and max price.


## Requirements

* Knowledge of how to use a command terminal
* A local clone of this repository
* Python installed locally
* Anaconda and Conda installed locally


## Usage
### Conda Environment Setup

This section will serve as a guide to set up the proper conda environment with the required libraries.

1. Clone this repository into a directory of your choosing
2. Verify you have [conda installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html): open a terminal and run `conda --version`. If a version number is returned, you have conda or miniconda installed.
3. Path to where you cloned the repository in the terminal of your choosing
4. Run the command `conda env create -f environment.yml` to create a new environment with the necessary libraries
5. Accept the creation and allow the dependencies to be installed
6. Activate the new environment with `conda activate JG-ETL` and have fun! 

**Other Conda Notes:**
- Use `conda --version` to check the version of conda
- Use `conda env list` to see your current conda environments
- Use `conda remove -n JG-ETL --all` to remove the environment
- Use `conda env update -f environment.yml` to update the environment after any changes to the environment.yml file

### Using the Tool:

This tool is made to run on the command line. The user has the option of using the interactive menu and be given the option to give specific search criteria including country, cities, property status, province (or state such as Colorado), max price, and number of search results to return. The user can also choose to use the current query, hardcoded in propertySearch.py

1. Open a terminal
2. Verify you have [python installed](https://www.python.org/downloads/): run `python --version`. If a version number is returned, you have python installed.
3. Path to where this repository is cloned
4. Create/Update the conda environment with the steps above
5. Run `python propertySearch.py`
6. Read the prompts and respond in the terminal