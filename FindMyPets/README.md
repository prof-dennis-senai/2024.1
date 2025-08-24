# 🐾 FindMyPet

Sistema web colaborativo para ajudar tutores a encontrarem seus Pets Perdidos, conectando pessoas da comunidade que possam ter informações relevantes sobre o paradeiro dos animais. O sistema permite cadastrar, gerenciar e divulgar casos de pets desaparecidos com página pública de acompanhamento.

---

## 🎯 Finalidade

O **FindMyPet** tem como objetivo facilitar a busca por animais desaparecidos por meio de:

- Cadastro de Pets Perdidos e Tutores;
- Geração de uma página pública de divulgação com link compartilhável;
- Atualizações automáticas do status após 6 meses;
- Contato com o tutor via botão de mensagem;
- Histórico de solicitações de busca.

---

## 🛠️ Principais Funcionalidades

- 🐶 Cadastro de pets com fotos e informações detalhadas;
- 📍 Registro de solicitação de busca com localização e data da perda;
- 🔄 Atualização do status do pet (perdido, encontrado, inativo, desatualizado);
- 🔒 Sistema de autenticação de tutores (login e registro);
- 📄 Página pública para compartilhamento do pet perdido;
- 📬 Notificações ao tutor sobre o andamento e expiração da solicitação;
- 🔎 Filtros de busca por raça, status, localização e nome;
- 👤 Área do tutor para gerenciar seus pets e solicitações.

---

## 🚀 Como executar o projeto (Django)

### 📦 Requisitos

- Python 3.10+
- Git
- Pip
- (Opcional) Virtualenv

---

### ✅ 1. Clone o repositório

Realize o fork do projeto para o seu github, depois realize o clone alterando para o seu usuário.

```bash
git clone https://github.com/SEU_USUARIO/2024.1
cd FindMyPets
```

---

### ✅ 2. (Opcional) Crie e ative um ambiente virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

---

### ✅ 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Execute as migrações

```bash
python manage.py migrate
```

---

### ✅ 5. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

---

## 📂 Estrutura do Projeto (exemplo)

```
[EM CONSTRUÇÃO]
```

---

## 📄 Documentação

A documentação do sistema está sendo mantida na pasta [`/docs`](./docs), contendo:

* Requisitos funcionais e não funcionais
* Diagrama de casos de uso
* Modelagem de dados
* Endpoints da API
* Regras de negócio

---

## 🧑‍💻 Autor

**Profº Dennis Rocha** – [@dennis-rocha](https://github.com/dennis-rocha)

---

## 🤝 Contribuições

Este projeto está sendo desenvolvido em sala de aula por estudantes da turma **CT DESI 2024/1**.  
As contribuições fazem parte de atividades práticas avaliativas e de aprendizagem colaborativa.

### 📌 Orientações para contribuir:

- Crie uma issue antes de desenvolver novas funcionalidades ou pegue uma issue conforme apresentado em aula;
- Descreva claramente o que será implementado;
- Ao finalizar, envie um pull request com uma breve descrição da mudança;
- Utilize mensagens de commit claras e padronizadas.

Todos os membros da turma devem seguir as boas práticas de versionamento, organização e documentação de código.
