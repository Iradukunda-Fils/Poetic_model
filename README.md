# 📖 Shakespeare Character-Level Text Generation

This project trains a neural network to generate text **character by character** in the style of **William Shakespeare**.  
The model learns from Shakespeare’s writings and produces new text that *looks like Shakespeare wrote it* (though not always making sense).  

---

## ✨ Features
- 📜 **Dataset**: Works with Shakespeare’s text corpus.  
- 🔠 **Character-level modeling**: Learns spelling, punctuation, and style directly at the character level.  
- 🤖 **RNN/LSTM model**: Predicts the **next character** in a sequence.  
- 🎭 **Text generation**: Creates new "Shakespeare-like" dialogues.  
- ⚡ **Configurable**: Adjust temperature, sequence length, and sampling strategy for creative control.  

---

## 📂 Project Structure
```
.
├── data/                # Shakespeare dataset
├── model.py             # Model architecture (RNN/LSTM/GRU)
├── train.py             # Training loop
├── generate.py          # Text generation script
├── README.md            # This file
└── requirements.txt     # Dependencies

```
---


🚀 Getting Started
1️⃣ Clone the repo
git clone https://github.com/your-username/shakespeare-text-gen.git
cd shakespeare-text-gen

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model
python train.py

4️⃣ Generate Shakespeare-like text
python generate.py --seed "To be, or not to be"

🎛️ Parameters You Can Tune
<details> <summary>🔎 Click to expand</summary>

temperature: Controls randomness of predictions

Low (e.g., 0.2) → predictable, repetitive text

High (e.g., 1.0) → more creative, surprising text

sequence_length: Length of input characters given to the model

sample_size: How many characters to generate in the output

</details>
📊 Example Output

Input (seed):

ROMEO:


Generated Output:

ROMEO:
What means the prince? Ah me!  
I would not have her live; she shall be none.

🧠 How It Works

Text is split into characters instead of words.

A sequence of characters is fed into the model.

The model predicts the next character.

Predictions are sampled repeatedly → producing continuous text.

🌟 Why Character-Level?

✅ Learns spelling & punctuation

✅ Can generate new words never seen before

❌ Sometimes struggles with long-term meaning

📌 Future Improvements

 Add word-level model for comparison

 Train on other authors

 Deploy as a web app with interactive text generation

🤝 Contributing

PRs and issues are welcome! If you’d like to improve training speed, add features, or optimize generation — feel free to contribute.

📜 License

This project is licensed under the MIT License.


🚀 Getting Started
1️⃣ Clone the repo

---

git clone https://github.com/your-username/shakespeare-text-gen.git
cd shakespeare-text-gen

---

2️⃣ Install dependencies
---
uv sync 
or: uv venv && uv sync
---

3️⃣ Train the model
python train.py

4️⃣ Generate Shakespeare-like text
python generate.py --seed "To be, or not to be"

🎛️ Parameters You Can Tune
<details> <summary>🔎 Click to expand</summary>

temperature: Controls randomness of predictions

Low (e.g., 0.2) → predictable, repetitive text

High (e.g., 1.0) → more creative, surprising text

sequence_length: Length of input characters given to the model

sample_size: How many characters to generate in the output

</details>
---

📊 Example Output

Input (seed):

ROMEO:

---

---

Generated Output:

```

ROMEO:
What means the prince? Ah me!  
I would not have her live; she shall be none.

```
---
---

🧠 How It Works


Text is split into characters instead of words.

A sequence of characters is fed into the model.

The model predicts the next character.

Predictions are sampled repeatedly → producing continuous text.

🌟 Why Character-Level?

✅ Learns spelling & punctuation

✅ Can generate new words never seen before

❌ Sometimes struggles with long-term meaning

📌 Future Improvements

 Add word-level model for comparison

 Train on other authors

 Deploy as a web app with interactive text generation

🤝 Contributing

PRs and issues are welcome! If you’d like to improve training speed, add features, or optimize generation — feel free to contribute.

---

📜 License

---

This project is licensed under the MIT License.

---