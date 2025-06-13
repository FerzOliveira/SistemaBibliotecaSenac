# SistemaBibliotecaSenac
Um sistema para gerenciar livros disponíveis na escola, com reservas e controle de empréstimos.

# Regras de Negócio do Sistema de Biblioteca Virtual Escolar

## 1. Cadastro de Livros
1.1. **Permissões**:
   - Apenas usuários autenticados com permissões de administrador (ex.: bibliotecários) podem cadastrar, editar ou excluir livros.
   - Alunos podem apenas visualizar os livros.

1.2. **Campos Obrigatórios**:
   - Título (máximo de 200 caracteres).
   - Gênero (seleção entre opções predefinidas: Ficção, Não Ficção, Infantil, Acadêmico).
   - Quantidade (número inteiro positivo, padrão = 1).
   - Autor(es) (pelo menos um autor deve ser associado, podendo ser múltiplos).

1.3. **Campos Opcionais**:
   - Capa (imagem em formato JPG, PNG ou GIF, com tamanho máximo de 5MB).
   - Data de cadastro (preenchida automaticamente com a data atual).

1.4. **Validações**:
   - O título deve ser único para evitar duplicatas.
   - A quantidade não pode ser negativa.
   - A imagem da capa deve ser validada quanto ao formato e tamanho antes do upload.
   - O sistema deve verificar se os autores selecionados existem no banco de dados.

1.5. **Comportamento**:
   - Após o cadastro, o livro é marcado como disponível se a quantidade for maior que 0.
   - O sistema registra a data de cadastro automaticamente.

---

## 2. Gerenciamento de Autores
2.1. **Permissões**:
   - Apenas administradores podem cadastrar, editar ou excluir autores.
   - Alunos podem visualizar informações dos autores associados aos livros.

2.2. **Campos Obrigatórios**:
   - Nome (máximo de 100 caracteres).

2.3. **Campos Opcionais**:
   - Biografia (texto livre, sem limite de tamanho).

2.4. **Validações**:
   - O nome do autor deve ser único.
   - Não é permitido excluir um autor que esteja associado a um livro.

2.5. **Comportamento**:
   - Autores são criados independentemente dos livros, mas devem ser associados a pelo menos um livro durante o cadastro de livros.

---

## 3. Busca e Listagem de Livros
3.1. **Permissões**:
   - Todos os usuários (autenticados ou não) podem visualizar a lista de livros e realizar buscas.
   - Usuários não autenticados não podem reservar livros.

3.2. **Funcionalidades de Busca**:
   - A busca é realizada por título, nome do autor ou gênero.
   - A busca é case-insensitive e suporta correspondência parcial.
   - Os resultados são exibidos em uma lista paginada (máximo de 12 livros por página).

3.3. **Exibição**:
   - Cada livro exibe: título, autor(es), gênero, disponibilidade (Sim/Não) e, se disponível, a capa.
   - Livros indisponíveis (quantidade = 0) são sinalizados, mas ainda podem ser visualizados.

3.4. **Validações**:
   - O campo de busca aceita apenas texto (máximo de 200 caracteres).
   - Resultados vazios exibem uma mensagem amigável: "Nenhum livro encontrado".

---

## 4. Reserva de Livros
4.1. **Permissões**:
   - Apenas usuários autenticados (alunos ou administradores) podem reservar livros.
   - Administradores podem reservar em nome de outros usuários, se necessário.

4.2. **Condições para Reserva**:
   - O livro deve ter quantidade disponível maior que 0.
   - Um usuário não pode reservar o mesmo livro mais de uma vez enquanto a reserva estiver ativa.
   - Um usuário pode ter no máximo 3 reservas ativas simultaneamente.

4.3. **Comportamento**:
   - Ao reservar, a quantidade disponível do livro é reduzida em 1.
   - A reserva registra: livro, usuário e data da reserva (automática).
   - Uma mensagem de sucesso é exibida ao usuário após a reserva.
   - Se o livro não estiver disponível, uma mensagem de erro é exibida.

4.4. **Cancelamento**:
   - Apenas o usuário que fez a reserva ou um administrador pode cancelar uma reserva.
   - Ao cancelar, a quantidade disponível do livro é incrementada em 1.
   - Reservas canceladas são marcadas como inativas, mas mantidas no histórico.

---

## 5. Empréstimo de Livros
5.1. **Permissões**:
   - Apenas administradores podem registrar empréstimos (ex.: confirmar retirada física do livro).
   - Alunos podem visualizar seus empréstimos ativos e históricos.

5.2. **Condições para Empréstimo**:
   - O livro deve ter uma reserva ativa pelo usuário ou estar disponível.
   - Um usuário pode ter no máximo 3 empréstimos ativos simultaneamente.
   - A data de devolução padrão é 7 dias após a data de empréstimo.

5.3. **Comportamento**:
   - Ao registrar um empréstimo, o sistema vincula o livro, o usuário, a data de empréstimo (automática) e a data de devolução.
   - Se o empréstimo for baseado em uma reserva, a reserva é marcada como inativa.
   - O sistema verifica se o livro está disponível antes de confirmar o empréstimo.

5.4. **Devolução**:
   - Apenas administradores podem marcar um empréstimo como devolvido.
   - Ao devolver, a quantidade disponível do livro é incrementada em 1.
   - O status de devolvido é atualizado, e a data de devolução é mantida para histórico.

5.5. **Atrasos**:
   - Um empréstimo é considerado atrasado se a data de devolução for ultrapassada e o livro não tiver sido devolvido.
   - O sistema sinaliza empréstimos atrasados na interface administrativa.

---

## 6. Notificações de Devolução por E-mail
6.1. **Condições**:
   - Notificações são enviadas automaticamente para empréstimos atrasados (data de devolução menor que a data atual e status não devolvido).
   - Apenas usuários com e-mail registrado recebem notificações.

