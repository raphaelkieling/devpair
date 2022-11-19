import os

import click
from loguru import logger as LoguruLogger

from app.logger import Logger
from app.manager import Manager
from app.timer import Timer


@click.group()
# TODO: Move these options for each command, it's ugly make devpair -v start 3 instead of devpair start 3 -v
@click.option("-v", default=False, help="Debug all the steps", is_flag=True)
@click.option("-o", default="origin", help="Set the origin for the command")
@click.pass_context
def cli(ctx, v, o):
    ctx.ensure_object(dict)

    logger = Logger(logger=LoguruLogger)
    logger.set_verbose(v)

    timer = Timer(logger=logger)

    manager = Manager(path_repository=os.getcwd(), logger=logger, origin=o, timer=timer)

    # It's shared with other commands
    ctx.obj["MANAGER"] = manager


@cli.command()
@click.argument("time", required=False, type=int)
@click.pass_context
def start(ctx, time):
    """
    Start a new session inside the current branch.

    Try to use 'devpair start 10'. It will start the pairing but
    with a 10 minutes timer for you! In the end of the 10 minutes a
    voice will say 'Next dev'
    """

    ctx.obj["MANAGER"].run_start(time)


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
@click.argument("time", required=False, type=int)
@click.pass_context
def timer(ctx, time):
    """
    Create a simple timer, it's good when you forget to put
    a timer value inside the devpair start <TIMER>
    """

    ctx.obj["MANAGER"].run_timer(time)


@cli.command()
@click.pass_context
def summary(ctx):
    """
    Show a simple resume of commit counts and last developer.
    """

    ctx.obj["MANAGER"].run_summary()


@cli.command()
@click.pass_context
def cow(ctx):
    """
    Run a cow test.
    """

    ctx.obj["MANAGER"].run_cow()
