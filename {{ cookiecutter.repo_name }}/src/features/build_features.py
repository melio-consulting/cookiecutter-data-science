# -*- coding: utf-8 -*-
import click
import traceback
import logging.config
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def pipeline():
    logger.info('Start building features.')

@click.command()
@click.argument('input_filepath', default='data/interim', type=click.Path(exists=True))
@click.argument('output_filepath', default='data/processed', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn cleaned data from (../interim) into
        training data ready to be trained (saved in ../processed).
    """
    logger.info(f'Read from {input_filepath}, write to {output_filepath}.')

if __name__ == '__main__':

    load_dotenv(find_dotenv())

    #pylint: disable = no-value-for-paramete
    main()
