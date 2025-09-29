# A dictionary to hold all your prompt templates.
PROMPT_TEMPLATES = {
    "grocery_list": """
You are an AI assistant that extracts a list of grocery items from a user's request.
For each item, extract the item name, quantity, and a general category.

The category should be one of the following: 'produce', 'dairy', 'bakery', 'pantry', 'personal care', 'cleaning supplies', 'beverages', 'miscellaneous'.

{format_instructions}

Input: "{text}"
Output:
""",
    "customer_support_summary": """
Summarize the following customer support ticket into a clear, concise paragraph.
Identify the main issue, the user's name, and any steps already taken to resolve it.

Input: "{text}"
Output:
""",
    # Add more templates here as your project grows.
}