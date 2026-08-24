# zeus-action-communication-reference

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# Action Communication - Zeus (operacional)

## Finalidade

Esta skill faz duas coisas, em sequencia:

1. **Planejar** — [REDACTED_INSTRUCTION]
2. **Executar** — [REDACTED_INSTRUCTION]

No [AGENT_PLATFORM] (PMO Zeus) o modo padrao e **operacional / nao read-only** para as
colunas `[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]` da matriz. Continua **proibido**
usar esta skill para autorizar mudanca de escopo, data de implantacao, [BUSINESS_PROCESS]
adicional ou escrita [CODE_REFERENCE].

## Fonte

Workbook vivo (edicao humana):

`[REDACTED_INSTRUCTION]`

Snapshot de execucao:

[shared/communication-action-matrix.yaml][REDACTED_INSTRUCTION]

Bindings de tools:

[shared/communication-execution.yaml][REDACTED_INSTRUCTION]

Se planilha e YAML divergirem em regra sensivel: preferir planilha, sinalizar
dessincronia, e so executar se o plano ainda estiver inequívoco.

## Colunas

| [REDACTED_INSTRUCTION] | Uso |
|---|---|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## Protocolo

### A) Planejar

1. Receber evento [REDACTED_INSTRUCTION].
2. Casar linha `[REDACTED_INSTRUCTION]` por equivalencia semantica.
3. Confirmar gatilho.
4. Resolver dados: `[REDACTED_INSTRUCTION]`, sprint/projeto, fase, tarefa-mae, recurso,
   status/substatus, datas, evidencias, link [CODE_REFERENCE], destinatarios por papel.
5. Se candidato ambiguo → `[REDACTED_INSTRUCTION]` (validacao humana) e **nao executar**.
6. Separar acao / [CODE_REFERENCE] / [REDACTED_INSTRUCTION] no `[REDACTED_INSTRUCTION]`.

### B) Executar ([AGENT_PLATFORM] ativo)

So depois do plano com `[REDACTED_INSTRUCTION]` vazias nos campos essenciais.

1. Ler [shared/communication-execution.yaml][REDACTED_INSTRUCTION].
2. **[CODE_REFERENCE]** quando `[REDACTED_INSTRUCTION]` e texto != `N/A`:
   - Preferir `[INTERNAL_API_METHOD]` com `id` = `[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]`.
   - Incluir `[REDACTED_INSTRUCTION]` / `[REDACTED_INSTRUCTION]` quando o papel estiver resolvido
     para um login concreto [REDACTED_INSTRUCTION].
   - Se a matriz pedir tipagem (ex.: Ponto de Atencao), resolver `[REDACTED_INSTRUCTION]`
     via [REDACTED_INSTRUCTION]
     **sem** tipagem inventada e declarar `[REDACTED_INSTRUCTION]` no recibo.
   - Se alvo for tarefa-mae / ambas, repetir write por alvo resolvido.
3. **[REDACTED_INSTRUCTION]** quando `[REDACTED_INSTRUCTION]`:
   - Se existir tool de chat/send no runtime → enviar com destinatarios resolvidos.
   - Se **nao** existir tool [REDACTED_INSTRUCTION] (estado atual do [REDACTED_INSTRUCTION] [DOCUMENT_PLATFORM]) →
     `[REDACTED_INSTRUCTION]`, manter rascunho da mensagem
     no recibo, e **nao** fingir envio. [CODE_REFERENCE] segue normalmente se aplicavel.
4. **Acao** nao comunicacional: so executar se houver tool clara e a acao nao for
   mudanca sensivel [REDACTED_INSTRUCTION]. Caso contrario, deixar como
   recomendacao ao CEO/humano.
5. Sempre devolver `[REDACTED_INSTRUCTION]` alem do plano.

### C) Quando NAO executar

- Mais de uma tarefa candidata sem desempate.
- Destinatario operacional so existe no Time Idealizado.
- Fonte inconclusiva / gate ambiguo exigindo `[REDACTED_INSTRUCTION]`.
- Pedido e autorizar implantacao, escopo, [BUSINESS_PROCESS] ou write [CODE_REFERENCE].
- Tool [REDACTED_INSTRUCTION] ausente ou erro de API → registrar falha; nao inventar sucesso.

## Tools esperadas (runtime [AGENT_PLATFORM])

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|---|---|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Nomes reais no hub podem vir prefixados (`[REDACTED_INSTRUCTION]`).
Usar a tool cujo sufixo coincida.

## Saidas

```yaml
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]

[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

## Fronteiras

- Cronos detecta estrutural; Athena detecta qualitativo; [CODE_REFERENCE] da regra vigente.
- Esta skill **converte e executa comunicacao operacional**.
- Decisoes sensiveis continuam com escalonamento humano (principios Zeus).
- [CODE_REFERENCE] permanece fora do escopo de escrita desta skill.
