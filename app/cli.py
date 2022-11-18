import os

import click
from loguru import logger

from app.manager import Manager


@click.group()
@click.option("-v", default=False, help="Debug all the steps", is_flag=True)
@click.option("-o", default="origin", help="Set the origin for the command")
@click.pass_context
def cli(ctx, v, o):
    ctx.ensure_object(dict)

    m = Manager(path_repository=os.getcwd(), logger=logger, origin=o)

    m.set_verbose(v)

    ctx.obj["MANAGER"] = m


@cli.command()
@click.pass_context
def start(ctx):
    """
    Start a new session inside the current branch.
    """

    ctx.obj["MANAGER"].run_start()


@cli.command()
@click.pass_context
def next(ctx):
    """
    Save everything and send to the next person.
    """

    ctx.obj["MANAGER"].run_next()


@cli.command()
@click.pass_context
def done(ctx):
    """
    Finish and put all the work in the original branch.
    """

    ctx.obj["MANAGER"].run_done()


@cli.command()
@click.pass_context
def summary(ctx):
    """
    Show a simple resume of commit counts and last developer.
    """

    ctx.obj["MANAGER"].run_summary()
