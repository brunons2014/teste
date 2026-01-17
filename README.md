🌦️ Sistema de Monitoramento Climático (Campo Grande)
Este projeto realiza a captura automática de dados meteorológicos da API OpenWeatherMap, armazena em um banco de dados PostgreSQL via Docker e disponibiliza os dados através de uma API FastAPI.

🚀 Tecnologias Utilizadas
Python 3.11

FastAPI (Para a criação da API de consulta)

SQLAlchemy (ORM para comunicação com o banco)

PostgreSQL (Banco de dados relacional)

Docker & Docker Compose (Containerização do ambiente)

🛠️ Configuração do Ambiente
1. Pré-requisitos
Docker Desktop instalado e rodando.

Python 3.x instalado localmente.

Chave de API (API KEY) ativa na OpenWeatherMap.

2. Estrutura de Arquivos
O projeto deve seguir a organização abaixo:

Plaintext

teste/

├── main.py           # Script de captura automática

├── minha_api.py      # API FastAPI para consulta

├── requirements.txt  # Dependências do Python

├── Dockerfile        # Instruções de imagem para o script de captura

└── docker-compose.yml # Orquestração dos containers (DB e App)

<img width="1366" height="720" alt="image" src="https://github.com/user-attachments/assets/28eb3646-ef57-499d-8dd8-bcbad8c9a833" />


3. Execução do Banco de Dados e Captura Automática
Para subir o banco de dados e iniciar a captura que ocorre a cada 1 hora, utilize o terminal na raiz do projeto:

Bash

docker-compose up --build -d
Nota: O script de captura (main.py) rodará dentro do Docker utilizando o host db para se conectar ao banco.

📡 Acesso aos Dados Remotamente (API)
Para visualizar os dados no Insomnia, Postman ou Navegador, siga estas instruções:

1. Iniciar o Servidor da API
No seu terminal local (Windows), execute o comando abaixo para disponibilizar a rota de consulta:

Bash

python -m uvicorn minha_api:app --reload
A API estará disponível em: http://127.0.0.1:8000.

2. Consultar Dados via Insomnia
Crie uma nova requisição do tipo GET.

Utilize o endereço: http://127.0.0.1:8000/clima.

O retorno será um JSON contendo o histórico de temperaturas de Campo Grande.

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/128ddfc1-287a-456f-b2d0-82381a6aea5f" />


3. Documentação Automática (Swagger)
O FastAPI gera automaticamente uma interface para testar as rotas. Com a API rodando, acesse no seu navegador:

http://127.0.0.1:8000/docs

📝 Observações Importantes

Ambiente Local vs Docker: Ao rodar scripts diretamente no seu terminal (como o minha_api.py ou verificar.py), a conexão com o banco deve usar localhost. Quando o script roda dentro do Docker (via Compose), deve usar o nome do serviço db.

Persistência: Os dados são salvos no banco de dados mesmo que o script de captura seja reiniciado.

Ambiente Local vs Docker: Ao rodar scripts diretamente no seu terminal (como o minha_api.py ou verificar.py), a conexão com o banco deve usar localhost. Quando o script roda dentro do Docker (via Compose), deve usar o nome do serviço db.

Persistência: Os dados são salvos no banco de dados mesmo que o script de captura seja reiniciado.

🧠 Detalhes Técnicos: Mapeamento de Dados (ORM)
O projeto utiliza o SQLAlchemy para mapear objetos Python diretamente em tabelas no PostgreSQL. Isso elimina a necessidade de escrever SQL manualmente para operações básicas.

Modelagem: A classe RegistroClima define a estrutura da tabela clima, incluindo tipos de dados como Float para temperaturas e DateTime para carimbos de data/hora.

Sincronização: O comando Base.metadata.create_all(engine) garante que a tabela seja criada automaticamente caso não exista no banco ao iniciar o serviço.

Consulta: Na API, utilizamos o Session para gerenciar a conexão e o select para buscar os dados de forma performática e segura contra ataques de injeção.

🤝 Como Contribuir
Se você é um aluno da UNIBE ou um desenvolvedor interessado em expandir este sistema:

Fork o projeto.

Crie uma Branch para sua modificação: git checkout -b feature/nova-funcionalidade.

Implemente melhorias (ex: novos endpoints de média de temperatura, integração com o app Conquest, ou gráficos com Matplotlib).

Abra um Pull Request detalhando as mudanças.

📋 Checklist de Manutenção
[ ] Verifique se o container db está com o status Up no Docker Desktop.

[ ] Garanta que sua API Key do OpenWeatherMap está válida.

[ ] Ao trocar de ambiente (Local para Docker), lembre-se de ajustar o host de localhost para db nas strings de conexão.
