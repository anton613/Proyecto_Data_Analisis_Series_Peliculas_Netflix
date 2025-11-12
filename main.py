import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("./Dataset/netflix_titles_procesado.csv")

df_distribucionProductos = df.value_counts("type")

st.set_page_config(
    page_title="Proyecto Análisis de Datos Netflix",
    page_icon="🎬",
    layout="wide",
)

## Functions for visualizations


### Distribución de productos por tipo
def distribucionTipoProductosNetflix(dataframe):
    fig = px.pie(
        df_distribucionProductos,
        values=df_distribucionProductos.values,
        names=df_distribucionProductos.index,
        title="¿Cómo está compuesto realmente su catálogo?",
        labels={"type": "Tipo de Producto", "values": "Cnt. de Productos"},
    )
    return fig


### Top 10 Países que más producen contenido para Netflix
def paisesMasProduccion(dataframe):
    df_distribucionProductos = (
        df[df["country"] != "Desconocido"].value_counts("country").head(10)
    )
    fig = px.bar(
        df_distribucionProductos,
        x=df_distribucionProductos.index,
        y=df_distribucionProductos.values,
        title="¿Dónde se produce realmente el contenido que consumimos?",
        labels={"x": "País", "y": "Cnt. de Producciones"},
    )
    return fig


### Evolución de la Cantidad de Productos Añadidos por Tipo y Año
def yearAdded_Evolution(dataframe):
    df_year_added = dataframe.copy()
    df_year_added["year_added"] = pd.to_datetime(
        dataframe["date_added"], format="%d/%m/%Y"
    ).dt.strftime("%Y")
    df_year_added_grouped = (
        df_year_added.groupby(by=["type", "year_added"]).count()["show_id"].to_frame()
    )

    fig = px.line(
        df_year_added_grouped.reset_index(),
        x="year_added",
        y="show_id",
        color="type",
        title="¿Cómo ha evolucionado la estrategia de adquisiciones de Netflix?",
        labels={
            "year_added": "Año de Incorporación",
            "show_id": "Cnt. Pro. Adquiridos",
        },
    )
    fig.update_traces(mode="markers+lines")
    fig.update_xaxes(dtick="M12")
    return fig


### Top 10 Clasificaciones con Mayor Cantidad de Productos en Netflix
def clasificacionesTop10(dataframe):
    df_rating = (
        dataframe.groupby(by=["rating"])
        .count()["show_id"]
        .sort_values(ascending=False)
        .head(10)
    )
    fig = px.bar(
        df_rating,
        x=df_rating.index,
        y=df_rating.values,
        title="¿A qué audiencias apunta realmente Netflix?",
        labels={"x": "Clasificación", "y": "Cnt. de Productos"},
    )
    return fig


### Top 10 Directores con Mayor Cantidad de Producciones en Netflix
def directorTop10(dataframe):
    df_directores = (
        dataframe[dataframe["director"] != "Desconocido"]
        .value_counts("director")
        .head(10)
    )
    fig = px.bar(
        df_directores,
        x=df_directores.index,
        y=df_directores.values,
        title="¿Quiénes son las mentes creativas que dan forma a la experiencia de Netflix?",
        labels={"x": "Director", "y": "Cnt. de Producciones"},
    )
    return fig


