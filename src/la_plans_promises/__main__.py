import rich_click as click
from .build import build_declarations, build_plans, build_commitments

@click.group()
def cli():
    pass


def main():
    cli()


@cli.command()
def build():
    build_declarations()
    build_plans()
    build_commitments()


if __name__ == "__main__":
    main()
