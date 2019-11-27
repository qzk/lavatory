"""Main entry point."""
import logging

import click
import coloredlogs
import os

from .commands.policies import policies
from .commands.purge import purge
from .commands.stats import stats

LOG = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', count=True, help='Increases logging level.')
@click.pass_context
def root(ctx, verbose):
    """Lavatory is a tool for managing Artifactory Retention Policies."""
    LOG.debug('Passed args: %s, %s', ctx, verbose)
    coloredlogs.install(level=0, fmt='[%(levelname)s] %(name)s %(message)s', isatty=True)
    logging.root.setLevel(logging.INFO)  # colored logs likes to change root level
    verbosity = logging.root.getEffectiveLevel() - 10 * verbose or 1
    logging.getLogger(__package__).setLevel(verbosity)

    if verbosity < logging.DEBUG:
        logging.root.setLevel(verbosity)


@root.command()
def version():
    """Print version information."""
    # this actually still isn't working but i'm lazy
    base_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    version_file = os.path.join(base_path, 'version')
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            version = f.read().strip()
        click.echo(version)
    else:
        click.echo('DEVELOPMENT')


root.add_command(policies)
root.add_command(purge)
root.add_command(stats)

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    root()
