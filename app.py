import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# =========================
# CARREGAMENTO DOS DADOS
# =========================
df = pd.read_csv(
    "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
)

# =========================
# BARRA LATERAL – FILTROS
# =========================
st.sidebar.header("🔍 Filtros")

if st.sidebar.button("🔄 Resetar filtros"):
    st.experimental_rerun()

anos = sorted(df["ano"].unique())
senioridades = sorted(df["senioridade"].unique())
contratos = sorted(df["contrato"].unique())
tamanhos = sorted(df["tamanho_empresa"].unique())

anos_sel = st.sidebar.multiselect("Ano", anos, default=anos)
senioridades_sel = st.sidebar.multiselect("Senioridade", senioridades, default=senioridades)
contratos_sel = st.sidebar.multiselect("Tipo de Contrato", contratos, default=contratos)
tamanhos_sel = st.sidebar.multiselect("Tamanho da Empresa", tamanhos, default=tamanhos)

# =========================
# FILTRAGEM
# =========================
df_filtrado = df[
    (df["ano"].isin(anos_sel)) &
    (df["senioridade"].isin(senioridades_sel)) &
    (df["contrato"].isin(contratos_sel)) &
    (df["tamanho_empresa"].isin(tamanhos_sel))
]

# =========================
# TÍTULO
# =========================
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown(
    "Análise exploratória dos salários na área de dados. "
    "Utilize os filtros à esquerda para personalizar sua visualização."
)

# =========================
# KPIs
# =========================
st.markdown("## 📌 Métricas Gerais (USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado["usd"].mean()
    salario_mediano = df_filtrado["usd"].median()
    salario_max = df_filtrado["usd"].max()
    total = df_filtrado.shape[0]
    cargo_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio = salario_mediano = salario_max = total = 0
    cargo_frequente = "-"

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário mediano", f"${salario_mediano:,.0f}")
col3.metric("Salário máximo", f"${salario_max:,.0f}")
col4.metric("Total de registros", f"{total:,}")
col5.metric("Cargo mais frequente", cargo_frequente)

st.markdown("---")

# =========================
# EVOLUÇÃO TEMPORAL
# =========================
st.markdown("## 📈 Evolução Salarial ao Longo do Tempo")

media_ano = df_filtrado.groupby("ano")["usd"].mean().reset_index()

grafico_linha = px.line(
    media_ano,
    x="ano",
    y="usd",
    markers=True,
    labels={"usd": "Salário médio (USD)", "ano": "Ano"},
    title="Salário médio por ano"
)

st.plotly_chart(grafico_linha, use_container_width=True)

# =========================
# GRÁFICOS PRINCIPAIS
# =========================
st.markdown("## 📊 Análises Comparativas")

col1, col2 = st.columns(2)

with col1:
    top_cargos = (
        df_filtrado.groupby("cargo")["usd"]
        .mean()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    grafico_cargos = px.bar(
        top_cargos,
        x="usd",
        y="cargo",
        orientation="h",
        title="Top 10 cargos por salário médio",
        labels={"usd": "Salário médio (USD)", "cargo": ""}
    )

    st.plotly_chart(grafico_cargos, use_container_width=True)

with col2:
    grafico_hist = px.histogram(
        df_filtrado,
        x="usd",
        nbins=30,
        title="Distribuição dos salários",
        labels={"usd": "Salário anual (USD)"}
    )

    st.plotly_chart(grafico_hist, use_container_width=True)

# =========================
# SENIORIDADE E CONTRATO
# =========================
st.markdown("## 🧠 Salário por Senioridade e Tipo de Contrato")

grafico_box = px.box(
    df_filtrado,
    x="senioridade",
    y="usd",
    color="contrato",
    title="Distribuição salarial por senioridade e contrato",
    labels={"usd": "Salário anual (USD)", "senioridade": "Senioridade"}
)

st.plotly_chart(grafico_box, use_container_width=True)

# =========================
# REMOTO + EMPRESA
# =========================
col1, col2 = st.columns(2)

with col1:
    remoto = df_filtrado["remoto"].value_counts().reset_index()
    remoto.columns = ["Tipo", "Quantidade"]

    grafico_remoto = px.pie(
        remoto,
        names="Tipo",
        values="Quantidade",
        hole=0.5,
        title="Distribuição por tipo de trabalho"
    )

    st.plotly_chart(grafico_remoto, use_container_width=True)

with col2:
    empresa = df_filtrado.groupby("tamanho_empresa")["usd"].mean().reset_index()

    grafico_empresa = px.bar(
        empresa,
        x="tamanho_empresa",
        y="usd",
        title="Salário médio por tamanho da empresa",
        labels={"usd": "Salário médio (USD)", "tamanho_empresa": "Tamanho"}
    )

    st.plotly_chart(grafico_empresa, use_container_width=True)

# =========================
# MAPA
# =========================
st.markdown("## 🌍 Salário de Data Scientist por País")

df_ds = df_filtrado[df_filtrado["cargo"] == "Data Scientist"]

media_pais = df_ds.groupby("residencia_iso3")["usd"].mean().reset_index()

grafico_mapa = px.choropleth(
    media_pais,
    locations="residencia_iso3",
    color="usd",
    color_continuous_scale="rdylgn",
    labels={"usd": "Salário médio (USD)"},
    title="Salário médio de Data Scientists por país"
)

st.plotly_chart(grafico_mapa, use_container_width=True)

# =========================
# DOWNLOAD
# =========================
st.markdown("## 📥 Download dos Dados")

st.download_button(
    label="Baixar dados filtrados (CSV)",
    data=df_filtrado.to_csv(index=False),
    file_name="salarios_dados_filtrados.csv",
    mime="text/csv"
)

# =========================
# TABELA
# =========================
st.markdown("## 🗂️ Dados Detalhados")
st.dataframe(df_filtrado)
