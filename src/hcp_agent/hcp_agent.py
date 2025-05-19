"""Example OpenAI agent that uses the Housecall Pro client."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from openai_agents import Agent, OpenAIAgentClient

from .housecall_client import HousecallClient


@dataclass
class HCPAgent:
    """Wrapper combining an OpenAI agent with the Housecall API."""

    housecall: HousecallClient
    agent: Agent

    @classmethod
    def from_env(cls) -> "HCPAgent":
        housecall = HousecallClient()
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("Missing OPENAI_API_KEY")
        client = OpenAIAgentClient(api_key=openai_api_key)
        agent = Agent(client=client)
        return cls(housecall=housecall, agent=agent)

    def summarize_customer(self, customer_id: int) -> str:
        """Fetch a customer and have the agent summarize it."""
        customer = self.housecall.get_customer(customer_id)
        prompt = f"Summarize the following customer record: {customer}"
        response = self.agent.complete(prompt)
        return str(response)
