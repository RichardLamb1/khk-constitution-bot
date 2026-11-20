# Student Organization Governance Bot

`/ask` answers questions from the Constitution and Bylaws and cites the relevant articles and sections. Replies appear in the channel where the command was used. The bot keeps the last five question-and-answer pairs in memory for each member in each channel.

## Setup

1. Install the dependencies with Python 3.10 or newer.

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

2. Place `constitution.pdf` and `bylaws.pdf` next to `extract_docs.py` and run `python extract_docs.py`. Review the generated `constitution.md` and `bylaws.md` for missing text, article and section labels, and list formatting. Rerun the extractor after document changes and restart the bot to load the updated text.

3. Create a Discord application. Install its bot in your server with the `bot` and `applications.commands` scopes and grant it View Channel and Send Messages in the channels where it will answer. Leave Message Content Intent disabled. [Discord bot setup](https://docs.discord.com/developers/quick-start/getting-started)

4. Deploy `gpt-5-nano` in Azure OpenAI. If you are using Azure for Students, check that your subscription and region can deploy the model and that the deployment is eligible for your credits. [Azure model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models), [Azure for Students](https://azure.microsoft.com/en-us/free/students/)

5. Run `cp .env.example .env` and fill in the Discord bot token, Azure resource endpoint, API key, deployment name, and API version. Use the resource URL such as `https://your-resource-name.openai.azure.com`. Set `ORGANIZATION_NAME` to personalize the prompt.

6. Run `python bot.py` and try `/ask` with a question whose answer and citation you can verify in the documents.

## Azure request settings

The bot uses `reasoning_effort="minimal"` and `max_completion_tokens=500`, which covers reasoning and visible output. Azure's `gpt-5-nano` deployment uses its default temperature. [Azure reasoning model settings](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning), [Chat Completions reference](https://learn.microsoft.com/en-us/azure/foundry/reference/rest/chat-create-chat-completion)

The instructions and both documents form the same first message on every request. Azure automatically caches eligible matching prefixes starting at 1,024 tokens. [Azure prompt caching](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/prompt-caching)
