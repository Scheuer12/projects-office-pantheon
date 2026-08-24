# Glossário operacional — Cronos v0

Documento compartilhado por todas as skills deste pilot. Autoritativo.

## Escopo [CODE_REFERENCE]

- Ambiente: **[ENVIRONMENT]** (`[REDACTED_INSTRUCTION]`)
- Sprints: **Projetos [PROJECT_SYSTEM] ativos** — `[REDACTED_INSTRUCTION]`, `[REDACTED_INSTRUCTION]`
- Mutação: **proibida** (somente consulta)

## Hierarquia de análise de tarefa (ordem obrigatória)

1. **Sprint** → 2. **Tipo Tarefa** → 3. **Nome Tarefa** → 4. **Status** → 5. **Substatus**

Categorias operacionais [REDACTED_INSTRUCTION] vêm do **nome** [REDACTED_INSTRUCTION], via [REDACTED_INSTRUCTION]. Tipo [CODE_REFERENCE] é contexto, não substituto.

**Capacidade e cronograma de campo** usam **blocos** (`[REDACTED_INSTRUCTION]`), não contagem bruta de tarefas: subtarefas `[REDACTED_INSTRUCTION]` são fragmentação do cronograma da tarefa pai [REDACTED_INSTRUCTION].

## Termos

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------|-----------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

## Datas de prazo (campos [CODE_REFERENCE])

| Campo | [REDACTED_INSTRUCTION] |
|-------|--------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

### Atraso (CONFIRMADO)

```
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

- **Proibido** classificar atraso por `[REDACTED_INSTRUCTION]`.
- Mesmo dia do limite → **ainda não** atrasada [REDACTED_INSTRUCTION].
- Flags WS `[REDACTED_INSTRUCTION]` / `[REDACTED_INSTRUCTION]`: **validar** com a regra acima; não confiar só no filtro [REDACTED_INSTRUCTION]. Cruzar sempre `[REDACTED_INSTRUCTION]`.
- Drift/prorrogação: dias entre `[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]` (sinal separado de atraso).

## Regra temporal (default)

Quando o usuário indicar período [REDACTED_INSTRUCTION], **todos os critérios** aplicam-se só a tarefas cujo prazo **intersecta P**:

- `[REDACTED_INSTRUCTION]` ∈ P, **ou**
- `[REDACTED_INSTRUCTION]` ∈ P [REDACTED_INSTRUCTION]

Tarefa aberta = `[REDACTED_INSTRUCTION]` ∈ {1 Lançada, 2 Andamento, 3 Pendente}.

**Exceção:** usuário diz explicitamente o contrário [REDACTED_INSTRUCTION].

Sem período na pergunta → visão **ativa completa** [REDACTED_INSTRUCTION].

## Pessoa (Recurso [COMPANY_PRODUCT])

Três camadas de identidade — **não confundir**:

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | Uso |
|--------|-------|-----|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

### Definições operacionais

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------|-----------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

**Regra:** pergunta com "consultor" → universo default = **consultores ativos (N)**, não todos cadastrados na função nem todos internos (totais via [REDACTED_INSTRUCTION]).

Ausência em `[REDACTED_INSTRUCTION]` = **inativo operacionalmente**, mesmo com tarefas legadas no [CODE_REFERENCE].

Excluir recursos de sistema/project-client-8 conforme [REDACTED_INSTRUCTION].

`[REDACTED_INSTRUCTION]` e `[REDACTED_INSTRUCTION]` **não** determinam função nem status ativo.

## Níveis de confiança

| [REDACTED_INSTRUCTION] | Uso |
|-------|-----|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Preferir **INSUFICIENTE** + explicação a resposta assertiva frágil.

## Eixos de projeto (por sprint)

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|------|--------|--------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

Contrato e heurísticas provisórias: [project-context.yaml](project-context.yaml).  
Premissas formais (futuro): skill `[REDACTED_INSTRUCTION]`.

**Regra:** agentes que **analisam**, geram **insights** ou **propõem mudanças** devem ler `[REDACTED_INSTRUCTION]` do snapshot e declarar complexidade/sensibilidade nas saídas por projeto afetado. Se `[REDACTED_INSTRUCTION]` → declarar eixos ausentes — não assumir valores default silenciosamente.

## Separação obrigatória na resposta

Nunca misturar contagens de **Atribuído** e **Envolvido** no mesmo número. Blocos distintos.
