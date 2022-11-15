import click
import os
from app.manager import Manager
from loguru import logger

m = Manager(
    path_repository=os.getcwd(),
    logger=logger
)

@click.group()
@click.option('-v', default=False, help='Debug all the steps', is_flag=True)
@click.pass_context
def cli(ctx, v):
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = v

@cli.command()
@click.pass_context
def start(ctx):
    verbose = ctx.obj['VERBOSE']
    """
        Start a new session inside the current branch.
    """
    m.set_verbose(verbose)
    m.run_start()


@cli.command()
@click.pass_context
def next(ctx):
    verbose = ctx.obj['VERBOSE']
    """
        Save everything and send to the next person.
    """
    m.set_verbose(verbose)
    m.run_next()


@cli.command()
@click.pass_context
def done(ctx):
    verbose = ctx.obj['VERBOSE']
    """
        Finish and put all the work in the original branch.
    """
    m.set_verbose(verbose)
    m.run_done()