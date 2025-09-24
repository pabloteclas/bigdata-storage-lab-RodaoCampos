# Diccionario de Datos — Esquema Canónico

El siguiente esquema canónico estandariza los datos financieros para su posterior análisis.  
Todos los orígenes deberán transformarse a este modelo:

| Campo    | Tipo     | Formato / Unidad | Descripción                                |
|----------|----------|------------------|--------------------------------------------|
| date     | Date     | YYYY-MM-DD       | Fecha de la transacción                    |
| partner  | String   | Texto libre      | Nombre de cliente/proveedor/entidad asociada |
| amount   | Float    | EUR              | Importe de la transacción en euros         |

---

## Mapeos de campos (Origen → Canónico)

| Origen (CSV) | Campo origen     | Campo canónico | Nota de transformación            |
|--------------|-----------------|----------------|-----------------------------------|
| ERP A        | fecha_transac   | date           | Convertir a formato ISO (YYYY-MM-DD) |
| ERP A        | cliente_nombre  | partner        | Texto tal cual, normalizar tildes |
| ERP A        | valor_total     | amount         | Convertir a float EUR              |
| CRM B        | date_created    | date           | Parsear timestamp a solo fecha    |
| CRM B        | account_name    | partner        | Renombrar                          |
| CRM B        | importe         | amount         | Asegurar conversión a EUR          |

---
