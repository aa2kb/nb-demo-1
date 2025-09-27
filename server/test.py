from phoenix.client import Client


phoenix_client = Client()
prompt_name = "agent_role"
prompt = phoenix_client.prompts.get(prompt_identifier=prompt_name)
print(prompt.format().messages[0].get("content").strip())