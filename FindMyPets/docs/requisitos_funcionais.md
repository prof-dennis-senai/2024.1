# 🔗 Índice de Requisitos Funcionais – FindMyPet

### 1. Usuários e Autenticação
- [RF01 – Cadastro de tutores](#rf01)
- [RF02 – Login e logout](#rf02)
- [RF03 – Edição e exclusão de perfil](#rf03)

### 2. Cadastro e Gerenciamento de Pets
- [RF04 – Cadastro de pet perdido](#rf04)
- [RF05 – Página pública do pet perdido](#rf05)
- [RF06 – Atualização e exclusão de pet](#rf06)

### 3. Solicitações de Busca
- [RF07 – Registro de solicitação de busca](#rf07)
- [RF08 – Atualização automática de status](#rf08)
- [RF09 – Histórico de solicitações do tutor](#rf09)

### 4. Comunicação e Notificações
- [RF10 – Contato com tutor](#rf10)
- [RF11 – Notificações ao tutor](#rf11)

### 5. Consulta Pública
- [RF12 – Filtros e busca pública](#rf12)

---

## 1. Usuários e Autenticação

### RF01 – Cadastro de tutores
O sistema deve permitir que usuários (tutores) se cadastrem com:
- Nome completo  
- E-mail (único)  
- Telefone  
- Data de nascimento  
- Senha  
- Endereço (opcional)

### RF02 – Login e logout
O sistema deve permitir login seguro por e-mail e senha, e logout do sistema.

### RF03 – Edição e exclusão de perfil
O sistema deve permitir que o tutor edite ou exclua seu perfil a qualquer momento.

---

## 2. Cadastro e Gerenciamento de Pets

### RF04 – Cadastro de pet perdido
O sistema deve permitir que tutores autenticados cadastrem pets com:
- Nome do pet  
- Foto(s)  
- Tipo de animal  
- Raça  
- Tamanho  
- Cor  
- Descrição (características visuais, cicatrizes, coleiras etc.)  
- Microchip (sim/não + código, se houver)  
- Status inicial: “Perdido”  
- Data do desaparecimento  
- Localização aproximada  

### RF05 – Página pública do pet perdido
O sistema deve gerar uma página pública com link único para compartilhamento contendo os dados do pet perdido.

### RF06 – Atualização e exclusão de pet
O tutor deve poder alterar o status do pet (ex: "Encontrado", "Inativo", "Reencontrado") ou excluir o registro.

---

## 3. Solicitações de Busca

### RF07 – Registro de solicitação de busca
Toda vez que um tutor cadastrar um pet perdido, o sistema deve registrar automaticamente uma solicitação de busca vinculada ao pet e tutor.

### RF08 – Atualização automática de status
O sistema deve alterar automaticamente o status de uma solicitação para "Desatualizado" após 6 meses sem alterações manuais.

### RF09 – Histórico de solicitações do tutor
O tutor deve ter acesso ao histórico completo de solicitações feitas na área do usuário.

---

## 4. Comunicação e Notificações

### RF10 – Contato com tutor
O sistema deve exibir um botão de mensagem na página pública do pet perdido, permitindo que qualquer visitante entre em contato com o tutor.

### RF11 – Notificações ao tutor
O sistema deve notificar o tutor via e-mail sobre:
- Alterações de status  
- Mensagens recebidas  
- Expiração da solicitação após 6 meses

---

## 5. Consulta Pública

### RF12 – Filtros e busca pública
O sistema deve permitir buscas públicas por pets perdidos com os seguintes filtros:
- Raça  
- Nome do pet  
- Status (perdido, encontrado, reencontrado, inativo, desatualizado)  
- Localização (com raio de até 50 km)