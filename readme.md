# Meu Projeto

Projeto de API para Controle de Contas de Casa.

## Bibliotecas Escolhidas

Este projeto utiliza as seguintes bibliotecas principais:

- [FastAPI](https://fastapi.tiangolo.com/): Um framework web moderno e rápido para construir APIs com Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): Uma biblioteca Python SQL toolkit e Object-Relational Mapping (ORM).
- [Pydantic](https://pydantic-docs.helpmanual.io/): Uma biblioteca para validação de dados com tipagem estática.


## Requisitos

Para executar este projeto, você precisará dos seguintes requisitos:

- Python 3.x
- Todas as dependências listadas no arquivo requirements.txt

Certifique-se de instalar todas as dependências antes de executar o projeto. Você pode instalá-las executando o seguinte comando:

```bash
pip install -r requirements.txt
```


# Documentação do Schema Pydantic

Este documento fornece uma visão geral do esquema Pydantic utilizado neste projeto. O esquema define as estruturas de dados usadas para representar famílias, contas e renda mensal.

## Familia

O schema `Familia` representa informações sobre uma família. Ele contém os seguintes campos:

- `id`: Um identificador único opcional para a família.
- `sobrenome`: O sobrenome da família.
- `email`: O endereço de e-mail da família.
- `senha`: A senha da família.
- `contas`: Uma lista opcional de objetos `ContaSimples`, representando as contas associadas à família.
- `renda_mensal`: Um objeto opcional `RendaMensalSimples`, representando a renda mensal da família.

### FamiliaSimples

O schema `FamiliaSimples` é uma versão simplificada do schema `Familia`, que inclui apenas o sobrenome e o email da família.

## LoginData e LoginSucesso

Os schemas `LoginData` e `LoginSucesso` são usados para lidar com operações de login. 
- `LoginData` contém o email e a senha para autenticação.
- `LoginSucesso` retorna o usuário (no formato `FamiliaSimples`) e um token de acesso após o login bem-sucedido.

## Conta

O schema `Conta` representa informações sobre uma conta financeira. Ele inclui os seguintes campos:
- `id`: Um identificador único opcional para a conta.
- `nome`: O nome da conta.
- `valor`: O valor associado à conta.
- `data_venc`: A data de vencimento da conta.
- `situacao`: Um campo booleano opcional indicando se a conta está paga ou não.
- `familia_id`: O identificador da família associada à conta.
- `familia`: Uma referência opcional à família associada à conta.

### ContaSimples

O schema `ContaSimples` é uma versão simplificada do schema `Conta`, que inclui apenas o nome, valor e data de vencimento da conta.

## RendaMensal

O schema `RendaMensal` representa informações sobre a renda mensal de uma família. Ele inclui os seguintes campos:
- `id`: Um identificador único opcional para a renda mensal.
- `valor`: O valor da renda mensal.
- `familia_id`: O identificador da família associada à renda mensal.
- `familia`: Uma referência opcional à família associada à renda mensal.

### RendaMensalSimples e RendaMensalFamilia

Os schemas `RendaMensalSimples` e `RendaMensalFamilia` são versões simplificadas do schema `RendaMensal`, que incluem apenas o valor da renda mensal.

Este documento fornece uma visão geral dos schemas e de seus campos. Consulte o código-fonte para obter mais detalhes e exemplos de uso.

# Documentação do model SQLAlchemy

## Familia
A tabela familia representa uma entidade de família no banco de dados. Ela armazena informações sobre a família, como sobrenome, e-mail e senha.

Colunas:
- `id`: Identificador único da família (Chave primária).
- `sobrenome`: Sobrenome da família.
- `email`: Endereço de e-mail da família.
- `senha`: Senha da família.

Relacionamentos:
- `contas`: Relacionamento com a tabela conta. Uma família pode ter várias contas.
- `renda_mensal`: Relacionamento com a tabela renda_mensal. Uma família pode ter várias entradas de renda mensal.


## Conta
A tabela conta representa uma conta financeira no banco de dados. Ela armazena informações sobre as contas financeiras associadas a uma família.

Colunas:
`id`: Identificador único da conta (Chave primária).
`nome`: Nome da conta.
`valor`: Valor da conta.
`data_venc`: Data de vencimento da conta.
`situacao`: Indica se a conta está pendente (False) ou paga (True).

Relacionamentos:
`familia`: Relacionamento com a tabela familia. Uma conta pertence a uma família.

## RendaMensal
A tabela renda_mensal representa uma entrada de renda mensal no banco de dados. Ela armazena informações sobre a renda mensal associada a uma família.

Colunas:
`id`: Identificador único da entrada de renda mensal (Chave primária).
`valor`: Valor da renda mensal.

Relacionamentos:
`familia`: Relacionamento com a tabela familia. Uma entrada de renda mensal pertence a uma família.

Este documento fornece uma visão geral dos models suas Colunas e Relacionamentos. Consulte o código-fonte para obter mais detalhes e exemplos de uso.


# Documentação do Hash Provider

## Visão Geral

O Hash Provider é responsável por gerar e verificar hashes de senhas usando a biblioteca `passlib.context.CryptContext`. Ele oferece funcionalidades para criar hashes seguros de senhas e verificar se uma senha corresponde a um hash específico.

## Métodos

### gerar_hash(texto: str) -> str

Este método recebe uma senha em texto plano como entrada e retorna o hash correspondente.

- ## Parâmetros: 
  - texto: A senha em texto plano que será transformada em hash.
  
- ## Retorno: 
  - Uma string contendo o hash gerado para a senha.

### verificar_hash(texto: str, hash: str) -> bool

Este método verifica se uma senha em texto plano corresponde a um hash específico.

- ## Parâmetros: 
  - texto: A senha em texto plano que será verificada.
  - hash: O hash contra o qual a senha será verificada.
  
- ## Retorno: 
  - True se a senha corresponder ao hash, False caso contrário.

## Exemplo de Uso

```python
from passlib.context import CryptContext

# Criando uma instância do CryptContext
pws_context = CryptContext(schemes=['bcrypt'])

# Gerando um hash para a senha 'minhasenha123'
hash = pws_context.hash('minhasenha123')

# Verificando se a senha 'minhasenha123' corresponde ao hash gerado
if pws_context.verify('minhasenha123', hash):
    print("Senha válida.")
else:
    print("Senha inválida.")

Essa documentação fornece uma explicação clara dos métodos e funcionalidades fornecidos pelo provedor de hash, bem como um exemplo de uso para ilustrar como ele pode ser usado em um aplicativo Python. 

```


# Documentação do Token Provider

## Visão Geral

O Token Provider é responsável por criar e verificar tokens de acesso usando a biblioteca `jose.jwt`. Ele oferece funcionalidades para gerar tokens de acesso com tempo de expiração e verificar a autenticidade de tokens recebidos.

## Variáveis de Configuração

### SECRET_KEY

A chave secreta usada para assinar e verificar os tokens.

### ALGORITHM

O algoritmo de criptografia usado para assinar e verificar os tokens.

### EXPIRES_IN_MINUTES

O tempo de validade dos tokens de acesso, em minutos.

## Métodos

### criar_access_token(data: dict) -> str

Este método cria um token de acesso com base nos dados fornecidos.

- ## Parâmetros:
  - data: Um dicionário contendo os dados a serem incluídos no token.
  
- ## Retorno:
  - Uma string contendo o token de acesso gerado.

### verificar_access_token(token: str) -> str

Este método verifica a autenticidade de um token de acesso recebido.

- ## Parâmetros:
  - token: O token de acesso a ser verificado.
  
- ## Retorno: 
  - O identificador de assunto (subject) contido no token, se o token for válido.

## Exemplo de Uso

```python
from jose import jwt
from datetime import datetime, timedelta

# Variáveis de configuração
SECRET_KEY = '24b73b213851993e900b2ebb45b1c81f'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 3600

# Método para criar token de acesso
def criar_access_token(data: dict) -> str:
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)
    dados.update({'exp': expiracao})
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

# Método para verificar token de acesso
def verificar_access_token(token: str) -> str:
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')

# Exemplo de uso
# Criando um token de acesso para o usuário 'usuario123'
token = criar_access_token({'sub': 'usuario123'})
print("Token de acesso:", token)

# Verificando o token de acesso
usuario = verificar_access_token(token)
print("Usuário autenticado:", usuario)
```

# Documentação do Repositório de Família

## Visão Geral

O Repositório de Família é responsável por gerenciar as operações de persistência relacionadas à entidade de Família em um banco de dados. Ele oferece funcionalidades para criar, buscar e atualizar informações de famílias armazenadas no banco de dados.

## Métodos

### criar(familia: Familia) -> Familia

Este método cria uma nova entrada de família no banco de dados.

- ## Parâmetros:
  - familia: Um objeto do tipo `Familia` contendo as informações da família a ser criada.
  
- ## Retorno:
  - Um objeto do tipo `Familia` representando a família criada no banco de dados.

### buscarPorID(id: int) -> Optional[Familia]

Este método busca uma família no banco de dados com base no seu ID.

- ## Parâmetros:
  - id: O ID da família a ser buscada.
  
- ## Retorno: 
  - Um objeto do tipo `Familia` representando a família encontrada no banco de dados. Retorna `None` se a família não for encontrada.

### buscarPorEmail(email: str) -> Optional[Familia]

Este método busca uma família no banco de dados com base no seu email.

- ## Parâmetros:
  - email: O email da família a ser buscada.
  
- ## Retorno:
  - Um objeto do tipo `Familia` representando a família encontrada no banco de dados. Retorna `None` se a família não for encontrada.

### atualizarEmail(id: int, email: str)

Este método atualiza o email de uma família existente no banco de dados.

- ## Parâmetros:
  - id: O ID da família a ser atualizada.
  - email: O novo email da família.
  
- ## Retorno:
  - Retorna uma mensagem caso o email tenha sido atualizado com sucesso.

## Exemplos de Uso

```python
from sqlalchemy.orm import Session
from schemas import Familia
from infra.sqlalchemy.models import Familia as FamiliaModel
from repositorios import RepositorioFamilia

# Criando uma instância de sessão do banco de dados
db = Session()

# Criando uma nova família
nova_familia = Familia(sobrenome="Silva", email="silva@example.com", senha="senha123")
familia_criada = RepositorioFamilia(db).criar(nova_familia)
print("Família criada:", familia_criada)

# Buscando uma família pelo ID
familia_encontrada = RepositorioFamilia(db).buscarPorID(1)
print("Família encontrada:", familia_encontrada)

# Buscando uma família pelo email
familia_por_email = RepositorioFamilia(db).buscarPorEmail("silva@example.com")
print("Família encontrada pelo email:", familia_por_email)

# Atualizando o email de uma família
RepositorioFamilia(db).atualizarEmail(1, "novosilva@example.com")
print("Email da família atualizado com sucesso.")
```

Essa documentação fornece uma explicação clara dos métodos e funcionalidades fornecidos pelo repositório de família, bem como exemplos de uso para ilustrar como ele pode ser usado em um aplicativo Python. 

# Documentação do Repositório de Família

## Visão Geral

O Repositório de Família é responsável por gerenciar as operações de persistência relacionadas à entidade de Família em um banco de dados. Ele oferece funcionalidades para criar, buscar e atualizar informações de famílias armazenadas no banco de dados.

## Métodos

### criar(familia: Familia) -> Familia

Este método cria uma nova entrada de família no banco de dados.

- **Parâmetros:**
  - familia: Um objeto do tipo `Familia` contendo as informações da família a ser criada.
  
- **Retorno:**
  - Um objeto do tipo `Familia` representando a família criada no banco de dados.

### buscarPorID(id: int) -> Optional[Familia]

Este método busca uma família no banco de dados com base no seu ID.

- **Parâmetros:**
  - id: O ID da família a ser buscada.
  
- **Retorno:**
  - Um objeto do tipo `Familia` representando a família encontrada no banco de dados. Retorna `None` se a família não for encontrada.

### buscarPorEmail(email: str) -> Optional[Familia]

Este método busca uma família no banco de dados com base no seu email.

- **Parâmetros:**
  - email: O email da família a ser buscada.
  
- **Retorno:**
  - Um objeto do tipo `Familia` representando a família encontrada no banco de dados. Retorna `None` se a família não for encontrada.

### atualizarEmail(id: int, email: str)

Este método atualiza o email de uma família existente no banco de dados.

- **Parâmetros:**
  - id: O ID da família a ser atualizada.
  - email: O novo email da família.
  
- **Retorno:**
  - Este método não possui retorno.

## Exemplos de Uso

```python
from sqlalchemy.orm import Session
from schemas import Familia
from infra.sqlalchemy.models import Familia as FamiliaModel
from repositorios import RepositorioFamilia

# Criando uma instância de sessão do banco de dados
db = Session()

# Criando uma nova família
nova_familia = Familia(sobrenome="Silva", email="silva@example.com", senha="senha123")
familia_criada = RepositorioFamilia(db).criar(nova_familia)
print("Família criada:", familia_criada)

# Buscando uma família pelo ID
familia_encontrada = RepositorioFamilia(db).buscarPorID(1)
print("Família encontrada:", familia_encontrada)

# Buscando uma família pelo email
familia_por_email = RepositorioFamilia(db).buscarPorEmail("silva@example.com")
print("Família encontrada pelo email:", familia_por_email)

# Atualizando o email de uma família
RepositorioFamilia(db).atualizarEmail(1, "novosilva@example.com")
print("Email da família atualizado com sucesso.")
```

# Documentação do Repositório de Contas

## Visão Geral

O Repositório de Contas é responsável por gerenciar as operações de persistência relacionadas à entidade de Conta em um banco de dados. Ele oferece funcionalidades para criar, listar e pagar contas, além de buscar contas específicas com base no ID da família.

## Métodos

### criar(conta: Conta) -> Conta

Este método cria uma nova entrada de conta no banco de dados.

- ## Parâmetros:
  - conta: Um objeto do tipo `Conta` contendo as informações da conta a ser criada.
  
- ## Retorno:
  - Um objeto do tipo `Conta` representando a conta criada no banco de dados.

### listarContasAPagar(id: int) -> List[Conta]

Este método lista todas as contas não pagas associadas a uma família específica.

- ## Parâmetros:
  - id: O ID da família associada às contas a serem listadas.
  
- ## Retorno:
  - Uma lista de objetos do tipo `Conta` representando as contas não pagas associadas à família.

### buscarContaID(id: int, conta_id: int) -> Optional[Conta]

Este método busca uma conta específica associada a uma família com base no seu ID.

- ## Parâmetros:
  - id: O ID da família associada à conta a ser buscada.
  - conta_id: O ID da conta a ser buscada.
  
- ## Retorno:
  - Um objeto do tipo `Conta` representando a conta encontrada no banco de dados. Retorna `None` se a conta não for encontrada.

### listarContasPagas(id: int) -> List[Conta]

Este método lista todas as contas pagas associadas a uma família específica.

- ## Parâmetros:
  - id: O ID da família associada às contas a serem listadas.
  
- ## Retorno:
  - Uma lista de objetos do tipo `Conta` representando as contas pagas associadas à família.

### PagarConta(familia_id: int, conta_id: int) -> Conta

Este método marca uma conta como paga no banco de dados.

- ## Parâmetros:
  - familia_id: O ID da família associada à conta.
  - conta_id: O ID da conta a ser marcada como paga.
  
- ## Retorno:
  - Um objeto do tipo `Conta` representando a conta que foi marcada como paga.

## Exemplos de Uso

```python
from sqlalchemy.orm import Session
from schemas import Conta
from infra.sqlalchemy.models import Conta as ContaModel
from repositorios import RepositorioConta

# Criando uma instância de sessão do banco de dados
db = Session()

# Criando uma nova conta
nova_conta = Conta(nome="Aluguel", valor=1000.0, data_venc="2024-04-15", situacao=False, familia_id=1)
conta_criada = RepositorioConta(db).criar(nova_conta)
print("Conta criada:", conta_criada)

# Listando contas a pagar para uma família
contas_a_pagar = RepositorioConta(db).listarContasAPagar(1)
print("Contas a pagar:", contas_a_pagar)

# Buscando uma conta pelo ID
conta_encontrada = RepositorioConta(db).buscarContaID(1, 1)
print("Conta encontrada:", conta_encontrada)

# Listando contas pagas para uma família
contas_pagas = RepositorioConta(db).listarContasPagas(1)
print("Contas pagas:", contas_pagas)

# Marcando uma conta como paga
conta_paga = RepositorioConta(db).PagarConta(1, 1)
print("Conta paga:", conta_paga)
```

Essa documentação fornece uma explicação detalhada dos métodos e funcionalidades fornecidos pelo repositório de contas, bem como exemplos de uso para ilustrar como ele pode ser usado em um aplicativo Python.


# Documentação do Repositório de Renda Mensal

## Visão Geral

O Repositório de Renda Mensal é responsável por gerenciar as operações de persistência relacionadas à entidade de Renda Mensal em um banco de dados. Ele oferece funcionalidades para criar e listar rendas mensais associadas a uma família.

## Métodos

### criar(renda: RendaMensal) -> RendaMensal

Este método cria uma nova entrada de renda mensal no banco de dados.

- ## Parâmetros:
  - renda: Um objeto do tipo `RendaMensal` contendo as informações da renda mensal a ser criada.
  
- ## Retorno:
  - Um objeto do tipo `RendaMensal` representando a renda mensal criada no banco de dados.

### listarRenda(familia_id: int) -> RendaMensal

Este método lista a renda mensal associada a uma família específica.

- ## Parâmetros:
  - familia_id: O ID da família associada à renda mensal a ser listada.
  
- ## Retorno:
  - Um objeto do tipo `RendaMensal` representando a renda mensal associada à família. Retorna `None` se não houver renda mensal associada à família.

## Exemplos de Uso

```python
from sqlalchemy.orm import Session
from schemas import RendaMensal
from infra.sqlalchemy.models import RendaMensal as RendaMensalModel
from repositorios import RepositorioRendaMensal

# Criando uma instância de sessão do banco de dados
db = Session()

# Criando uma nova renda mensal
nova_renda = RendaMensal(valor=5000.0, familia_id=1)
renda_criada = RepositorioRendaMensal(db).criar(nova_renda)
print("Renda mensal criada:", renda_criada)

# Listando a renda mensal para uma família
renda_familia = RepositorioRendaMensal(db).listarRenda(1)
print("Renda mensal da família:", renda_familia)
```

Essa documentação fornece uma explicação detalhada dos métodos e funcionalidades fornecidos pelo repositório de renda mensal, bem como exemplos de uso para ilustrar como ele pode ser usado em um aplicativo Python.

# Routers auth_utils

Este módulo fornece utilitários relacionados à autenticação e autorização.

## Metodos

### obter_usuario_logado

Esta função é um utilitário para obter o usuário autenticado com base no token de acesso fornecido.

#### Parâmetros

- `token`: `str`  - Token de acesso JWT.
- `db`: `Session` - Sessão do banco de dados SQLAlchemy.

#### Retorno

Retorna um objeto `Familia` representando o usuário autenticado.

#### Exceções

- `HTTPException`:
  - `status_code`: `401` (Não autorizado) - Se o token fornecido for inválido.
  - `status_code`: `401` (Não autorizado) - Se o token não contiver um e-mail válido.
  - `status_code`: `401` (Não autorizado) - Se o usuário associado ao e-mail do token não for encontrado no banco de dados.

# Routers rotas_auth

Este módulo define as rotas relacionadas à autenticação e autorização de usuários.

## Rotas

### `POST /signup`

Rota para registrar um novo usuário.

- ## Método: `POST`
- ## Path: `/signup`
- ## Código de status de sucesso: `201` (Criado)
- ## Modelo de resposta: `FamiliaSimples`

#### Parâmetros

- `familia`: `Familia` (obrigatório) - Dados da família a serem registrados.

#### Retorno

Retorna os dados da família registrada.

#### Exceções

- `HTTPException`:
  - `status_code`: `400` (Requisição inválida) - Se já existir um usuário com o mesmo e-mail fornecido.

#### Exemplo de uso

```python
import requests

url = "http://localhost:8000/signup"

payload = {
    "sobrenome": "Doe",
    "email": "johndoe@example.com",
    "senha": "123456"
}

response = requests.post(url, json=payload)
print(response.json())
```

## POST /token
Rota para obter um token de acesso JWT para autenticação.

- ## Método: `POST`
- ## Path: `/token`
- ## Modelo de resposta: `LoginSucesso`

### Parâmetros

-  `login_data`: `LoginData` (obrigatório) - Dados de login contendo e-mail e senha.

### Retorno

Retorna um objeto contendo as informações do usuário e o token de acesso.

### Exceções
- `HTTPException`:
    - `status_code`: `400` (Requisição inválida) - Se o e-mail ou senha fornecidos forem incorretos.

### Exemplo de Uso

```python
import requests

url = "http://localhost:8000/token"

payload = {
    "email": "johndoe@example.com",
    "senha": "123456"
}

response = requests.post(url, json=payload)
print(response.json())
```

# Rota `GET /me`

Esta rota é responsável por retornar as informações do usuário autenticado.

- ## Método: `GET`
- ## Path: `/me`
- ## Modelo de resposta: `FamiliaSimples`

## Parâmetros

- `usuario`: `Familia` (obrigatório) - Objeto contendo as informações do usuário autenticado.

## Retorno

Retorna um objeto contendo as informações básicas do usuário autenticado.

## Exceções

- `HTTPException`:
  - `status_code`: `401` (Não autorizado) - Se o token de acesso fornecido não for válido.

## Exemplo de uso

```python
import requests

url = "http://localhost:8000/me"
headers = {
    "Authorization": "Bearer <SEU_TOKEN>"
}

response = requests.get(url, headers=headers)
print(response.json())
```

# Routers rotas_familia

Este módulo contém as rotas relacionadas às operações da família, como atualização de email, gerenciamento de contas e renda mensal.

## Rota `PUT /atualizar-email`

Esta rota é responsável por atualizar o email da família.

- ## Método: `PUT`
- ## Path: `/atualizar-email`
- ## Parâmetros:
  - `email` - Novo email a ser atualizado.
- ## Modelo de resposta: `message`
- ## Exceções:
  - `HTTPException`:
    - `status_code`: `404` (Não encontrado) - Se a família não for encontrada.

## Rota `GET /contas-a-pagar`

Esta rota retorna a lista de contas a pagar da família.

- ## Método: `GET`
- ## Path: `/contas-a-pagar`
- ## Modelo de resposta: Lista de `ContaSimples`

## Rota `GET /conta`

Esta rota busca uma conta específica da família pelo ID.

- ## Método: `GET`
- ## Path: `/conta`
- ## Parâmetros:
  - `conta_id` (obrigatório) - ID da conta a ser buscada.
- ## Modelo de resposta: `Conta`
- ## Exceções:
  - `HTTPException`:
    - `status_code`: `404` (Não encontrado) - Se a conta não for encontrada.

## Rota `GET /contas-pagas`

Esta rota retorna a lista de contas pagas da família.

- ## Método: `GET`
- ## Path: `/contas-pagas`
- ## Modelo de resposta: Lista de `ContaSimples`

## Rota `GET /pagar-conta`

Esta rota é responsável por marcar uma conta como paga.

- ## Método: `GET`
- ## Path: `/pagar-conta`
- ## Parâmetros:
  - `conta_id` (obrigatório) - ID da conta a ser marcada como paga.
- ## Modelo de resposta: `message`
- ## Exceções:
  - `HTTPException`:
    - `status_code`: `404` (Não encontrado) - Se a conta não for encontrada.

## Rota `GET /listar-renda`

Esta rota retorna a renda mensal da família.

- ## Método: `GET`
- ## Path: `/listar-renda`
- ## Modelo de resposta: `RendaMensal`
- ## Exceções:
  - `HTTPException`:
    - `status_code`: `404` (Não encontrado) - Se a renda não for encontrada.


# Routers rotas_conta

Este módulo contém as rotas relacionadas às operações de contas.

## Rota `POST /criar_conta`

Esta rota cria uma nova conta.

- ## Método: `POST`
- ## Path: `/criar_conta`
- ## Parâmetros:
  - `conta`: `Conta` (obrigatório) - Objeto contendo as informações da conta a ser criada.
- ## Retorno: Conta criada.

# Routers rotas_renda

Este módulo contém as rotas relacionadas às operações de renda mensal.

## Rota `POST /criar_renda`

Esta rota cria uma nova entrada de renda mensal.

- ## Método: `POST`
- ## Path: `/criar_renda`
- ## Parâmetros:
  - `renda`: `RendaMensal` (obrigatório) - Objeto contendo as informações da renda mensal a ser criada.
- ## Retorno: Renda mensal criada.

