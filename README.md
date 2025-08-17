# 📝 Shakespeare Character-Level Text Generator

This project is an **NLP (Natural Language Processing)** application that generates Shakespeare-like text using a **Recurrent Neural Network (RNN)** with **LSTM (Long Short-Term Memory)** layers.  
It is trained on Shakespeare's works at the **character level** and can generate creative new text based on a given seed input.

---

## 📂 Project Structure

```
├── ai.py # Core AI model & text generation logic
├── data
│ ├── shakespeare.txt # Training dataset (Shakespeare text corpus)
│ └── textgenerator.h5 # Pre-trained LSTM model
├── main.py # Entry point for running the generator
├── pyproject.toml # Project dependencies & metadata
├── README.md # Project documentation
└── uv.lock # Lock file for dependencies
```

Create a virtual environment and run the project
---

```

uv venv

# Activate the environment
source .venv/bin/activate  # On Linux / macOS
.venv\Scripts\activate     # On Windows

# Install dependencies
uv sync

uv run ai.py

```

You will be prompted to enter a seed text:
---

```

Enter the input text as starting of the poetry: To be or not to be

```


The model will generate new Shakespeare-like text continuing your input.

🔥 Key Features
---

Character-level language model (predicts next character instead of next word).

Uses LSTM layers to remember long-term dependencies in text.

Temperature sampling to control creativity:

Low temperature (0.2) → more predictable, repetitive text.

High temperature (1.0) → more creative, but may produce nonsense.

Accepts custom seed input to guide text generation.

📊 Example Output
---

Seed: "to be or not to be"

Generated (temp=0.7):

to be or not to be, that is the question: 
whether 'tis nobler in the mind to suffer 
the slings and arrows of outrageous fortune, 
or to take arms against a sea of troubles...

🧠 How It Works
---

Data Preparation

Loads Shakespeare text.

Encodes characters into numbers (char_to_index, index_to_char).

Creates training sequences of length SEQ_LENGTH=40.

Model

LSTM (256 units) + Dense Softmax layer.

Trained with categorical crossentropy + RMSProp optimizer.

Text Generation

Starts from a seed text.

Predicts next character probabilities.

Applies temperature sampling to control creativity.

Appends the chosen character and continues.

📦 Dependencies
---

tensorflow

numpy

uv (for dependency management, optional)

✨ Future Improvements
---

Train with more epochs for richer text.

Add word-level language model for more semantic meaning.

Deploy as a simple Flask/Streamlit web app for interactive use.

📜 License
---

MIT License © 2025 Your Name

---