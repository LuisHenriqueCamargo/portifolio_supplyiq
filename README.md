# ⛽ Painel Operacional de Autonomia e Abastecimento — SupplyIQ

O **SupplyIQ** é um painel operacional desenvolvido para **monitorar em tempo real o nível de tanques de combustível**, calcular **autonomia em dias** e emitir **alertas automáticos de reabastecimento**.  
Com integração entre **Python, SQL Server e Power BI**, a solução fornece **insights visuais e preditivos** para suporte à tomada de decisão em ambientes logísticos e industriais.

---

## 🎯 Objetivo do Projeto

Automatizar o controle de abastecimento e prever riscos de ruptura, permitindo **gestão proativa de consumo e reposição**.  
O projeto combina **engenharia de dados, automação e visualização executiva** em um único fluxo integrado.

---

## 🔍 Funcionalidades Principais

- 🔄 **Extração e atualização automática** do banco de dados (SQL Server / Excel)
- ⛽ **Cálculo de autonomia** em dias com base no consumo médio real
- 📧 **Envio automático de alertas por e-mail** (Outlook e Gmail)
- 📊 **Painel interativo em Power BI** com indicadores críticos e alertas visuais
- 🧠 **DAX avançado** para cálculo dinâmico de alertas (cores e status)
- 🧩 **Integração Python + SQL + Power BI**, formando um pipeline de dados completo

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Ferramentas |
|------------|-------------|
| Linguagem | **Python** (Pandas, SQLAlchemy, SMTP) |
| Banco de Dados | **SQL Server Express / Local** |
| Visualização | **Power BI Desktop (DAX, Power Query)** |
| Automação | **Outlook / Gmail API (teste de alertas)** |
| Modelagem | **ETL + Cálculo de Autonomia via Python** |

---

## 🗂️ Arquitetura do Projeto

```bash
📁 portfólio_supplyiq/
├── supplyiq_etl.py          → Script de integração e cálculo de autonomia
├── supplyiq_alerts.py       → Envio de alertas automáticos por e-mail
├── supplyiq_dashboard.pbix  → Painel Power BI (visualização executiva)
├── database/                → SQL Server Express ou Excel local
└── docs/                    → Prints e documentação do projeto
📷 Visual do Dashboard
<img width="617" alt="image" src="https://github.com/user-attachments/assets/77a27a43-9cfc-40c4-9cec-2966922dbe24" /> <img width="787" alt="image" src="https://github.com/user-attachments/assets/c5710967-3d6f-4171-91d3-a19aa5f5a149" /> <img width="1011" alt="image" src="https://github.com/user-attachments/assets/48ef97d0-0947-443a-8a27-d534192ef3cf" /> <img width="634" alt="image" src="https://github.com/user-attachments/assets/28fbe430-ca50-48fc-afbf-77d6adbb57ee" /> <img width="759" alt="image" src="https://github.com/user-attachments/assets/a47b309f-26d5-467f-8d25-1552be685cbf" /> 

💡 Benefícios Estratégicos
✅ Previsão de reabastecimento baseada em consumo real
✅ Redução de riscos de ruptura e paradas operacionais
✅ Alertas automáticos de tanques críticos
✅ Consolidação de dados de diversas fontes (SQL, Excel, API)
✅ Visualização executiva com KPIs e alertas dinâmicos

🧠 Aplicações Corporativas

O SupplyIQ pode ser adaptado para:

Monitorar tanques, silos ou reservatórios em tempo real

Gerar alertas automáticos para operações industriais e logísticas

Integrar-se a sistemas ERP e SCADA via API REST ou banco relacional

Operar como módulo de Torre de Controle Logístico 

👨‍💼 Sobre o Autor

Luis Henrique Camargo
Especialista em Dados e Supply Chain • Business Intelligence Logístico

📧 especialista.luiscamargo@gmail.com

📱 +55 11 94088-0735

🔗 LinkedIn

💻 GitHub
