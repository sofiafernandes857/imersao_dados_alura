# 📊 Dashboard de Análise de Salários na Área de Dados

Este projeto consiste em um **dashboard interativo desenvolvido em Python**, com foco na análise exploratória de salários na área de dados ao longo dos anos.  
O objetivo é permitir a visualização clara de tendências salariais, comparações entre cargos, senioridade, tipo de contrato, tamanho da empresa e distribuição geográfica.

O dashboard foi desenvolvido utilizando **Streamlit** e **Plotly**, permitindo uma experiência dinâmica e intuitiva para exploração dos dados.

---

## 🎯 Objetivo do Projeto

- Analisar salários na área de dados de forma exploratória
- Identificar tendências ao longo do tempo
- Comparar remunerações por cargo, senioridade e tipo de contrato
- Avaliar o impacto do trabalho remoto e do tamanho da empresa
- Visualizar a distribuição salarial por país
- Praticar boas práticas de análise de dados e visualização

---

## 🧠 Principais Análises Realizadas

- 📌 **KPIs gerais**
  - Salário médio, mediano e máximo
  - Total de registros analisados
  - Cargo mais frequente

- 📈 **Evolução salarial ao longo do tempo**
  - Análise da média salarial por ano

- 📊 **Comparações salariais**
  - Top 10 cargos por salário médio
  - Distribuição dos salários (histograma)
  - Salário por senioridade e tipo de contrato (boxplot)
  - Salário médio por tamanho da empresa

- 🌍 **Análise geográfica**
  - Mapa com o salário médio de Data Scientists por país

- 🏠 **Modalidade de trabalho**
  - Proporção entre trabalho remoto, híbrido e presencial

---

## 🚀 Funcionalidades Extras Adicionadas

Além das análises iniciais, foram implementadas melhorias para deixar o projeto mais completo e personalizado:

- 🔍 Filtros interativos (ano, senioridade, contrato e tamanho da empresa)
- 🔄 Botão para resetar filtros
- 📥 Download do dataset filtrado
- 🧠 Seção de insights automáticos
- 🗂️ Tabela detalhada com todos os dados filtrados
- 📐 Organização do dashboard em seções com storytelling analítico

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Streamlit
- Plotly
- Google Colab (para análise inicial dos dados)

---

## 📌 Como executar o projeto

```bash
pip install -r requirements.txt
streamlit run app.py
