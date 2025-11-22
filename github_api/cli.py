from email.policy import default

import click
from github_api.github_api import get_user_events
from github_api.utils import format_event


@click.group()
def cli():
    pass

@cli.command()
@click.argument('username')
@click.option('--limit', default=10, type=int)
def cli(username, limit):
    try:
        events = get_user_events(username, limit)
        if not events:
            click.secho(f"Error: {username} has no events", fg="red")
            return

        click.secho("Last activities:", fg="green")
        for event in events:
            msg = format_event(event)
            click.echo(f"- {msg}")  # <- Affichage comme tu veux
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")

if __name__ == "__main__":
    cli()