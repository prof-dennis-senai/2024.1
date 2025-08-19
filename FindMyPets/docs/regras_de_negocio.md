# Regras de Negócio — Pets Perdidos

Este documento define as validações e restrições que devem ser aplicadas no backend da aplicação Pets Perdidos, garantindo integridade, segurança e consistência dos dados.

## Cadastro Único por Tutor

- Cada tutor pode cadastrar **apenas um pet perdido por vez**.
- O sistema deve verificar se já existe um pet perdido ativo antes de permitir novo cadastro.
- Pets com nomes duplicados para o mesmo tutor devem ser rejeitados.

## Expiração Automática

- O anúncio de pet perdido **expira automaticamente após 6 meses** da data de cadastro.
- O sistema deve enviar **notificações de expiração** ao tutor 7 dias antes do vencimento.
- Após expirar, o anúncio deve ser **arquivado** e removido da listagem pública.

## Segurança e Visibilidade

- Apenas o tutor responsável pode **editar ou excluir** o anúncio do pet perdido.
- Tutores devem estar **autenticados** para realizar qualquer operação de cadastro, edição ou exclusão.
- A página pública do pet **não exibe dados sensíveis** do tutor (como e-mail ou telefone).
- Visitantes podem **denunciar conteúdo impróprio** nas páginas públicas.

## Busca Geográfica

- O sistema deve permitir busca por pets perdidos com base em **raio geográfico** (ex: até 10 km da localização informada).
- A localização deve ser armazenada em formato **latitude/longitude** para facilitar cálculos de distância.

## Histórico de Alterações

- Tutores podem **atualizar o status** do pet ("Ainda perdido", "Encontrado", "Adotado").
- Quando o status for alterado para "Encontrado", o anúncio deve ser **removido da listagem pública**.
- O sistema deve registrar um **histórico de alterações** para cada pet, com data e tipo de mudança.
