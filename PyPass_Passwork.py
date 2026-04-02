import secrets
import string
import os

class UltraPasswordGenerator:
    # Constantes de cores ##
    COLORS = {
        "RED": '\033[91m',
        "YELLOW": '\033[93m',
        "GREEN": '\033[92m',
        "RESET": '\033[0m',
        "CYAN": '\033[96m'
    }

    def __init__(self):
        self.charset = string.ascii_letters + string.digits + string.punctuation

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate(self, length=12):

        """Gera uma senha usando segredos criptográficos."""

        # Usei o secrets.choice para garantir segurança 

        password = ''.join(secrets.choice(self.charset) for _ in range(length))
        return password

    def analyze_strength(self, password):
        """Analisa a entropia e variedade da senha."""
        score = 0
        if len(password) >= 12: score += 2
        elif len(password) >= 8: score += 1

        checks = {
            "num": any(c.isdigit() for c in password),
            "spec": any(c in string.punctuation for c in password),
            "upper": any(c.isupper() for c in password),
            "lower": any(c.islower() for c in password)
        }
        
        score += sum(checks.values())

        if score < 4:
            return (self.COLORS["RED"], "FRACA 🔓")
        elif score < 6:
            return (self.COLORS["YELLOW"], "MÉDIA 🛡️")
        else:
            return (self.COLORS["GREEN"], "FORTE 🔒")

    def run(self):
        self.clear_screen()
        print(f"{self.COLORS['CYAN']}=== ULTRA PASSWORD GENERATOR PRO ==={self.COLORS['RESET']}")
        
        while True:
            try:
                entrada = input(f"\nDigite o comprimento (ou '0' para sair): ")
                if entrada == '0': break
                
                length = int(entrada)
                if length < 6:
                    print(f"{self.COLORS['RED']}Erro: Mínimo de 6 caracteres para segurança.{self.COLORS['RESET']}")
                    continue

                pwd = self.generate(length)
                color, rating = self.analyze_strength(pwd)

                print("="*40)
                print(f"Senha Gerada: {self.COLORS['RESET']}{pwd}")
                print(f"Força:        {color}{rating}{self.COLORS['RESET']}")
                print("="*40)

            except ValueError:
                print(f"{self.COLORS['RED']}Erro: Digite apenas números inteiros.{self.COLORS['RESET']}")

if __name__ == "__main__":
    app = UltraPasswordGenerator()
    app.run()