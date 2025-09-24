# bigdata-storage-lab-RodaoCampos
# De CSVs heterogéneos a un almacén analítico confiable  
**Laboratorio Técnico — `bigdata-storage-lab-<apellido>`**

---

## 1. Objetivo

El propósito de este laboratorio es **diseñar e implementar un flujo completo de ingesta, validación y normalización de datos heterogéneos en CSV** para consolidarlos en un **almacén analítico confiable**.  

La secuencia de trabajo será:

1. **Ingesta:** lectura y almacenamiento inicial de múltiples CSV (estructuras dispares, columnas faltantes, diferentes codificaciones/formatos).  
2. **Validación:** aplicación de reglas de calidad (tipos de datos, valores nulos, rangos válidos, duplicados).  
3. **Normalización:** unificación de esquemas, tipos de datos y claves de integración.  
4. **Zonas de almacenamiento (Medallion Architecture):**  
   - **Bronze:** datos crudos tal como se ingieren.  
   - **Silver:** datos limpios y normalizados.  
   - **Gold:** modelos listos para analítica y generación de KPIs.  
5. **KPIs:** cálculo de métricas simples a partir de los datos consolidados (ej. volumen total de registros válidos, % de errores, tendencias agregadas).

---

## 2. Entregables

- **Repositorio GitHub público (`bigdata-storage-lab-<apellido>`):**  
  - Código fuente (Python/SQL/ETL).  
  - Scripts/notebooks de validación y normalización.  
  - Estructura de carpetas clara (bronze/silver/gold).  
  - Documentación (`README.md`, diagramas, instrucciones de ejecución).  

- **Aplicación Streamlit:**  
  - Dashboard que muestre KPIs y permita navegar los datos en las diferentes capas.  
  - Visualizaciones básicas (tablas, gráficos de barras/líneas/pastel según pertinencia).  

---

## 3. Criterios de Evaluación

1. **Diseño y justificación:**  
   - Claridad en la arquitectura propuesta y sus decisiones.  
   - Uso de buenas prácticas (nombres consistentes, modularidad).  

2. **Calidad de los datos:**  
   - Aplicación de validaciones relevantes y registro de errores.  
   - Nivel de limpieza y consistencia logrado en Silver/Gold.  

3. **Trazabilidad y modelo de almacén de datos:**  
   - Evidencia de flujo claro Bronze → Silver → Gold.  
   - Capacidad de reconstruir pasos de transformación.  

4. **Documentación:**  
   - Instrucciones reproducibles (setup, dependencias, ejecución).  
   - Breve memoria técnica justificando decisiones.  

---

## 4. Qué **NO** subir

- **Datos sensibles, confidenciales o con información personal identificable (PII).**  
- Archivos CSV reales de empresas/instituciones.  
- Claves de acceso, contraseñas, tokens o credenciales en el repo o app.  

*(Se recomienda generar datos sintéticos o usar datasets públicos abiertos.)*

---

## 5. Tiempo estimado por fase

| Fase                        | Tiempo estimado |
|-----------------------------|-----------------|
| Ingesta de CSVs             | 2 h             |
| Validación de calidad       | 3 h             |
| Normalización y esquemas    | 4 h             |
| Diseño Bronze/Silver/Gold   | 3 h             |
| Desarrollo de KPIs          | 3 h             |
| Implementación en Streamlit | 3 h             |
| Documentación final         | 2 h             |
| **Total aproximado**        | **20 h**        |

---

📌 **Entrega final:** subir el repo en GitHub público (`bigdata-storage-lab-<apellido>`) e incluir el link a la app de Streamlit desplegada.
