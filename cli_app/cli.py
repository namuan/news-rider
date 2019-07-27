from argparse import ArgumentParser

from .engine.markdown_exporter import md_file_path
from .engine.notifier import notify_user
from .engine.workflow import orchestrate


def parse_args():
    parser = ArgumentParser(
        description="A simple script to read titles for given urls and send tweets"
    )
    parser.add_argument('-c', '--commands-file', type=str, required=True, help='File name with all the commands.')
    parser.add_argument('-d', '--dry-run', action="store_true", help='Avoid sending tweet if set to True.')
    return parser.parse_args()


def main():
    args = parse_args()
    orchestrate(args.commands_file, args.dry_run)
    notify_user("Tech News", f"Markdown File ready at {md_file_path}")
