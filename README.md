# Webinar sobre Rasa
Esse projeto foi utilizado no webinar **Rasa para iniciantes** realizado no dia 06/10/2020.
O projeto é um simples chatbot para uma pastelaria, desenvolvido utilizando o framework Rasa.

## Executando o projeto
**Importante!** Para executar o projeto é necessário ter o Rasa, docker e o Python (3.6 ou 3.7) instalado na sua máquina. 

No docker execute o comando `docker run -d -p 8000:8000 rasa/duckling` para rodar o serviço do Duckling em segundo plano, que é utilizado como extrator de entidades.

Além disso, também é necessário ter o Spacy instalado na sua máquina. Para instalar, execute os comandos:
```
pip install -U spacy                        //para instalar o Spacy
python -m spacy download pt_core_news_lg    //para baixar o modelo em português do Spacy
```

Para executar o projeto execute os comandos:
- Abra um terminal no diretório do projeto e execute o comando `rasa train`, para treinar um novo modelo;
- Após isso, execute o comando `rasa run actions`, para iniciar o servidor de *custom actions*;
- Abra outro terminal no diretório do projeto e execute o comando `rasa shell`, para iniciar a conversa com o chatbot no terminal.
