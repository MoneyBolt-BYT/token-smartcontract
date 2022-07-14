from brownie import MoneyBolt, network, config
from scripts.helpful_scripts import getAccount


def deploy_MB():
    account = getAccount()
    money_bolt = MoneyBolt.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )


def main():
    deploy_MB()