6.2. **Conteúdo do E-mail**:
   - Assunto: "Lembrete de Devolução".
   - Corpo: Inclui o nome do usuário, título do livro e uma solicitação para devolução.
   - Remetente: Configurado no sistema (ex.: e-mail da biblioteca).

6.3. **Frequência**:
   - Notificações são enviadas uma vez por dia para cada empréstimo atrasado, até que o livro seja devolvido ou o atraso seja resolvido.
   - O sistema evita enviar múltiplas notificações para o mesmo empréstimo no mesmo dia.

6.4. **Validações**:
   - O e-mail do usuário deve ser válido.
   - O sistema registra tentativas de envio e falhas (ex.: e-mail inválido) para auditoria.

---

## 7. Relatório de Livros Mais Emprestados
7.1. **Permissões**:
   - Apenas administradores podem acessar o relatório.
   - O relatório é restrito à interface administrativa.

7.2. **Conteúdo**:
   - Lista os 10 livros com maior número de empréstimos (contagem total, incluindo empréstimos passados e ativos).
   - Exibe: título do livro e número de empréstimos.
   - Ordenação: Decrescente pelo número de empréstimos.

7.3. **Comportamento**:
   - Se não houver empréstimos registrados, o relatório exibe uma mensagem: "Nenhum empréstimo registrado".
   - O relatório é gerado em tempo real com base nos dados do banco.

7.4. **Validações**:
   - Apenas empréstimos confirmados (não reservas) são contabilizados.
   - O sistema garante que a contagem seja precisa, evitando duplicatas.

---

## 8. Gerenciamento de Usuários
8.1. **Tipos de Usuários**:
   - **Administradores**: Bibliotecários ou professores com acesso total (cadastro de livros, autores, empréstimos, relatórios).
   - **Alunos**: Usuários padrão com acesso a busca, reservas e visualização de empréstimos.

8.2. **Autenticação**:
   - O login é obrigatório para reservas, empréstimos e acesso a funcionalidades administrativas.
   - O sistema usa autenticação padrão do Django (nome de usuário/senha).
   - Senhas devem ter no mínimo 8 caracteres e incluir letras e números.

8.3. **Cadastro**:
   - Administradores podem criar contas para alunos via interface administrativa.
   - Alunos não podem se cadastrar diretamente (opcional, para controle escolar).
   - Cada usuário deve ter um e-mail único.

8.4. **Permissões**:
   - Alunos não podem acessar a interface administrativa ou modificar livros/empréstimos.
   - Administradores têm acesso irrestrito, mas ações sensíveis (ex.: exclusão de livros) exigem confirmação.

---

## 9. Regras Gerais do Sistema
9.1. **Disponibilidade de Livros**:
   - Um livro é considerado disponível se sua quantidade for maior que 0.
   - A quantidade é atualizada automaticamente em reservas, empréstimos e devoluções.

9.2. **Histórico**:
   - Todas as ações (cadastros, reservas, empréstimos, devoluções) são registradas com data e usuário responsável.
   - O histórico é mantido indefinidamente para auditoria.

9.3. **Interface**:
   - A interface usa Bootstrap para design responsivo, garantindo acessibilidade em dispositivos móveis e desktops.
   - Mensagens de sucesso/erro são exibidas para todas as ações do usuário (ex.: "Livro reservado com sucesso").

9.4. **Validações de Entrada**:
   - Todos os formulários validam entradas (ex.: números negativos, formatos inválidos).
   - Campos de texto são protegidos contra injeção de scripts (XSS).

9.5. **Escalabilidade**:
   - O sistema suporta até 1.000 livros e 500 usuários simultâneos sem degradação significativa (baseado em SQLite).
   - Para maior escala, recomenda-se migrar para PostgreSQL.

9.6. **Manutenção de Dados**:
   - Livros não podem ser excluídos se tiverem reservas ou empréstimos ativos.
   - Reservas inativas ou empréstimos devolvidos podem ser arquivados para otimizar o desempenho.

---

## 10. Fluxos Principais
10.1. **Fluxo de Reserva**:
   - Usuário busca um livro → Verifica disponibilidade → Clica em "Reservar" → Sistema valida e registra a reserva → Quantidade é reduzida → Mensagem de sucesso.

10.2. **Fluxo de Empréstimo**:
   - Administrador seleciona um livro reservado ou disponível → Registra o empréstimo para o usuário → Define data de devolução → Sistema atualiza status.

10.3. **Fluxo de Devolução**:
   - Administrador marca o empréstimo como devolvido → Sistema incrementa a quantidade do livro → Envia confirmação ao usuário (opcional).

10.4. **Fluxo de Notificação**:
   - Sistema verifica empréstimos atrasados diariamente → Envia e-mail para usuários com atrasos → Registra o envio.

10.5. **Fluxo de Relatório**:
   - Administrador acessa o relatório → Sistema calcula os livros mais emprestados → Exibe a lista ordenada.

---

## 11. Considerações Adicionais
11.1. **Segurança**:
   - Todas as ações sensíveis (ex.: cadastro, exclusão) exigem autenticação.
   - Dados sensíveis (ex.: e-mails) são armazenados com criptografia adequada.
   - O sistema protege contra ataques comuns (ex.: CSRF, XSS).

11.2. **Extensibilidade**:
   - O sistema permite adicionar novas funcionalidades, como categorias de livros ou integração com APIs de bibliotecas externas.
   - Novas regras podem ser implementadas sem alterar a estrutura principal.

11.3. **Manutenção**:
   - O sistema inclui logs para auditoria de erros e ações administrativas.
   - Backups regulares do banco de dados são recomendados.
