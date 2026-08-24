# [COMPANY_PRODUCT]-pm-orchestrator

> Internal procedure for `[REDACTED_INSTRUCTION]`. Shared contracts: `[REDACTED_INSTRUCTION]`.

# PM Orchestrator — Cronos v0

## Fluxo

```mermaid
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

## Classificação de intenção

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|----------------|-------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

### Management Advisor — estratégia e contingência

Acionar **[COMPANY_PRODUCT]-pm-management-advisor** quando a pergunta pedir **decisão gerencial**, não só dado [CODE_REFERENCE]:

- reorganizar equipe / redistribuir carga;
- plano contingencial [REDACTED_INSTRUCTION];
- o que mover vs **não mover** ([IMPLEMENTATION_EVENT], [VALIDATION_ENV]);
- viabilidade cronograma com capacidade atual;
- plano [METRIC] / [METRIC] / [METRIC];
- trade-offs qualidade vs velocidade;
- escalonamento / recuperação de projeto.

**Ordem:** Reader → Schedule **e** Workload → [REDACTED_INSTRUCTION] → **Management Advisor** → Monitor → Fallback.

**Nunca** acionar Advisor **sem** Schedule + Workload [REDACTED_INSTRUCTION].

Ver [../[COMPANY_PRODUCT]-pm-management-advisor/SKILL.md][REDACTED_INSTRUCTION].

### Contexto externo ao [CODE_REFERENCE] → Data Hunter

Acionar **[COMPANY_PRODUCT]-pm-data-hunter** quando a pergunta depender de evidência **fora** do [CODE_REFERENCE]:

- cliente avisado do atraso;
- promessa informal de [RELEASE_DECISION];
- aceite formal ou confirmação de [VALIDATION_STAGE];
- mudança de escopo por [COMM_CHANNEL]/[EXTERNAL_CHANNEL];
- quem pediu alteração (comunicação externa);
- consultor bloqueado por terceiro;
- decisão pendente em ata/[COMM_CHANNEL];
- anexo ou documento que confirme data;
- contexto qualitativo para explicar atraso.

Montar `[REDACTED_INSTRUCTION]` conforme [../[COMPANY_PRODUCT]-pm-data-hunter/SKILL.md][REDACTED_INSTRUCTION].

**Se Data Hunter retornar NO_ACCESS:** continuar com [CODE_REFERENCE] [REDACTED_INSTRUCTION] quando possível; declarar limitação no Monitor — **PARCIAL** se contexto externo for relevante, **INSUFICIENTE** se decisão depender criticamente da fonte.

**Não substituir** [CODE_REFERENCE] Reader pelo Data Hunter — Hunter é **complementar**.

## Extração de parâmetros

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-----------|---------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

### Função do recurso (`[INTERNAL_API_METHOD]`)

Fonte: [REDACTED_INSTRUCTION]

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------------------|----------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

**Não** assumir que interno = consultor ativo.

Aplicar [glossary.md](shared/glossary.md): período delimita **todos** os critérios salvo opt-out explícito.

## Ordem de execução

1. **Data Hunter** (se contexto externo) — pode rodar em paralelo ao Reader; nunca substitui [CODE_REFERENCE]
2. **Reader** — [REDACTED_INSTRUCTION]
3. **Schedule** e/ou **Workload** — nunca chamar [REDACTED_INSTRUCTION] [CODE_REFERENCE] diretamente fora do Reader
4. **Management Advisor** [REDACTED_INSTRUCTION] — **depois** de Schedule + Workload
5. **Monitor** — [REDACTED_INSTRUCTION]
6. **Fallback Agent** — [REDACTED_INSTRUCTION]

**Nenhum agente** entrega texto final ao gestor **sem** `[REDACTED_INSTRUCTION]`.

## Resposta ao gestor

Usar template em [../[COMPANY_PRODUCT]-pm-response-monitor/template.md][REDACTED_INSTRUCTION].

O rascunho vai para **[COMPANY_PRODUCT]-pm-fallback-agent** — única skill que entrega ao gestor [REDACTED_INSTRUCTION]).

Declarar na abertura o universo **resolvido no snapshot** (não hardcode):
`[REDACTED_INSTRUCTION]` onde
`[REDACTED_INSTRUCTION]` em [shared/resource-types.yaml][REDACTED_INSTRUCTION],
IDs confirmados pelo Reader via [REDACTED_INSTRUCTION]. Contagens de sprints/recursos internos = [REDACTED_INSTRUCTION], nunca literal de skill.

## Skills do pacote

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------|-------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## MCP necessário

- **user-[REDACTED_INSTRUCTION][CODE_REFERENCE]** ou **user-[REDACTED_INSTRUCTION]** autenticado para [ENVIRONMENT] ([CODE_REFERENCE])
- **Data Hunter:** detectar [REDACTED_INSTRUCTION] no ambiente [REDACTED_INSTRUCTION]; [EXTERNAL_CHANNEL] e fontes sem [REDACTED_INSTRUCTION] → NO_ACCESS
- Opcional: **[COMPANY_PRODUCT]-tar-api-integration** para detalhes de schema
