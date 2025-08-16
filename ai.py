import os, random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

# --------------------
# Data Preparation
# --------------------
file_path = tf.keras.utils.get_file(
    "shakespeare.txt",
    origin="https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt",
    cache_dir="./data",
    cache_subdir=""
)

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read().lower()

characters = sorted(set(text))
char_to_index = {c: i for i, c in enumerate(characters)}
index_to_char = {i: c for i, c in enumerate(characters)}

SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = [text[i:i+SEQ_LENGTH] for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE)]
next_chars = [text[i+SEQ_LENGTH] for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE)]

X = np.array([[char_to_index[c] for c in s] for s in sentences])
Y = np.array([char_to_index[c] for c in next_chars])
Y = to_categorical(Y, num_classes=len(characters))

model = load_model("./data/textgenerator.h5")

# --------------------
# Model Training / Loading
# --------------------
# MODEL_PATH = "./data/textgenerator.h5"

# if os.path.exists(MODEL_PATH):                                                                                                                                                                                                                                                                                                                      
#     model = tf.keras.models.load_model(MODEL_PATH)                                                                                                                                    
# else:
#     model = Sequential([
#         LSTM(256, input_shape=(SEQ_LENGTH, len(characters))),
#         Dense(len(characters), activation="softmax")
#     ])
#     model.compile(loss="categorical_crossentropy", optimizer=RMSprop(learning_rate=0.01))
#     model.fit(tf.one_hot(X, len(characters)), Y, batch_size=256, epochs=30)
#     model.save(MODEL_PATH)

# --------------------
# Text Generation
# --------------------
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(np.clip(preds, 1e-10, 1.0)) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    return np.argmax(np.random.multinomial(1, preds, 1))

def generate_text(length=300, temperature=0.5):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    sentence = text[start_index:start_index+SEQ_LENGTH]
    generated = sentence
    
    for _ in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x[0, t, char_to_index[char]] = 1
            
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = index_to_char[next_index]
        generated += next_char
        sentence = sentence[1:] + next_char
    return generated

if __name__ == "__main__": 
    
    for t in [0.2, 0.5, 0.8, 1.0]:
        print(f"\n---- Temperature: {t} ----")
        print(generate_text(300, temperature=t))
