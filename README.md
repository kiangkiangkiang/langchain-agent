# Build The First LangChain Agent

This tutorial is designed for Data Scientists who want to harness the power of LangChain to build, customize, and deploy intelligent agents for their projects. The guide is split into several focused sections to help you understand key concepts and get started quickly.

## Getting Start

#### Prerequisites

- Python 3.10
- A working knowledge of Python and basic AI concepts
- OpenAI API key (if using OpenAI models)

#### Setup Environment

1. Create a `.env` file in your project (Sample [Here](.env.template))
2. Export environment: `export PYTHONPATH="$PWD/src"`

## Creating a Toy Agent

Refers to [here](./examples/create_toy_agent.py).

### Tools 

jf


## Adding Custom Strategy to Your Agent

## Managing Memory in Agents

## Deploying Your Agent Chatbot

curl -X POST http://localhost:5000/text_ask \
     -H "Content-Type: application/json" \
     -d '{"input": "你知道王小龍在哪嗎"}'