# Meeting Summarizer

This is a Python script that uses a **local LLM model via Ollama** to summarize meeting minutes. It extracts key discussion points, decisions made, action items, and follow-up tasks.

## ✨ Features
- Uses a **local** LLM model (e.g., `mistral`, `gemma`, `llama3`, `deepseek`).
- Summarizes meeting minutes into key points and action items.
- Outputs the summary **on screen** and **saves it to a file**.
- Lightweight, requires only `ollama` as a dependency.

---

## Installation

### Install **Ollama**
Ollama is required to run the local LLM model. Install it from the official website:

🔗 **[Download Ollama](https://ollama.com/download)**

After installation, verify it is working by running:

```sh
ollama --version
```

### Install a Local Model

```sh
ollama pull mistral   # Small and fast model (default)
ollama pull gemma     # Another lightweight model
ollama pull llama3    # More powerful model
ollama pull deepseek  # Largest and most powerful model
```

### Install Required Python Libraries

```sh
pip install ollama
```

### Usage

```sh
python3 ./meeting_summarizer.py meeting_minutes.vtt
```

### (Optional) Choose a different LLM model

By default, the script uses the `mistral` model. To use a different model, specify it as an argument:

```sh
python3 ./meeting_summarizer.py meeting_minutes.vtt --model gemma
```

### Output

The summary will be printed on screen.
A summary file will be saved as meeting_minutes_summary.txt.