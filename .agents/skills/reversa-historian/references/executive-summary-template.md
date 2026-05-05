# Executive Summary

## System Identity
- **Domain:** [Resumo das principais regras extraídas do domain.md]
- **Stack:** [Linguagens e frameworks principais extraídos de dependências/inventário]
- **Age:** [Idade calculada via primeiro e último commit]
- **Team Size & Bus Factor:** [N contribuidores ativos, indicador de dependência de indivíduos chave]

## Architecture at a Glance
Veja os detalhes visuais em: [c4-context.md](c4-context.md) / [architecture.md](architecture.md)

*Resumo narrativo da arquitetura: É um monolito? Microserviços? Usa quais bancos de dados principais?*

## Health Indicators
| Indicator | Status | Source |
|-----------|--------|--------|
| Specification Confidence | 🟢 [X]% confirmed / 🟡 [Y]% inferred / 🔴 [Z]% gap | Reviewer / Artifact Inventory |
| Technical Debt | [High/Medium/Low] | Architect |
| Operational Risk | [Bus factor / Dependência excessiva de um dev] | Historian |

## Top Consolidated Risks
*Liste de 3 a 5 riscos cruciais mapeados ao longo da fase de descoberta. Combine dívidas técnicas, incertezas de regras de negócio e problemas de histórico de manutenção.*
1. [Risk]
2. [Risk]
3. [Risk]

## Reading Guide
Para iniciar um plano de reconstrução ou migração, siga esta ordem de leitura:
1. `executive_summary.md` (este documento)
2. `architecture.md` → estrutura do sistema
3. `domain.md` → regras de negócio
4. `confidence-report.md` → nível de confiabilidade
5. `<unit>/requirements.md` → especificações precisas por módulo
6. `git_archaeology.md` → histórico de evolução e autores

## Artifact Inventory Overview
Total Files: [X]
Total Size: [Y] bytes
*Veja `artifact_inventory.json` para detalhes completos.*
