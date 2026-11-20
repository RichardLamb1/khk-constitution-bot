# Constitution Bot - A Student Organization Governance Bot

Mention the bot in a server message to ask about the Constitution or Bylaws. The bot replies in the same channel or thread with relevant article and section citations. It keeps the last five question-and-answer pairs in memory for each member in each channel or thread.

## Setup

1. Install the dependencies with Python 3.10 or newer.

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

2. Place `constitution.pdf` and `bylaws.pdf` next to `extract_docs.py` and run `python extract_docs.py`. Review the generated `constitution.md` and `bylaws.md` for missing text, article and section labels, and list formatting. Rerun the extractor after document changes and restart the bot to load the updated text.

3. Create a Discord application and install it in your server with the `bot` scope. Give it View Channel, Send Messages, and Read Message History in the channels where it will answer. Grant Send Messages in Threads for thread replies. Leave Message Content Intent disabled. Discord still delivers the content of messages that mention the bot. [Discord bot setup](https://docs.discord.com/developers/quick-start/getting-started), [Gateway intents](https://docs.discord.com/developers/events/gateway#message-content-intent)

4. Deploy `gpt-5-nano` in Azure OpenAI. If you are using Azure for Students, check that your subscription and region can deploy the model and that the deployment is eligible for your credits. [Azure model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models), [Azure for Students](https://azure.microsoft.com/en-us/free/students/)

5. Run `cp .env.example .env` and fill in the Discord bot token, Azure resource endpoint, API key, deployment name, and API version. Use the resource URL such as `https://your-resource-name.openai.azure.com`. Set `ORGANIZATION_NAME` to personalize the prompt.

6. Run `python bot.py` and tag the bot in a server message such as `@Governance Bot Who can vote in elections?`.

## Azure request settings

The bot uses `reasoning_effort="minimal"` and `max_completion_tokens=500`, which covers reasoning and visible output. Azure's `gpt-5-nano` deployment uses its default temperature. [Azure reasoning model settings](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning), [Chat Completions reference](https://learn.microsoft.com/en-us/azure/foundry/reference/rest/chat-create-chat-completion)

The instructions and both documents form the same first message on every request. Azure automatically caches eligible matching prefixes starting at 1,024 tokens. [Azure prompt caching](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/prompt-caching)
