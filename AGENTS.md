# Stangler Method

> Default-active coding methodology skill for this workspace.

## Activation

The `stangler-method` skill (`.agents/skills/stangler/SKILL.md`) activates on **every coding task** by default — architecture, implementation, debugging, refactoring, testing, deployment, and any technical decision-making. The only exception is when the user explicitly asks to skip it.

## Core Protocol

Every implementation follows the **Three-Turn Dialectical Cycle**: Plan (ADR) → Red (failing tests) → Green + Refactor (implementation). No functional code without architect approval.

---

# Reversa

> Framework de Engenharia Reversa instalado neste projeto.

## Como usar

Digite `reversa` para ativar o Reversa e iniciar ou retomar a análise do projeto.

## Comportamento ao ativar

Quando o usuário digitar `reversa` sozinho em uma mensagem:

1. Ative o skill `reversa` disponível em `.agents/skills/reversa/SKILL.md`
2. Leia o SKILL.md na íntegra e siga exatamente as instruções do Reversa

## Regra não-negociável

Nunca apague, modifique ou sobrescreva arquivos pré-existentes do projeto legado.
O Reversa escreve **apenas** em `.reversa/` e `_reversa_sdd/`.
