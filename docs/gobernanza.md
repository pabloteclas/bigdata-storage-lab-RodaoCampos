# Lineamientos de Gobernanza de Datos

La gobernanza de datos asegura calidad, seguridad y trazabilidad en el ciclo de vida de la información.

---

## 1. Origen y Linaje
- Todo dataset debe registrar **origen del CSV** (nombre del sistema, fecha de extracción).  
- Mantener **linaje** claro: `raw → bronze → silver → gold`.  
- Documentar cada transformación (qué se cambia y por qué).  

---

## 2. Validaciones mínimas
- **Fechas:** deben cumplir formato `YYYY-MM-DD`.  
- **Partner:** no nulo, sin caracteres especiales críticos.  
- **Amount:** numérico, no nulo, convertido a euros.  
- **Duplicados:** eliminación o marcaje con justificación.  

---

## 3. Política de mínimos privilegios
- Cada usuario debe tener solo los permisos estrictamente necesarios.  
- Separar roles de **lectura**, **escritura** y **administración**.  
- Prohibido el acceso directo a datos en **raw** sin justificación.  

---

## 4. Trazabilidad
- Registrar metadatos de cada proceso (timestamp, usuario, script).  
- Mantener logs accesibles y versionados.  
- Asegurar que cada registro en Gold pueda reconstruirse hacia su origen en Raw.  

---

## 5. Roles
- **Data Engineer:** diseña y mantiene pipelines (Ingesta, Validación, Transformación).  
- **Data Steward:** asegura la calidad y la gobernanza de los datos.  
- **Data Analyst:** consume datos en Silver/Gold para reportes y KPIs.  
- **Administrador:** gestiona accesos y políticas de seguridad.  
