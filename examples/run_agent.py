"""Small demo for the HCPAgent."""

import argparse

from hcp_agent.hcp_agent import HCPAgent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer_id", type=int, required=True)
    args = parser.parse_args()

    agent = HCPAgent.from_env()
    summary = agent.summarize_customer(args.customer_id)
    print(summary)


if __name__ == "__main__":
    main()
