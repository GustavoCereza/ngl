# Bot de Saturação de Mensagens Anônimas para ngl.link

## Aviso Legal
**`Este projeto foi desenvolvido EXCLUSIVAMENTE PARA FINS EDUCACIONAIS e demonstração de conceitos técnicos. O uso deste bot em sistemas reais deve seguir rigorosamente as leis e políticas de uso das plataformas alvo. O desenvolvedor não se responsabiliza por qualquer uso indevido, abusivo ou contrário às normas legais.`**

## 1. Visão Geral
Este projeto é um bot desenvolvido em Python para interagir com plataformas de mensagens anônimas, simulando diversos usuários. Ele envia mensagens em intervalos aleatórios com identificadores únicos (`deviceId`), imitando dispositivos diferentes. O bot utiliza `HTTP/2 e SSL` para garantir comunicação segura e eficiente.

## 2. Funcionalidades
- Simulação de Usuários: Gera valores únicos de deviceId para cada requisição, simulando diferentes dispositivos/usuários;
- Mensagens Anônimas: Envia mensagens "invisíveis" utilizando caracteres Unicode de largura zero (`\u200b`);
- Comunicação Segura: Utiliza HTTP/2 e SSL para comunicação criptografada e de alto desempenho;
- Resistente a Banimento: O sistema é projetado para dificultar banimentos baseados no deviceId. Como cada mensagem é enviada com um deviceId único, seria necessário bloquear manualmente cada identificador, tornando o processo de banimento ineficiente até o momento (**últimos testes realizados em 20/12/2024**);
- Intervalos Aleatórios: Envia requisições em intervalos aleatórios (1 a 3 segundos) para evitar detecção ou bloqueios;
- Configurável e Extensível: Permite fácil modificação de payloads, cabeçalhos e intervalos para se adequar a diferentes necessidades.

## 3. Requisitos
- `Python 3.8+`;
- `httpx`: Para comunicação HTTP/2;
- `ssl`: Para conexões seguras via SSL;

### 3.1 Instalação da biblioteca httpx:
```bash
pip install httpx
```

## 4. Como Funciona?
  Basicamente a plataforma funciona com geração de `deviceId` que é uma espécie de token usado para identificar de forma única cada dispositivo, dai a plataforma também coleta seu IP e informa sua localização para usuários pagantes da plataforma.
No entanto, ela não informa quem de fato acessou, vai mostrar apenas um `user_xxxxxx` contendo os 3 primeiros bytes respecitivo ao deviceId, e o bloqueio também ocorre encima do `deviceId` por isso esse bot gera vários `deviceId` falsos para que caso o usuário bloqueie, o bot continue enviando.

 
Um `deviceId` tem o seguinte formato:
```bash
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```
Mas mesmo embora tenha esse formato, podemos mandar o texto que quiser, porém particularmente prefiro simular algo que fique menos "na cara", então segui a estrutura original. Além de tudo isso, o bot fica mandando mensagens em intervalor um pouco randomicos de 1 a 3s para evitar que o servidor do ngl bloquie o IP devido ao envio massivo em intervalos muito curtos.

## 5. Ativando o bot
Clone o repositório:

```bash
git clone https://github.com/seuusuario/bot-mensagens-anonimas.git
cd bot-mensagens-anonimas
```

OBS: Mude o nome do usuário para a vitima desejada. Para isso apenas dê um `sudo nano /bot-mensagens-anonimas/bot.py` e altere o `username`. 

Execute o bot:
```bash
python bot.py
```

### 5.1 Demonstração de Funcionamento

<div align="center">
    <img src="https://github.com/user-attachments/assets/083129cf-81f7-4804-bfc0-320a6e8dee51" alt="Screenshot_1" width="300">
    <img src="https://github.com/user-attachments/assets/421157ea-cf69-4382-87fc-f800f9876686" alt="Screenshot_2" width="300">
</div>
<br>
<div align="center">
    <img src="https://github.com/user-attachments/assets/78f13cb0-27f8-48c6-b789-a79b51099183" alt="Screenshot_3" width="300">
    <img src="https://github.com/user-attachments/assets/a398bf3e-ac81-4e74-bcd4-fa37d2e11cb6" alt="Screenshot_4" width="300">
</div>


