# Melio's Cookiecutter Data Science

This repository is forked from [cookiecutter-data-science](http://drivendata.github.io/cookiecutter-data-science/) from driven data for  Melio's data science workflow.

## Table of Content

1. [Requirements to use the cookiecutter template](#requirements-to-use-the-cookiecutter-template)
2. [To start a new project](#to-use-the-melio-cookiecutter-data-science-template)
   - [Cookiecutter project structure](#the-resulting-directory-structure)
3. [Recommendation on using the template](#recommendation-on-using-the-template)
   - [Logging module](#logging-module)
   - [Model cards](#model-cards)
   - [Testing framework](#testing-framework)
4. [Contribute](#contribute)

## Requirements to use the cookiecutter template
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## To start a new project
------------

    cookiecutter https://github.com/melioconsulting/cookiecutter-data-science


## The resulting directory structure
------------

The directory structure of your new project looks like this:

```
    ├── LICENSE
    |
    ├── .devcontainer.json    <- VSCode devcontainer declaration
    ├── .env                  <- env files where all secrets go
    ├── .gitignore            <- gitignore so you don't commit random stuff
    ├── .pylintrc             <- so we can have consistent code style score between different repos
    |
    ├── azure-pipelines.yml   <- Azure DevOps build pipeline declaration
    ├── Makefile              <- Makefile with commands like `make data` or `make train`
    ├── README.md             <- The top-level README for developers using this project.
    ├── data
    │   ├── external          <- Data from third party sources.
    │   ├── interim           <- Intermediate data that has been transformed.
    │   ├── processed         <- The final, canonical data sets for modeling.
    │   └── raw               <- The original, immutable data dump.
    │
    ├── docs                   <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models                 <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references             <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures            <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py               <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                    <- Source code for use in this project.
    │   ├── __init__.py        <- Makes src a Python module
    │   ├── pipeline.py        <- Scripts to orchestrate the whole pipeline
    │   │
    │   ├── data               <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features           <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models             <- Scripts to train models and then use trained models to make
    │   │   │                     predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization      <- Scripts to create exploratory and results oriented visualizations
    │   |    └── visualize.py
    │   │
    │   └── utilities          <- Scripts that are common between the other folders go here
    │        └── util.py       <- utility file that stores functions that are common across scripts
    │
    └── tests                  <- folders where all pytest files sit
    |
    |
    └── tox.ini                <- tox file with settings for running tox; see tox.readthedocs.io
    |
    └── logging.ini            <- logging configuration using fileConfig() method
```

## Recommendation on using the template

The cookiecutter template includes a couple of tools to improve the development and deployment cycle. These are some of the recommendations.

### Logging module

The logging is configured through `logging.ini`.

The logging configuration is set up per module as below, with a couple of things to watch out for:

  1. Construc message lazily to improve logging performance.
     - use logger.info('This is message: %s', message) rather than logger.info(f'This is {message}').
  2. Capture traceback properly
     - for handled exceptions: logger.error(e, exc_info=True)
     - for unhadled: logger.error('uncaught exception: %s', traceback.format_exc())
  3. Two log files are generated: app_debug.log and app_warning.log
     - Use TimedRotatingFileHandler for debug to save space. Rotating every 7 days and back up 5 copies.
     - Use FileHandler for warnings and above logs.
  4. Use json formatter for log files. This is helpful to generate machine-readable logs.

```
# make_dataset.py
import logging.config
import traceback

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def word_count(myfile):
    try:
        # count the number of words in a file, myfile, and log the result
        with open(myfile, 'r+') as f:
            file_data = f.read()
            logger.info('Line: %s', file_data)
            return file_data
    except OSError as e:
        logger.error(e, exc_info=True)
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())
        return False

if __name__ == '__main__':
    word_count('myfile.txt')
```
### Model Cards

##TODO: Chuene update here.

### Testing Framework

##TODO: Merelda update here.



## Contribute
------------

To contribute, follow the steps below:

#### **Step 1:**

Change what you need in the `{{ cookiecutter.repo_name }}` repository or the `cookiecutter.json` file

#### **Step 2:**

Once finished updating, submit a Pull Request for review.