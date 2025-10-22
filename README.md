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
```

---

## 📊 **Visão Analítica**

### 🔹 **Visão Geral do Painel**
Indicadores macro de performance operacional — total de litros, autonomia média, tanques críticos e consumo por período.

![Painel SupplyIQ - Visão Macro](https://github.com/user-attachments/assets/b2cab61d-37ca-466a-836d-8e64fe090b15)

---

### 🔹 **Ruptura em Estado de Alerta**
Visualização dos tanques em alerta, destacando consumo elevado e necessidade de reabastecimento iminente.

![Painel SupplyIQ - Alerta](https://github.com/user-attachments/assets/91414baa-884a-4b9d-a3b6-f5725d68fa0b)

---

### 🔹 **Ruptura Normal**
Operação sob controle, com níveis de autonomia dentro dos parâmetros aceitáveis.

![Painel SupplyIQ - Normal](https://github.com/user-attachments/assets/dc056bb2-76ac-4f73-8663-5dda2f19ea3e)

---

### 🔹 **Ruptura Crítica**
Status crítico com risco de interrupção operacional e acionamento de alertas automáticos.

![Painel SupplyIQ - Crítico](https://github.com/user-attachments/assets/c2e94420-e693-4e8a-a870-34af73b228a9)

---

## 💡 **Benefícios Estratégicos**

✅ Antecipação de reabastecimento com base no consumo real  
✅ Mitigação de riscos de ruptura e paradas operacionais  
✅ Padronização e consolidação de dados de múltiplas fontes (SQL, Excel, API)  
✅ Redução de tempo em rotinas manuais de controle  
✅ Suporte à decisão executiva com indicadores visuais e preditivos  

---

## 🧠 **Aplicações Corporativas**

O **SupplyIQ** pode ser adaptado para diferentes contextos operacionais:

- Monitoramento de tanques, silos e reservatórios em tempo real  
- Gestão de consumo e reabastecimento em plantas industriais  
- Integração com sistemas ERP, SCADA e plataformas IoT via API REST  
- Módulo analítico para **Torre de Controle Logístico**  

---

## 👨‍💼 **Autor**

**Luis Henrique Camargo**  
Especialista em Dados e Supply Chain • Business Intelligence Logístico  

📧 especialista.luiscamargo@gmail.com  
📱 +55 11 94088-0735  
🌐 [LinkedIn](https://www.linkedin.com/in/luisespecialista/)  

---
