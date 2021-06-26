from bullet import Bullet, colors, styles
from pip._internal.cli.main_parser import create_main_parser
from pip._internal.commands.configuration import ConfigurationCommand

def get_environment_config():
    import ipdb; ipdb.set_trace()
    command = ConfigurationCommand()
    command.list_values()

def main():
    do_exit = False
    while not do_exit:
        cli = Bullet(
            prompt='\nGiftwrap Menu',
            choices = [
                '1. Get current environment config',
                '2. Package research'
                '3. Scan package for entry points',
                '4. Run giftwrap pypi server',
                '5. Exit'
            ],
        )
        result = cli.launch()
    :wqa

