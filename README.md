# Exercício do Workshop

Esta é uma aplicação feita a partir do material de apoio do workshop da Linuxtips ministrado pelo Daniel Romero <https://github.com/infoslack/linuxtips-llm>. 

A aplicação faz a ingestão do arquivo PDF da CLT e apresenta uma interface web simples que tira dúvidas sobre a mesma utilizando LLM e fazendo RAG a partir das informações contidas no arquivo, para melhorar as respostas do modelo genérico.

Para utilizar é necessário ter o python instalado e ter chaves criadas para utilizar a API do OpenAI e no banco de dados vetorial Pinecone. 

1 - Clonar o repositório.

2 - Criar um arquivo .env com as variáveis de ambiente

    * OPENAI_API_KEY 
    * PINECONE_API_KEY
    * PINECONE_ENV

3 - Fazer o download da CLT em PDF para o diretório docs nomeando como clt.pdf

4 - Instalar as dependências 

```bash
pip install -r requirements.txt

```

5 - Fazer a ingestão e iniciar o app rodando 

```bash
    python ingestion.py 
    python app.py
```
 
6 - Chamar a aplicação em <http://localhost:7860>

## Exemplo de perguntas: 

- Como funciona o décimo terceiro salário. 

- Em que ano a CLT foi criada.

- Como funcionam as férias remuneradas.



