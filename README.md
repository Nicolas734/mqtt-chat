# Documentação do Chat MQTT

Este é um chat criado usando MQTT (Message Queuing Telemetry Transport). Este documento fornece instruções sobre como configurar e executar o chat MQTT.

## Pré-requisitos

- Python 3.x instalado no sistema.
- Pacote `paho-mqtt` instalado no ambiente virtual Python.

## Configuração

1. Crie um ambiente virtual Python (venv):


```bash
python -m venv venv
```
2. Ative o ambiente virtual:
No Windows:

```bash
venv\Scripts\activate
```
No Linux/Mac:

```bash
source venv/bin/activate
```

3. Instale o pacote paho-mqtt:

```bash
pip install paho-mqtt
```

4. Opcional: preencha o arquivo config.ini:

Caso queira fornecer as informações de configuração antecipadamente, você pode editar o arquivo config.ini com as configurações desejadas.

Se o arquivo config.ini estiver vazio ao executar a aplicação, o próprio programa irá solicitar as informações necessárias através de prompts interativos.

## Execução

Siga os passos abaixo para executar o chat MQTT:

1. Abra um terminal e navegue até o diretório raiz do projeto.

2. Execute o subscriber (sub.py):

```bash

python sub.py
```
O subscriber ficará aguardando por mensagens enviadas pelos publishers.

3. Abra outro terminal e navegue até o diretório raiz do projeto.

4. Execute o publisher (pub.py):

```bash
python pub.py
```
O publisher permite que você envie mensagens para o subscriber. As mensagens enviadas serão exibidas pelo subscriber.

Certifique-se de executar o subscriber primeiro e o publisher em seguida para garantir a correta comunicação entre eles.

Se você não preencheu o arquivo config.ini, o programa solicitará informações como o endereço do broker MQTT, o tópico do chat, etc., através de prompts interativos.

Observação: Certifique-se de ter um broker MQTT em funcionamento e configurado corretamente antes de executar o chat MQTT.