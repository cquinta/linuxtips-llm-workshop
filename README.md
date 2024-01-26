# Exercício do Workshop

Esta é uma aplicação que faz a ingestão do arquivo PDF da CLT feita a partir do material de apoio do workshop da Linuxtips ministrado pelo [Daniel Romero]<https://https://github.com/infoslack/linuxtips-llm>. 

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



