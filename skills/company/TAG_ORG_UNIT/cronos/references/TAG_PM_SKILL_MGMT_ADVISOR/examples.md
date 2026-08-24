# Exemplos — Management Advisor

> Todos assumem insumos já produzidos por Reader → Schedule + Workload → Monitor. Advisor **não** chama [CODE_REFERENCE].

---

## 1. Perda de consultor em semana com implantações

**Pergunta:** [PERSON_NAME] ([RESOURCE_ID_3]) caiu esta semana. Como redistribuir?

**Insumos (resumo):**
- Workload: 2 blocos impl na mesma semana [REDACTED_INSTRUCTION]; [PERSON_NAME] tinha bloco sprint [PROJECT_CLIENT_2]
- Schedule: sprint [PROJECT_CLIENT_2] ameaça média; [PROJECT_CLIENT_1] [VALIDATION_ENV] pendente

**Veredicto:** CRÍTICO | Confiança: DERIVADO

**Recomendação (trecho):**
1. **Não mover** implantações já agendadas (mobilidade muito baixa)
2. Realocar bloco [PERSON_NAME] → [PERSON_NAME] se livre na semana [REDACTED_INSTRUCTION]
3. Postergar **admin/coordenação** dos sprints secundários (mobilidade alta)
4. **Decisão humana:** aprovar troca consultor em bloco [PROJECT_CLIENT_2] + comunicação cliente

**Plano [METRIC]:** Confirmar blocos semana; listar tarefas admin movíveis  
**Plano [METRIC]:** Executar realocação aprovada; revisar picos  
**Plano 7d:** Normalizar WIP; evitar heroísmo triplo em impl

---

## 2. Redistribuição com WIP alto

**Pergunta:** Como reorganizar a equipe esta semana com WIP alto?

**Veredicto:** ATENÇÃO | PARCIAL se previsto [CODE_REFERENCE] zerado

**Estratégia:**
- Congelar novos compromissos de **[IMPLEMENTATION_EVENT]** até pico cair
- Redistribuir **documentação interna** e reuniões (alta mobilidade)
- Não equalizar WIP sacrificando qualidade — [REDACTED_INSTRUCTION]

---

## 3. Cronograma inviável com 2 consultores

**Pergunta:** Plano contingencial se só 2 consultores disponíveis?

**Insumos:** Schedule `[REDACTED_INSTRUCTION]` > 2 em 3 semanas futuras

**Veredicto:** CRÍTICO | DERIVADO

**Alternativas:**

| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
|-------|-------|-------|
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |
| [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] | [REDACTED_INSTRUCTION] |

**Recomendação:** A + B; escalar C apenas com aprovação gestão + cliente

---

## 4. Plano de recuperação — projeto em risco

**Pergunta:** Plano [METRIC]/[METRIC]/7d para [PROJECT_CLIENT_1] (ameaça alta)?

**Insumos:** Schedule top ameaça; [VALIDATION_ENV] #[TASK_ID_5] aguardando cliente; sprint limite 24/07

**Veredicto:** ATENÇÃO

**Plano:**
- **[METRIC]:** Escalar substatus aguardando cliente; Data Hunter (futuro) aceite termo
- **[METRIC]:** Revisar caminho crítico [VALIDATION_ENV]→impl; **não** antecipar impl sem [VALIDATION_ENV] documentada
- **7d:** Margem 1 semana [VALIDATION_ENV]-impl ou exceção declarada

---

## 5. Falta contexto qualitativo externo

**Pergunta:** Cliente exige antecipação [RELEASE_DECISION] — o que fazer?

**Insumos:** Schedule OK; Data Hunter **NO_ACCESS**; Qualitative ausente

**Veredicto:** INSUFICIENTE para recomendação forte de data | PARCIAL para opções internas

**Limitação explícita:**

> Sem contexto qualitativo externo. Diagnóstico baseado apenas em [CODE_REFERENCE], cronograma e workload. Não sei se há promessa comercial ou aceite pendente.

**Recomendação interna (DERIVADO):** proteger impl existentes; pedir Hunter quando [REDACTED_INSTRUCTION] existir

---

## 6. Mover levantamento vs [IMPLEMENTATION_EVENT]

**Pergunta:** O que pode mover com menor impacto esta semana?

**Veredicto:** ATENÇÃO | DERIVADO

**Ordem de preferência [REDACTED_INSTRUCTION]:**
1. Tarefas administrativas / gestão demandas  
2. Documentação interna  
3. Reuniões alinhamento  
4. Levantamento / diagnóstico  
5. Setup (cautela)  
6. [VALIDATION_ENV] final (baixa)  
7. **[IMPLEMENTATION_EVENT] — não mover** salvo crise + aprovação  

---

## 7. INSUFICIENTE — falta insumo crítico

**Pergunta:** Quais projetos ficam em risco se [PERSON_NAME] sair?

**Insumos:** Monitor INSUFICIENTE — Workload não ranqueou WIP de [PERSON_NAME] (draft Schedule only)

**Veredicto advisor:** INSUFICIENTE

**Resposta:**

> Não produzo mapa de risco por recurso sem saída validada do **Workload Controller** [REDACTED_INSTRUCTION]. Reexecutar pipeline Reader → Workload → Monitor.

**Decisão humana:** nenhuma realocação até insumos completos.
