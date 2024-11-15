# ECF Validation - Republica Dominicana 

Este modulo implementa la validacion de los comprobantes fiscales electronicos que se deben emitir mediante la direccion general de impuestos internos (DGII), segun la ley 32-23 de facturacion electronica.

## Funciones principales

- Generacion de archivo (JSON) con datos de factura necesarios para la validacion de todos los tipos de comprobantes electronicos.
- Integracion de los valores necesarios para la facturacion electronica.
- Almacenamiento de respuestas recibidas de la DGII por cada validacion realizada

# Contactos

## Consideraciones

Es importante que al crear un contacto sean tomados en cuenta algunos datos relevantes, para que al validar su comprobante no tenga inconvenientes, estos son los datos mas importantes para cada contacto (Segun aplique):

RAZON SOCIAL (NOMBRE)
RNC, CEDULA O PASAPORTE (O ID FISCAL CORRESPONDIENTE SI ES EXTRANJERO)
TIPO DE CONTRIBUYENTE

NOTA: Estos datos pueden variar su importancia segun el tipo de comprobante, por ejemplo, en una factura de consumo (E32)
no es necesario agregar un RNC o CEDULA.

# Almacenamiento

Las respuestas recibidas desde la DGII seran almacenadas en 'Contabilidad -> Reportes -> Comprobantes' estos contienen los
datos recibidos en cada respuesta de la DGII, por ejemplo:

E-ncf: E310000000001
Fecha de firma: 10/9/2024 10:00:09 PM
Tipo de comprobante: E31
Comprador: 101000000
Impuesto: 180.00
Importe total: 1,180.00
Estado: Aceptado

Estos datos seran almacenados unicamente en la base de datos de su sistema odoo, y puede limpiarlos si asi se requiere.

# Datos Obligatorios, condicionales y no aplicables para cada tipo de comprobante

La cantidad de datos posibles para envio es extensa, cada tipo de comprobante esta sujeto a llevar algun dato obligatorio,
condicional y no aplicable. Tambien existen los datos opcionales pero esto es solo preferencia del cliente, aqui detallaremos
que datos exactamente llevara un tipo de comprobante, y si este dato es obligatorio, condicional o no aplicable. Cada uno de olos datos estara indicado con su nombre tecnico que debe llevar een el Xml.

## Factura de credito fiscal E31

### Obligatorios



