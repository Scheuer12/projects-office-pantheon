# Exemplos — Fallback Agent

## 1. Entrega OK — sem inconsistência

**Entrada:** GOLD-009 match — prazo sprint [PROJECT_CLIENT_1]; Monitor CONFIRMADO.

**Saída (trecho Fallback):**

```markdown
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

Não perguntar registro no buffer.

---

## 2. CORRIGIDA — golden GOLD-002

**Problema no rascunho:** Afirmou prazo único [VALIDATION_STAGE] [PERSON_NAME].

**Fallback:**

- **Status entrega:** CORRIGIDA
- **Golden match:** GOLD-002
- Inconsistência: `[REDACTED_INSTRUCTION]` — veredicto deveria ser INSUFICIENTE; listar #[TASK_ID_5] [PERSON_NAME_21] vs [PERSON_NAME] finalizada
- Substituir conclusão por recusa responsável + candidatas

**Melhoria sugerida:** Reforçar em `[REDACTED_INSTRUCTION]` exemplo [PROJECT_CLIENT_1] na abertura de ambiguidade [VALIDATION_ENV].

**Ao gestor:** *"Deseja registrar esta melhoria no improvement buffer?"*

Se gestor: *"Sim, registre"* → append `[REDACTED_INSTRUCTION]`:

```markdown
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
[REDACTED_CODE_OR_CONFIG]
```

**Não** editar `[REDACTED_INSTRUCTION]` automaticamente.

---

## 3. COM_RESSALVAS — Monitor PARCIAL omitido no draft

**Fallback:** Reinsere bloco Monitor completo; status COM_RESSALVAS; severidade baixa.

Sem buffer salvo inconsistência baixa — salvo se gestor pedir.

---

## 4. BLOQUEADA — afirmou [COMM_CHANNEL] externo com Data Hunter NO_ACCESS

**Fallback:** Bloqueia conclusão; mantém dados [CODE_REFERENCE]; declara impossibilidade de afirmar comunicação externa.

**Melhoria sugerida:** Orchestrator forçar Data Hunter + Monitor INSUFICIENTE quando criticidade alta.

Severidade **alta** → perguntar buffer.

---

## 5. Lembrete segurança (futuro)

Se gestor perguntar: *"O fallback pode atualizar a skill sozinho?"*

Responder:

> Não. Na V0.1 o Fallback só registra sugestões em `[REDACTED_INSTRUCTION]` com seu aceite.  
> **Pendente:** bloquear que usuários finais alterem skills via [REDACTED_INSTRUCTION].  
> No futuro, um **self-improver** separado lerá o buffer e aplicará mudanças **somente após sua aprovação explícita**.
