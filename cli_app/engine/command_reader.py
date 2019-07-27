from pathlib import Path
from subprocess import check_output, STDOUT
from .log_helper import logger


def read_commands(commands_file):
    logger.info(f"Reading commands from {commands_file}")
    commands = Path(commands_file).read_text()
    return [c for c in commands.split("\n") if len(c.strip()) > 0]


def run_command(command):
    logger.info(f"Running command {command}")
    process = check_output(command, stderr=STDOUT, shell=True)
    return process.decode('utf8').strip().split("\n")
