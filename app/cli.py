import os

import click
from loguru import logger as LoguruLogger

from app.logger import Logger
from app.manager import Manager
from app.timer import Timer


@click.group()
@click.option("-v", default=False, help="Debug all the steps", is_flag=True)
@click.option("-o", default="origin", help="Set the origin for the command")
@click.pass_context
def cli(ctx, v, o):
    ctx.ensure_object(dict)

    logger = Logger(logger=LoguruLogger)
    logger.set_verbose(v)

    timer = Timer()

    manager = Manager(path_repository=os.getcwd(), logger=logger, origin=o, timer=timer)

    # It's shared with other commands
    ctx.obj["MANAGER"] = manager


@cli.command()
@click.argument("timer", required=False)
@click.pass_context
def start(ctx, timer):
    """
    Start a new session inside the current branch.
    """

    ctx.obj["MANAGER"].run_start(timer)


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
