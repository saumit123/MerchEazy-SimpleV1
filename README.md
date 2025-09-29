# MerchEazy

MerchEazy is an AI-powered tool designed to take in voice input, generate invoices, manage databases, and provide analytics for vendors. This is an ongoing project under development.

---

## Features

- **Grocery List Extraction**: Extracts grocery items, quantities, and categories from user input.
- **Customer Support Summarization**: Summarizes customer support tickets into concise paragraphs.
- **Integration with LangChain**: Uses LangChain for prompt management and LLM chaining.
- **Google Generative AI**: Powered by Google's Gemini model for high-quality language understanding.
- **Pydantic Validation**: Ensures structured and validated outputs using Pydantic models.

---

## Project Structure

```
MerchEazy/
├── .env                     # Environment variables (API keys, configurations)
├── src/
│   ├── core/
│   │   ├── prompts.py       # Prompt templates for various tasks
│   │   ├── llm_chain.py     # Core logic for processing LLM responses
│   ├── main.py              # Entry point for the application (if applicable)
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
```

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- A Google Generative AI API key
- MongoDB connection string (if applicable)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MerchEazy.git
   cd MerchEazy
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     OPENAI_API_KEY=<your_openai_api_key>
     HUGGINGFACEHUB_API_TOKEN=<your_huggingface_api_token>
     GOOGLE_API_KEY=<your_google_api_key>
     PINECONE_API_KEY=<your_pinecone_api_key>
     MONGO_URI=<your_mongodb_connection_string>
     DB_NAME=<your_database_name>
     ```

---

## Usage

### Grocery List Extraction

The `process_grocery_list` function in `llm_chain.py` extracts grocery items, quantities, and categories from user input.

Example:
```python
from src.core.llm_chain import process_grocery_list

text = "I need 5 kg of onions, 2 dishwash gels, and 1 Nivea body wash."
result = process_grocery_list(text)
print(result)
```

### Customer Support Summarization

The `customer_support_summary` prompt in `prompts.py` can be used to summarize customer support tickets.

Example:
```python
from src.core.prompts import PROMPT_TEMPLATES

text = "The customer, John Doe, reported that his order was delayed by 3 days. He has already contacted support twice."
prompt = PROMPT_TEMPLATES["customer_support_summary"].format(text=text)
print(prompt)
```

---

## Key Components

### 1. **Prompt Templates**
Located in `src/core/prompts.py`, this file contains reusable templates for various tasks.

### 2. **LLM Chain**
Located in `src/core/llm_chain.py`, this file handles the interaction with the LLM and processes its responses.

### 3. **Pydantic Models**
Used for validating and structuring the output of the LLM. Example models include `InvoiceItem` and `InventoryItem`.

---

## Troubleshooting

### Common Errors

1. **Validation Error:**
   ```
   Input should be a valid string [type=string_type]
   ```
   - Ensure the LLM response is properly extracted using the `content` attribute before parsing.

2. **Environment Variable Issues:**
   - Ensure all required variables are set in the `.env` file.

3. **Dependency Issues:**
   - Run `pip install -r requirements.txt` to ensure all dependencies are installed.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for prompt management and LLM chaining.
- [Google Generative AI](https://cloud.google.com/ai) for powering the language model.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation and parsing.

---

## Future Work

- Implement advanced voice recognition for seamless input processing.
- Develop a robust invoice generation system with customizable templates.
- Integrate advanced analytics dashboards for vendor insights.
- Add multi-language support for voice and text inputs.
- Enhance database management with real-time synchronization and backups.
- Incorporate AI-driven recommendations for inventory and sales optimization.