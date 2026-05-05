# Mapa de Propriedade de Código (Ownership Map)

Análise de quem são os especialistas por trás de cada módulo do sistema.

## Bus Factor por Módulo

O "Bus Factor" (Fator Ônibus) mede quantas pessoas precisariam desaparecer do projeto para que o conhecimento sobre um módulo se perdesse (quanto menor, maior o risco).

| Módulo | Contribuidor Principal | Contribuidor Secundário | Bus Factor Estimado | Risco |
|--------|------------------------|-------------------------|---------------------|-------|
| [Module A] | [Name] (XX%) | [Name] (YY%) | [1 ou 2+] | [🔴 Alto / 🟢 Baixo] |
| [Module B] | [Name] (XX%) | - | 1 | 🔴 Crítico |

## Observações de Risco Operacional
*Descreva os principais pontos de falha humana caso os desenvolvedores principais não estejam disponíveis para a migração ou manutenção do projeto.*
