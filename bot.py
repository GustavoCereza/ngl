import httpx
import random
import string
import time
import ssl

def generate_device_id():
    """Gera um deviceId aleatório composto por letras e números."""
    return "-".join(
        [
            "".join(random.choices(string.ascii_lowercase + string.digits, k=8)),
            "".join(random.choices(string.ascii_lowercase + string.digits, k=4)),
            "".join(random.choices(string.ascii_lowercase + string.digits, k=4)),
            "".join(random.choices(string.ascii_lowercase + string.digits, k=4)),
            "".join(random.choices(string.ascii_lowercase + string.digits, k=12)),
        ]
    )

def send_request():
    url = "https://ngl.link/api/submit"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "username": "usuario",                      # Substitua para o usuário desejado
        "question": "\u200b",                       # Caractere invisível
        "deviceId": generate_device_id(),
        "gameSlug": None,
        "referrer": None,
    }

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    try:
        with httpx.Client(http2=True, verify=ssl_context) as client:
            response = client.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"Mensagem enviada com sucesso! Resposta: {response.text}")
            else:
                print(f"Erro ao enviar a mensagem: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erro na requisição: {e}")

def main():
    try:
        while True:
            send_request()
            time.sleep(random.uniform(1, 3))        # Intervalo aleatório entre 1 e 3 segundos
    except KeyboardInterrupt:
        print("\nBot encerrado.")

if __name__ == "__main__":
    main()
