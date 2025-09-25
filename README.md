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

