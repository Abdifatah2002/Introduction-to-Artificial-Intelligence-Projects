Sure! Here's the complete `README.md` file with your name included, and no extra content:

---

```markdown
# Probabilistic Language Identification

This Python program identifies whether a shredded text letter is written in **English** or **Spanish** using **Bayesian inference** and **multinomial character probabilities**.

---

## 📂 Project Structure

```

.
├── hw2.py                   # Main Python script
├── e.txt                    # Multinomial probabilities for English
├── s.txt                    # Multinomial probabilities for Spanish
├── samples/                 # Sample input/output files (letter0.txt to letter4.txt)

````

---

## 🚀 How It Works

1. **Shredding**: 
   - Reads a text file, ignores case, and counts occurrences of letters A–Z.
   - Ignores all other characters (spaces, punctuation, digits, etc).

2. **Bayes Rule**: 
   - Computes the likelihood that the letter is in English or Spanish based on pre-defined letter frequencies.

3. **Multinomial Probability**:
   - Uses a log-transformed multinomial model to compute log-likelihoods and posterior probabilities.

---

## 🧪 Example Usage

```bash
python3 hw2.py samples/letter1.txt 0.6 0.4
````

* `samples/letter1.txt`: input shredded letter
* `0.6`: prior probability of English
* `0.4`: prior probability of Spanish

---

## ✅ Output Format

The program prints 4 sections as required:

* **Q1**: Letter counts A-Z
* **Q2**: `X1 * log(e1)` and `X1 * log(s1)` for letter A
* **Q3**: Log-likelihoods `F(English)` and `F(Spanish)`
* **Q4**: Posterior probability `P(English | X)`

Example:

```
Q1
A 1
B 0
...
Z 0
Q2
-0.0000
-0.0000
Q3
-78.8932
-81.2345
Q4
0.8461
```

---

## 🛠 Requirements

* Python 3.x
* No external libraries (uses only built-in Python modules)

---

## ✍️ Author

Abdifatah Abdi



