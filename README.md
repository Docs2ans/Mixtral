# Docs2Answer- Intelligent Documentation Chatbot

One stop solution to transform all of your docs into an efficient LLM-powered Chatbot.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Docs2Answer is an advanced natural language processing (NLP) project designed to revolutionize the way users interact with documentation. Leveraging cutting-edge language models, specifically Large Language Models (LLM), Docs2Answer transforms static documentation into a dynamic and interactive conversational experience. Now, users can effortlessly obtain information and answers to their queries by engaging in a conversation with their personal Docs bot.

## Features

1. LLM-powered Conversations: DocBot utilizes state-of-the-art Large Language Models to comprehend and respond to user queries with high accuracy, providing a more natural and intuitive interaction.
2. Document Understanding: The system processes and comprehends extensive documentation, allowing users to extract relevant information through context-aware conversations.
3. Dynamic Responses: DocBot generates dynamic responses, adapting to the user's questions and providing detailed explanations, examples, or references within the documentation.

## Installation and Setup

Follow the steps below to setup the project locally on your system.

### Prerequisites

System needs to have Python 3.10 installed.

### Installation Steps

1. Clone the Repository.
2. The project uses LaMini-T5-738M as the LLM engine, the folder in the repo contains all tokenizer and config files. However, the pytorch_model.bin file for the mentioned model has to be downloaded seperately from Huggingface. Download the file [here](https://huggingface.co/MBZUAI/LaMini-T5-738M/tree/main) and move it into the LaMini-738M folder.
3. Install the required libraries using pip.
   `pip install -r requirements.txt`
4. Create 2 empty directories 'db' and 'docs'.
5. Add your documentation pdf files to the 'docs' folder.
6. Run ingest.py
   `python ingest.py`
7. Open a terminal and run the following command
   `uvicorn server:app --reload`
8. Server is now live with your data

## Contributing

We welcome contributions to enhance the capabilities of Docs2Answer. Check out our [CONTRIBUTING.md](CONTRIBUTING.md) guide to get started.

## License

DocBot is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


