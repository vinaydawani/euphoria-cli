from typing import Pattern
from eth_typing import abi
from pyfiglet import Figlet
import web3
import click
import re

from assets import staking, sWAGMI, WAGMI

provider = web3.HTTPProvider("https://api.s0.t.hmny.io")
w3 = web3.Web3(provider)

user_hmny_addr = ""
hmny_addr_pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")

staking_contract = w3.eth.contract(address=staking.address, abi=staking.ABI)
WAGMI_contract = w3.eth.contract(address=WAGMI.address, abi=WAGMI.ABI)
sWAGMI_contract = w3.eth.contract(address=sWAGMI.address, abi=sWAGMI.ABI)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option("--address", "-a", help="Set the account address in '0x' format")
def euphoria(ctx, address):
    if address:
        res = hmny_addr_pattern.match(str(address))
        if res:
            user_hmny_addr = w3.toChecksumAddress(address)
            click.echo(f"Address saved => {address}")
        else:
            return
    if ctx.invoked_subcommand is None:
        f = Figlet(font="larry3d")
        click.echo(f.renderText("euphoria"))
        click.echo("Stake WAGMI and earn harmonious compounding interest (🤝,🤝)")


@euphoria.command()
def info():
    ...


if __name__ == "__main__":
    euphoria()
