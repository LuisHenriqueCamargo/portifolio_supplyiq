# ⛽ **Painel Operacional de Autonomia e Abastecimento — SupplyIQ**

O **SupplyIQ** é uma solução integrada de **monitoramento operacional e análise preditiva de abastecimento**, projetada para **gestão inteligente de tanques de combustível** e **prevenção de rupturas logísticas**.  
Desenvolvido com **Python, SQL Server e Power BI**, o sistema consolida dados em tempo real e fornece **insights acionáveis** para suporte à decisão em **operações industriais e de transporte**.

---

## 🎯 **Objetivo Estratégico**

O projeto tem como meta **automatizar o controle de consumo e reabastecimento**, garantindo **autonomia operacional**, **redução de riscos de ruptura** e **otimização do ciclo logístico**.  
Por meio da integração entre engenharia de dados e inteligência analítica, o SupplyIQ transforma dados brutos em **indicadores estratégicos e alertas automáticos**.

---

## 🔍 **Principais Funcionalidades**

- 🔄 **Atualização automática dos dados** via integração SQL Server / Python ETL  
- ⛽ **Cálculo dinâmico de autonomia (dias)** com base no consumo real  
- 📧 **Geração e envio automático de alertas de reabastecimento** (Outlook / Gmail API)  
- 📊 **Painel interativo em Power BI**, com indicadores de desempenho e status operacional  
- 🧠 **Cálculos DAX e modelagem Power Query** para análises comparativas e preditivas  
- 🧩 **Pipeline completo de dados (Python → SQL → Power BI)** com automação de ETL  

---

## ⚙️ **Stack Tecnológica**

| Categoria | Ferramentas |
|------------|-------------|
| **Linguagem / ETL** | Python (Pandas, SQLAlchemy, SMTP) |
| **Banco de Dados** | SQL Server Express / Excel Local |
| **Visualização e BI** | Power BI (DAX, Power Query, KPIs) |
| **Automação de Alertas** | Outlook e Gmail API |
| **Integração e Modelagem** | Pipeline ETL + Cálculo de Autonomia via Python |

---

## 🧩 **Arquitetura do Projeto**

```bash
📁 supplyiq/
├── supplyiq_etl.py          → Extração, transformação e cálculo de autonomia
├── supplyiq_alerts.py       → Envio automatizado de alertas por e-mail
├── supplyiq_dashboard.pbix  → Painel Power BI com indicadores executivos
├── database/                → Base SQL Server Express / Excel
└── docs/                    → Documentação e imagens de dashboards

