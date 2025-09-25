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

## 🏆 Retos opcionales (dificultad creciente)

### 🔹 Reto A: Validaciones extra
- **Objetivo:** Asegurar calidad de datos mediante reglas adicionales.  
- **Pasos sugeridos:**  
  1. En `validate.py`, implementar control de rangos de fechas (ej. fecha ≥ 2015).  
  2. Detectar duplicados según clave natural (ej. `id_cliente + fecha`).  
  3. Rechazar filas no válidas y registrarlas en un log.  
- **Criterio de aceptación:**  
  - En el repo se ve la función extra en `validate.py`.  
  - La app muestra conteo de registros rechazados.  

---

### 🔹 Reto B: Métrica de veracidad en la app
- **Objetivo:** Calcular un % de registros válidos por archivo y mostrarlo en el dashboard.  
- **Pasos sugeridos:**  
  1. Modificar `validate.py` para devolver (válidos, inválidos).  
  2. Calcular `veracidad = válidos / total * 100`.  
  3. En `streamlit_app.py`, añadir un gráfico simple (ej. barras).  
- **Criterio de aceptación:**  
  - Al subir un CSV, la app muestra la métrica % por archivo.  
  - Evidencia en README (captura).  

---

### 🔹 Reto C: Tabla Gold con linaje
- **Objetivo:** Crear una tabla optimizada para reporting y mantener trazabilidad.  
- **Pasos sugeridos:**  
  1. Definir tabla **Gold**: ej. ventas mensuales por categoría (`fecha, categoria, ventas_total`).  
  2. Documentar en README cómo se genera desde Silver.  
  3. Añadir metadato de linaje (ej. en columna `origen_archivo`).  
- **Criterio de aceptación:**  
  - Archivo `gold.csv` generado en `/data/gold/`.  
  - README explica reglas de derivación y linaje.  

---

### 🔹 Reto D: Ensayo CSV vs Parquet
- **Objetivo:** Comparar formatos y concluir cuál es más eficiente en este caso.  
- **Pasos sugeridos:**  
  1. Generar dataset sintético de al menos 100k filas.  
  2. Guardar como CSV y Parquet.  
  3. Medir: tamaño en disco y tiempo de lectura con pandas.  
  4. Escribir conclusiones en README.  
- **Criterio de aceptación:**  
  - Notebook o script con el experimento incluido en `src/`.  
  - Resultados (tabla comparativa) documentados en README.  

---

### 🔹 Reto E: Simulación paso a streaming
- **Objetivo:** Analizar cómo evolucionaría la arquitectura hacia streaming.  
- **Pasos sugeridos:**  
  1. Identificar qué capa cambia primero (ej. ingesta → micro-batches a colas).  
  2. Diseñar esquema de flujo actualizado (diagrama simple en `docs/`).  
  3. Redactar pseudocódigo de ingesta en tiempo real (ej. usando colas + validación online).  
- **Criterio de aceptación:**  
  - Diagrama en `docs/streaming_design.png` o `.md`.  
  - Pseudocódigo documentado en README.  
  - Justificación de la capa que se adapta primero.  


## 🚀 Pega y corre — Guía rápida de entrega

### Pasos mínimos (en orden)

1. **Crear repositorio con estructura**  
   - Nombre: `bigdata-storage-lab-<apellido>`.  
   - Crear carpetas (`src`, `data/raw`, `data/bronze`, `data/silver`, `data/gold`, `docs`, `tests`).  
   - Tiempo estimado: **20 min**.  
   - ✔️ Verificar: que todas las carpetas aparecen en GitHub con `.gitkeep`.

2. **Pegar archivos base**  
   - Subir `ingest.py`, `validate.py`, `transform.py`, `streamlit_app.py`, `requirements.txt`.  
   - Tiempo estimado: **30 min**.  
   - ✔️ Verificar: el repo abre bien los archivos y no hay errores de sintaxis al ejecutar `streamlit run streamlit_app.py` en local.

3. **Subir CSVs de prueba a `/data/raw/`**  
   - Usar datasets sintéticos (ej. ventas, IoT, fraude).  
   - Tiempo estimado: **15 min**.  
   - ✔️ Verificar: que la app procesa al menos 2–3 archivos distintos y genera Bronze + Silver.

4. **Desplegar en Streamlit Community Cloud**  
   - Conectar el repo, elegir `streamlit_app.py` como archivo principal.  
   - Tiempo estimado: **30 min**.  
   - ✔️ Verificar: la URL abre y se pueden subir CSVs desde el navegador.

5. **Completar README con reflexiones**  
   - Añadir sección “📝 Prompts de reflexión” y responder los 5 puntos.  
   - Tiempo estimado: **20 min**.  
   - ✔️ Verificar: README tiene arquitectura, justificación (5V), checklist, capturas en `docs/`.

6. **Entregar URLs**  
   - **Repo público en GitHub.**  
   - **URL de la app en Streamlit.**  
   - Tiempo estimado: **5 min**.  
   - ✔️ Verificar: ambos links son accesibles sin credenciales.

---

### ⏱️ Tiempo total estimado: **~2 h**

### ✅ Checklist final antes de entregar
- [ ] URL de Streamlit funcional.  
- [ ] `bronze.csv` y `silver.csv` generados en `/data`.  
- [ ] README con decisiones justificadas + reflexiones respondidas.  
- [ ] Diccionario y gobernanza completos en `docs/`.  
- [ ] Capturas de pantallas del dashboard incluidas.  
- [ ] Tests/checklist.md marcado.  


### 📝 Prompts de reflexión — Ejemplo de respuestas completas

1. **Pregunta:** V dominante hoy y V dominante si se duplica el tráfico (justifica en 3 líneas)  
   **Respuesta:**  
   Hoy la V dominante es **Velocidad**, porque necesitamos procesar los CSV y micro-batches rápidamente.  
   Si el tráfico se duplica, la V dominante sería **Volumen**, ya que el número de registros aumentaría significativamente.  
   Esto impacta en almacenamiento y procesamiento, requiriendo ajustes de pipeline.

2. **Pregunta:** Trade-off elegido (ej.: más compresión vs CPU): por qué lo elegiste y cómo lo medirás  
   **Respuesta:**  
   Elegimos compresión moderada (**Parquet con snappy**) para equilibrar tamaño de almacenamiento y CPU.  
   Esto reduce espacio sin afectar demasiado el tiempo de lectura.  
   Mediremos impacto con benchmarks de ingestión y consultas en Silver.

3. **Pregunta:** Por qué “inmutable + linaje” mejora veracidad y qué coste añade  
   **Respuesta:**  
   Mantener datos **inmutables** y registrar **linaje** asegura que siempre podemos rastrear cada registro hasta su origen, aumentando la confianza en los datos.  
   El coste añadido es **mayor consumo de almacenamiento** y algo de overhead en metadatos.

4. **Pregunta:** KPI principal y SLA del dashboard: qué decisión habilita y por qué esa latencia  
   **Respuesta:**  
   KPI principal: **volumen total de transacciones válidas por mes**.  
   SLA: actualización en **<5 min** tras la subida de CSV.  
   Esta latencia permite análisis casi en tiempo real sin sobrecargar el servidor.

5. **Pregunta:** Riesgo principal del diseño y mitigación técnica concreta  
   **Respuesta:**  
   Riesgo: **errores de encoding o formatos inconsistentes** en CSV de origen.  
   Mitigación: normalización automática con **fallback UTF-8 → Latin-1**, y validaciones en Bronze que registran fallos para poder corregirlos posteriormente.

