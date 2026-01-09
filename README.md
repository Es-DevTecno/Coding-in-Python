# 🔐 PyPass - Ultra Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**PyPass** is a robust Command Line Interface (CLI) tool written in Python designed to generate secure, random passwords. Unlike simple generators, PyPass includes a real-time strength analyzer that gives you immediate visual feedback on how secure your generated password is.

---

## 🚀 Features

* **Customizable Length:** You decide how long the password should be (minimum 4 characters).
* **High Entropy:** Uses Python's `random` and `string` libraries to mix uppercase, lowercase, numbers, and special symbols.
* **Strength Analysis:** An integrated algorithm evaluates the password based on length and character variety.
* **Visual Feedback:** Returns color-coded results in the terminal:
    * 🔴 **WEAK** (Unsafe)
    * 🟡 **MEDIUM** (Acceptable)
    * 🟢 **STRONG** (Recommended)

---

## 🛠️ How to Run

### Prerequisites
* Python 3.x installed on your machine.

### Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/pypass-generator.git](https://github.com/YOUR-USERNAME/pypass-generator.git)
    ```

2.  **Navigate to the project folder**
    ```bash
    cd pypass-generator
    ```

3.  **Run the script**
    ```bash
    python main.py
    ```

---

## 📸 Preview

```text
--- ULTRA PASSWORD GENERATOR ---

Enter password length (or '0' to exit): 16

----------------------------------------
Generated Password:  K9#mPv!2$xL@qZ1w
Strength:            STRONG 🔒
----------------------------------------
