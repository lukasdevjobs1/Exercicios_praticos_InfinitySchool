# Sistema de Gerenciamento de Produtos - Flask

Sistema web para gerenciamento de produtos desenvolvido com Flask, SQLAlchemy e SQLite.

## 🚀 Funcionalidades

- ✅ Listagem de produtos
- ✅ Cadastro de novos produtos
- ✅ Edição de produtos existentes
- ✅ Exclusão de produtos
- ✅ Pesquisa de produtos
- ✅ API REST para produtos
- ✅ Interface responsiva

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask 3.1.2
- **Banco de Dados**: SQLite com SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Migrações**: Flask-Migrate
- **Formulários**: Flask-WTF
- **Servidor**: Gunicorn (produção)

## 📁 Estrutura do Projeto

```
SM-FlaskProject/
├── controllers/
│   └── produto_controller.py    # Controladores das rotas
├── models/
│   └── produto_model.py         # Modelos do banco de dados
├── static/
│   ├── css/
│   │   └── style.css           # Estilos CSS
│   ├── images/
│   │   └── logo.jpg            # Imagens do projeto
│   └── js/
│       └── produtos.js         # Scripts JavaScript
├── templates/
│   ├── base.html               # Template base
│   ├── index.html              # Página inicial
│   ├── produtos.html           # Lista de produtos
│   ├── criar_produto.html      # Formulário de cadastro
│   ├── editar_produto.html     # Formulário de edição
│   └── 404.html                # Página de erro
├── .env                        # Variáveis de ambiente
├── app.py                      # Aplicação principal
├── config.py                   # Configurações
├── database.db                 # Banco de dados SQLite
└── requirements.txt            # Dependências
```

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/lukasdevjobs1/Exercicios_praticos_InfinitySchool.git
cd Exercicios_praticos_InfinitySchool/SUPER-MODULOS/SM-FlaskProject
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Configure as variáveis de ambiente**
```bash
# Crie um arquivo .env na raiz do projeto
# Exemplo de configuração já incluído no projeto
```

6. **Execute a aplicação**
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 🌐 Rotas Disponíveis

### Interface Web
- `GET /` - Página inicial
- `GET /produtos` - Lista todos os produtos
- `GET /produtos/cadastro` - Formulário de cadastro
- `POST /produtos/cadastro` - Criar novo produto
- `GET /produtos/editar/<id>` - Formulário de edição
- `POST /produtos/editar/<id>` - Atualizar produto
- `GET /produtos/deletar/<id>` - Excluir produto
- `GET /produtos/pesquisar` - Pesquisar produtos

### API REST
- `GET /api/produtos` - Retorna todos os produtos em JSON

## 🗄️ Modelo de Dados

### Produto
- `id` (Integer, Primary Key)
- `nome` (String, obrigatório)
- `preco` (Float, obrigatório)
- `descricao` (Text, opcional)

## 🚀 Deploy

### Railway (Alternativa)

1. **Conecte ao Railway**:
   - Acesse [railway.app](https://railway.app)
   - Conecte seu repositório GitHub
   - Deploy automático com suporte a arquivos

### Render (Recomendado para este projeto)

1. **Conecte ao Render**:
   - Acesse [render.com](https://render.com)
   - Faça login com GitHub
   - Clique em "New +" → "Web Service"

2. **Configure o projeto**:
   - **Repository**: Selecione seu repositório
   - **Root Directory**: `SUPER-MODULOS/SM-FlaskProject`
   - **Environment**: Python 3
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn app:app`

3. **Vantagens do Render**:
   - ✅ Suporte completo a upload de arquivos
   - ✅ SQLite funciona perfeitamente
   - ✅ HTTPS automático
   - ✅ Deploy automático a cada push
   - ✅ Gratuito para projetos pessoais

### Servidor Local/VPS

Para deploy em produção com Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**Nota**: Vercel não é adequado para este projeto pois não suporta upload de arquivos.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é parte dos exercícios práticos da Infinity School.

## 👨‍💻 Autor

Desenvolvido como projeto educacional para aprendizado de Flask e desenvolvimento web.