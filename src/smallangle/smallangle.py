import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def cmd_group():
    """Main command group for mathematical functions."""
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    type=int,
    default=10,
    help="Number of angles between 0 and 2pi",
    show_default=True,  # Shows the default value in help
)
def sin(number):
    """Calculates sine of x over the interval from 0 to 2pi."""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin(x)": np.sin(x)})
    print(df)


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    type=int,
    default=10,
    help="Number of angles between 0 and 2pi",
    show_default=True,  # Shows the default value in help
)
def tan(number):
    """Calculates tangent of x over the interval from 0 to 2pi."""
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan(x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()  # Call the command group to handle the CLI
