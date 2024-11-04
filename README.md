# Agentic AI Customer Support Bot using LlamaIndex and Azure OpenAI

An **agentic AI-powered customer support bot** that leverages **Azure OpenAI** and **LlamaIndex** to handle customer service interactions with human-like intelligence and responsiveness. This bot is designed to streamline customer support operations by autonomously providing information on orders, delivery dates, and return policies, all within a single conversational interface.

### Project Overview
This customer support bot leverages **Agentic AI** and **Azure OpenAI** to handle typical customer service inquiries, including order details, delivery dates, and return policies. The bot can answer complex, multi-part questions and provide support information with accuracy and clarity. It serves as an example of how agentic AI can streamline customer service interactions.

### Key Features
- **Order Information Retrieval**: Responds to queries about items in an order.
- **Delivery Tracking**: Provides scheduled delivery dates for orders.
- **Return Policy Lookup**: Supplies information on return policies based on items.
- **Customer Support Information**: Returns customer support contact details based on the context of the query.
- **Powered by Azure OpenAI**: Uses Azure’s GPT-4 API for advanced language understanding and response generation.

### Project Structure
- **Agent Setup**: Initializes an Azure OpenAI connection and configures models for generating responses.
- **Support Functions**: Custom functions return order details, delivery dates, and item return policies.
- **Vector Database**: Utilizes LlamaIndex for managing and retrieving customer service documents.
- **Query Agent**: LlamaIndex orchestrates function calls and document retrieval to create accurate and context-aware responses.

### Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/llama-agentic-ai-customer-support-bot.git
   ```

2. **Configure Azure OpenAI Settings**: Replace <YOUR_API_KEY>, <YOUR_ACCOUNT>, and other necessary parameters with your Azure OpenAI credentials.
3. Run the Code: Test the bot's functionality by running sample queries (see sample_usage.py).

### Example Usage
The bot can handle various customer support requests with ease:
  ```python 
  response = agent.query("What is the return policy for order number 1001?")
  print("Response:", response)
  ```


### Use Cases
This project demonstrates a practical approach to customer service automation in e-commerce and similar industries. By automating responses to common queries, businesses can improve response times and free up human agents for more complex inquiries.

### License
This project is licensed under the MIT License.