def main():
    # Header principal
    st.markdown("# 🎬 Análisis Descriptivo: Dataset de Netflix")

    # Información personal
    st.markdown("---")
    st.markdown("### Presentación Personal")
    st.markdown("**Manuel Antonio Casani Osores**")
    st.markdown("*Estudiante de Ingeniería de Sistemas*")
    st.markdown("---")
    # Objetivo del proyecto
    st.markdown("### 🎯 Objetivo del Proyecto")

    st.markdown("""
    Este proyecto tiene como objetivo principal demostrar mis habilidades en análisis de datos mediante 
    **storytelling estratégico**, transformando datos crudos en insights accionables sobre el contenido de Netflix. 
    Utilizando el framework Narrative Arc con 5 Actos, he desarrollado un análisis que no solo describe tendencias, 
    sino que también cuenta la historia detrás de los datos.
    """)

    # Métricas rápidas
    st.markdown("### 📊 Métricas Clave")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Títulos Analizados", "5,000+")

    with col2:
        st.metric("Años de Data", "20+")

    with col3:
        st.metric("Países", "100+")

    with col4:
        st.metric("Categorías", "15+")

    # Metodología
    st.markdown("### 🔬 Metodología")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### Framework Utilizado
        - Narrative Arc con 5 Actos
        - Enfoque iterativo y estructurado
        - Ciclo completo de análisis
        """)

    with col2:
        st.markdown("""
        #### Proceso Aplicado
        - **Storytelling** con datos
        - Análisis descriptivo avanzado
        - Visualizaciones estratégicas
        - Insights accionables
        """)

    # Proyecto complementario
    st.markdown("### 📈 Proyecto Complementario: Análisis Técnico")

    st.markdown("""
    Para aquellos interesados en el aspecto técnico, he desarrollado un análisis más detallado que incluye:
    """)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        #### 🔧 Proceso ETL
        - Extracción de datos
        - Transformación y limpieza
        - Carga y validación
        - Gestión de datos faltantes
        """)

    with col2:
        st.markdown("""
        #### 📊 Visualizaciones
        - Gráficos interactivos
        - Dashboards dinámicos
        - Análisis temporal
        - Segmentación por categorías
        """)

    with col3:
        st.markdown("""
        #### 📋 Metodología
        - Técnicas estadísticas
        - Análisis exploratorio
        - Machine Learning básico
        - Validación de resultados
        """)

    # Enlaces de interés
    st.markdown("### 🔗 Enlaces de Interés")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📁 Dataset Original")
        st.markdown(
            "[Acceder al dataset de Netflix](https://www.kaggle.com/datasets/shivamb/netflix-shows)"
        )

    with col2:
        st.markdown("#### 🛠️ Análisis Técnico")
        st.markdown(
            "[Ver proyecto ETL y gráficos](https://github.com/anton613/Proyecto_Data_Analisis_Series_Peliculas_Netflix)"
        )

    # Beneficios del enfoque
    st.markdown("### 💡 ¿Por qué este Enfoque?")

    st.markdown("""
    El **storytelling con datos** me permite:
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        **Contextualizar**  
        Información presentada de manera accesible y comprensible
        """)

    with col2:
        st.markdown("""
        **Destacar**  
        Patrones y tendencias relevantes identificadas claramente
        """)

    with col3:
        st.markdown("""
        **Comunicar**  
        Hallazgos de forma impactante y memorable
        """)

    with col4:
        st.markdown("""
        **Demostrar**  
        Capacidad de análisis estratégico y toma de decisiones
        """)

    st.markdown("### Datos procesados usados para el análisis")
    st.dataframe(df)
    st.divider()

    st.markdown("""
    ## 🎯 La Estrategia de Contenido de Netflix: Un Análisis Evolutivo
    
    **Problema central**: ¿Cómo ha evolucionado la estrategia de contenido de Netflix 
    para mantener su liderazgo en el mercado streaming?
    """)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(distribucionTipoProductosNetflix(df))
            st.markdown("""
            **La revelación**: Haciendo el análisis de la distribución de contenido, descubrimos que Netflix mantiene un equilibrio, tanto en peliculas como TV shows:
            - **Películas**: Representan el 69.7% del catálogo, ofreciendo consumo inmediato
            - **Series**: Constituyen 30.3%, diseñadas para engagement a largo plazo
            - **Brindando en balance entre ambos formatos para atraer y retener suscriptores**
            """)
        with col2:
            st.plotly_chart(paisesMasProduccion(df))
            st.markdown("""
            **El hallazgo estratégico**: El mapa de producción revela una transformación radical:
            - **Estados Unidos** sigue siendo el gigante, pero su dominio está cambiando
            - **India e Inglaterra** estan emergiendo como potencias creativas
            - **Producción distribuida**: De 3 países principales a 10+ centros creativos
            """)

    st.divider()

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(yearAdded_Evolution(df))
            st.markdown("""
            **El punto de inflexión**: La evolución temporal muestra momentos críticos:
            - **2016-2018**: Crecimiento explosivo, el gran despegue del streaming a raiz de la pandemia
            - **2019-2020**: Estabilización y ajuste estratégico despues de la pandemia
            - **2021+**: Consolidación con foco en calidad sobre cantidad
            """)
        with col4:
            st.plotly_chart(clasificacionesTop10(df))
            st.markdown("""
            **El perfil del suscriptor ideal**: Las clasificaciones revelan una estrategia audaz:
            - **Contenido adulto (TV-MA)**: Domina el catálogo, apuntando a suscriptores mayores de 17, un público con mayor poder adquisitivo
            - **Familias (TV-14, PG)**: Segmento secundario pero crucial para retención de futuros suscriptores
            - **Niños (TV-Y, G)**: Inversión estratégica para capturar el siguiente ciclo de suscriptores
            - **El equilibrio perfecto**: Ofertas para cada momento del día y cada miembro de la familia
            """)

    st.divider()
    st.plotly_chart(directorTop10(df))
    st.markdown("""
    **La estrategia de talentos**: Los datos de directores revelan un patrón interesante:
    - **Relaciones estrechas**: Pocos directores producen gran volumen del contenido
    - **El valor de la consistencia**: Directorios confiables que entregan calidad constante
    """)

    st.divider()
    st.markdown("### 📌 Conclusión Final")
    st.markdown("""
    **La fórmula revelada**: Después de analizar cada dimensión, el patrón es claro:
    
    ### 🔑 Los 5 Pilares de la Estrategia Netflix:
    
    1. **🎭 Balance Dual**: Películas para engagement inmediato + Series para retención a largo plazo
    2. **🌎 Globalización Inteligente**: Contenido local que viaja globalmente
    3. **📈 Evolución Constante**: Inicio con pocos contenidos, subida de la demanda por el auge del streaming, estabilización
    4. **🎯 Targeting Precise**: Adultos como base, familias como crecimiento
    5. **🤝 Talentos Estratégicos**: Relaciones profundas con creadores clave
    
    ### 🚀 El Impacto Real:
    
    Esta estrategia explica por qué Netflix:
    - **Mantiene liderazgo** en un mercado cada vez más competitivo
    - **Reduce churn** con contenido para cada tipo de suscriptor
    - **Maximiza ROI** con producciones que viajan across borders
    - **Construye ventajas** sostenibles mediante datos y relaciones
    
    **El veredicto final**: Netflix no vende entretenimiento, vende experiencias culturales personalizadas 
    a escala global. Y los datos lo confirman.
    """)


if __name__ == "__main__":
    main()
