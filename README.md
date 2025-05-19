# AiSync

AiSync provides a starting point for building AI agents that interact with the [Housecall Pro API](https://docs.housecallpro.com/docs/housecall-public-api/a4ca20a18010c-housecall-v1-api).
The agents are implemented using the [OpenAI Agent SDK](https://openai.github.io/openai-agents-python/).

## Overview

This repository contains a small Python package with helper classes for communicating
with the Housecall Pro API and defining OpenAI-based agents. The code is intentionally
minimal and is meant as a starting point for your own experiments.

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables:

   - `HOUSECALL_API_TOKEN` – your Housecall Pro API token
   - `OPENAI_API_KEY` – your OpenAI API key

3. Run the example agent:

   ```bash
   python examples/run_agent.py --customer_id 123
   ```

The example merely fetches a customer record from Housecall Pro and lets the OpenAI
agent reason about it. Extend the logic to suit your needs.

## License Notes

The OpenAI Agent SDK is released under an open-source license. Consult the
[project page](https://openai.github.io/openai-agents-python/) for details.
The Housecall Pro API documentation does not clearly specify a license; please
review their terms of service before using it in a production setting.
