import click
from app.manager import Manager
from loguru import logger

m = Manager(
    path_repository="/Users/kieling/Documents/projects/personal/test-github",
    logger=logger
)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--verbose', default=False, help='Debug all the steps')
def start(verbose):
    m.set_verbose(verbose)
    m.run_start()


@cli.command()
@click.option('--verbose', default=False, help='Debug all the steps')
def next(verbose):
    m.set_verbose(verbose)
    m.run_next()


@cli.command()
@click.option('--verbose', default=False, help='Debug all the steps')
def done(verbose):
    m.set_verbose(verbose)
    m.run_done()