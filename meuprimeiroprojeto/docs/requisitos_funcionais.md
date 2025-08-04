# 🔗 Índice de Requisitos Funcionais – FindMyPet

## 1. Cadastro e Acesso de Usuários
- [RF01 – Cadastro de usuários (tutores)](#rf01)
- [RF02 – Login e logout](#rf02)
- [RF03 – Edição e exclusão de dados do usuário](#rf03)

## 2. Cadastro de Pets Perdidos (Usuários autenticados)
- [RF04 – Cadastro de pet perdido](#rf04)
- [RF05 – Associação do pet ao tutor](#rf05)
- [RF06 – Edição e remoção de pet perdido](#rf06)

## 3. Cadastro de Pets Encontrados (Público geral)
- [RF07 – Cadastro de pet encontrado (anônimo ou autenticado)](#rf07)
- [RF08 – Associação do pet encontrado ao usuário autenticado](#rf08)
- [RF09 – Dados mínimos de contato para anônimos](#rf09)
- [RF10 – Edição e exclusão de pet encontrado](#rf10)

## 4. Listagens e Filtros
- [RF11 – Listagem de pets perdidos com filtros](#rf11)
- [RF12 – Listagem de pets encontrados com filtros](#rf12)

## 5. Correspondência e Notificações
- [RF13 – Correspondência automática de pets](#rf13)
- [RF14 – Notificação ao tutor](#rf14)

## 6. Comunicação entre Usuários
- [RF15 – Contato entre tutor e encontrador](#rf15)
- [RF16 – Privacidade dos dados de contato](#rf16)

## 7. Funcionalidades Extras
- [RF17 – Múltiplas fotos por pet](#rf17)
- [RF18 – Mapa interativo](#rf18)
- [RF19 – Registro de histórico de ações](#rf19)
- [RF20 – Alertas na página inicial e por e-mail](#rf20)

## 1. Cadastro e Acesso de Usuários

### RF01
- O sistema deve permitir o cadastro de usuários (tutores) com os seguintes dados:
  - Nome completo  
  - E-mail (único)  
  - Telefone  
  - Data de nascimento  
  - Senha (com critérios de segurança)
  - Endereço (opcional)

### RF02
O sistema deve permitir login e logout seguro para usuários cadastrados.
  

### RF03
O sistema deve permitir que o usuário autenticado edite e exclua seus dados pessoais.

---

## 2. Cadastro de Pets Perdidos (Somente por usuários autenticados)

### RF04
- O sistema deve permitir que usuários autenticados cadastrem pets perdidos com os seguintes dados:
  - Foto do pet    
  - Tipo de animal (ex: cachorro, gato)  
  - Raça  
  - Tamanho (pequeno, médio, grande)
  - Descrição detalhada (características físicas, marcas, cicatrizes)
  - Última vez visto (data e hora)  
  - Localização aproximada  
  - Informações sobre microchip:
    - Possui chip? (sim/não)
    - Código do chip (se aplicável)
  - Status: "Perdido", "Encontrado", "Reencontrado"
  - Data de cadastro automática

### RF05
O sistema deve associar o pet perdido ao tutor (usuário autenticado que o cadastrou).

### RF06
O sistema deve permitir que o tutor edite ou remova os cadastros de pets perdidos que ele criou.

---

## 3. Cadastro de Pets Encontrados (Disponível para usuários autenticados e anônimos)

### RF07
O sistema deve permitir que qualquer pessoa (com ou sem login) cadastre um pet encontrado, informando:
- Localização onde foi encontrado  
- Data que foi encontrado  
- Tipo de animal  
- Raça (se conhecida)  
- Foto do pet  
- Foi levado a clínica/pet shop para verificar chip? (sim/não)
  - Código do chip (se identificado)
- Status: "Encontrado", "Entregue ao tutor", "Encaminhado a abrigo"

### RF08
Para cadastros feitos por usuários autenticados, o sistema deve associar o registro ao usuário.

### RF09
Para cadastros feitos por pessoas anônimas, o sistema deve solicitar:
- Nome  
- E-mail ou telefone de contato (pelo menos um)

### RF10
O sistema deve permitir a edição ou exclusão dos cadastros de pets encontrados apenas por quem o cadastrou (via login ou código de verificação enviado por e-mail).

---

## 4. Listagens e Filtros

### RF11
O sistema deve exibir uma listagem pública de pets perdidos com filtros por:
- Tipo de animal  
- Raça  
- Localização (raio de até 50 km)
- Data de desaparecimento
- Código de chip (se disponível)

### RF12
O sistema deve exibir uma listagem pública de pets encontrados com filtros por:
- Tipo de animal  
- Raça  
- Localização  
- Data de achado
- Código de chip (se disponível)

---

## 5. Correspondência e Notificações

### RF13
O sistema deve realizar a correspondência automática entre pets perdidos e encontrados com base em:
- Tipo de animal  
- Raça  
- Localização próxima  
- Data compatível  
- Código de chip (se disponível)

### RF14
O sistema deve notificar o tutor quando um pet encontrado corresponder com seu cadastro de pet perdido.

---

## 6. Comunicação entre Usuários

### RF15
O sistema deve permitir que tutores entrem em contato com quem cadastrou um pet encontrado, via formulário interno ou envio de mensagem.

### RF16
O sistema deve manter os dados de contato privados e só disponibilizá-los com autorização.

---

## 7. Funcionalidades Extras

### RF17
O sistema deve permitir anexar múltiplas fotos por pet.

### RF18
O sistema deve oferecer um mapa interativo com pins dos locais de perda e achado.

### RF19
O sistema deve registrar a data e hora de cada ação no sistema (cadastro, edição, exclusão).

### RF20
O sistema deve exibir alertas de pets encontrados compatíveis na página inicial ou via e-mail.

