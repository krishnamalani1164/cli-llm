# SecCLI: Natural Language to Secure Command-Line Interface 🕵️‍♂️

SecCLI is a smart command-line tool that translates natural language text into executable security commands. It's designed to lower the barrier to entry for complex security tools, helping both new and experienced users perform security tasks more efficiently without needing to memorize complex command syntax.

This project leverages a **semantic search** model to find the most appropriate command from a pre-defined dataset and includes a crucial safety filter to prevent the execution of potentially dangerous commands.

## ✨ Features

-   **Natural Language Input**: Simply type what you want to do (e.g., "scan a subnet for live hosts").
-   **Intelligent Command Matching**: Uses a Sentence-BERT model to understand the *meaning* of your request and find the best command.
-   **Interactive CLI**: A user-friendly, interactive prompt for a smooth workflow.
-   **Built-in Safety Filter**: Protects against accidental execution of harmful commands like `rm -rf` or `sudo`.
-   **Extensible**: The tool's knowledge can be expanded by simply adding more examples to the dataset.

---

## ⚙️ How It Works

The tool operates on a simple yet powerful 6-step pipeline to turn a user's query into a safe command:

1.  **Input**: The user enters a command in plain English via an interactive CLI prompt.
2.  **Similarity Search**: The input text is encoded into a vector embedding using a pre-trained **Sentence-Transformer (BERT)** model. This embedding is compared against a pre-computed database of over 10,000 security command embeddings to find the most semantically similar one using **cosine similarity**.
3.  **LLM Classifier (Simulated)**: The command with the highest similarity score is selected as the best match. This acts as a fast and efficient classifier.
4.  **Command Generation (Simulated)**: The corresponding CLI command from the dataset is retrieved.
5.  **Safety Filter**: The retrieved command is checked against a blocklist of dangerous keywords (`rm -rf`, `shutdown`, `sudo`, etc.).
6.  **Final Output**: If the command is deemed safe, it is printed to the user's console. Otherwise, an error message is shown.



---

## 🚀 Getting Started

You can run this project locally or directly in a Google Colab notebook.

### Prerequisites

You need Python 3.8+ and `pip` installed.

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/SecCLI.git](https://github.com/your-username/SecCLI.git)
cd SecCLI
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset

Ensure you have the `security_nlp_cli_10000.csv` file in the root directory of the project.

---

## 💻 How to Use

Run the main script from your terminal to start the interactive session:

```bash
python seccli.py
```

The application will first load the NLP model and dataset (this may take a moment). Once loaded, you can start typing your requests at the `>>` prompt.

### Example Session

```
==============================================
      Welcome to SecCLI Direct 🕵️‍♂️
==============================================
Type your security task and get a command.
Enter 'exit' or 'quit' to close.

Loading NLP model and dataset for the first time...
✅ Model and data loaded.

>> scan a subnet for live hosts
   nmap -sn 10.0.2.0/24

>> find all pdf files in the current directory
   find . -type f -name "*.pdf"

>> exit
👋 Goodbye!
```

---

## 🔮 Future Improvements

This project is a solid proof-of-concept. Future development could include:

-   **True Generative Model**: Replace the dataset retrieval with a fine-tuned LLM (like LLaMA or a custom T5 model) to *generate* commands instead of just finding them. This would allow for handling more complex and novel requests.
-   **Parameter Extraction**: Use Named Entity Recognition (NER) to extract specific parameters (like IP addresses, filenames, ports) from the user's text and insert them into the generated command.
-   **Expanded Dataset**: Increase the size and variety of the command dataset to cover more tools and scenarios.
-   **Feedback Loop**: Implement a system where users can confirm if a command was correct, providing valuable data for further model fine-tuning.
