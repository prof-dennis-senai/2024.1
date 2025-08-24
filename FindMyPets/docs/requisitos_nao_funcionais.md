# Requisitos Não Funcionais – FindMyPet

## 1. Segurança

- **RNF01** – O sistema deve utilizar o protocolo HTTPS para proteger a comunicação entre cliente e servidor.
- **RNF02** – As senhas dos tutores devem ser armazenadas de forma criptografada utilizando algoritmos seguros como bcrypt.
- **RNF03** – O sistema deve ter proteção contra ataques comuns como SQL Injection, XSS e CSRF.
- **RNF04** – A área do tutor só deve ser acessível por usuários autenticados.

---

## 2. Desempenho

- **RNF05** – As páginas devem ser carregadas em no máximo 2 segundos em conexões banda larga (>10 Mbps).
- **RNF06** – O tempo de resposta do servidor para ações básicas não deve exceder 1 segundo em média.

---

## 3. Escalabilidade

- **RNF07** – O sistema deve suportar o crescimento de registros sem perda significativa de desempenho.
- **RNF08** – O sistema deve seguir os princípios de uma API RESTful, permitindo integração com aplicações front-end desacopladas no futuro (como React ou mobile).

---

## 4. Usabilidade

- **RNF09** – O sistema deve ser responsivo e adaptável a diferentes dispositivos (smartphones, tablets e desktops).
- **RNF10** – A interface deve ser intuitiva para usuários com conhecimento básico em internet.
- **RNF11** – As mensagens de erro devem ser claras e amigáveis ao usuário.

---

## 5. Disponibilidade

- **RNF12** – O sistema deve estar disponível 24/7, com suporte a atualizações e correções sem necessidade de interrupção do serviço, por meio de estratégias como deploy contínuo ou atualização em segundo plano.
- **RNF13** – As páginas públicas de pets desaparecidos devem ser acessíveis sem login.

---

## 6. Confiabilidade

- **RNF14** – Backups automáticos do banco de dados devem ser realizados diariamente.
- **RNF15** – O sistema deve ser capaz de restaurar os dados a partir de um backup em caso de falha.

---

## 7. Compatibilidade

- **RNF16** – O sistema deve funcionar corretamente nos principais navegadores modernos.

---

## 8. Manutenibilidade

- **RNF17** – O código-fonte deve seguir boas práticas e ser documentado.
- **RNF18** – O projeto deve utilizar um sistema de controle de versão distribuído, com histórico rastreável de alterações por meio de commits e revisões de código.

---

## 9. Implantação (Deploy)

- **RNF19** – O sistema deve permitir implantação (deploy) em ambientes de produção com alta disponibilidade e escalabilidade, utilizando processos automatizados e compatíveis com integração contínua.