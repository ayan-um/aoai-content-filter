This is a simple implementation to demonstrate the working of content filter functionality.
Here are the steps to execute the demo -
1. Enable Content Filter in your Azure OpenAI settings [https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/content-filters]
2. Update the secrets.csv with your Azure OpenAI service details (region, key, and endpoint)
3. Execute the main.py with something like: python main.py eus 2024-02-01 gpt-35-turbo-instruct-ab 'I am going to cut myself! '
4. It should return a table indicating the category that triggered the filters
 
