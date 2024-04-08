## Artificial Intelligence for Classify Product Types

### Como rodar o projeto?
1. Baixe o repositório de tradutor: [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)
2. Modificar o `docker run` no arquivo `run.sh` ou `run.bat` adicionando a cláusula `--name libretranslate` para facilitar a comunicação entre os dois containers
3. Use o Shell de Run e espere o servidor subir
4. Crie o modelo da aplicação com o Notebook no repositório: [Notebook](https://github.com/mathsantos44/furnflow-model-training)
5. Coloque o modelo gerado no local `src/shared/trained_model/`
6. Dê use o comando `docker-compose up` para rodar o projeto

### Como usar a aplicação?
1. Acesse a aplicação no endereço: [Documentação da API](http://localhost:8000/swagger)
