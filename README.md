# Descripción de la Solución:

La solución proporcionada incluye la implementación básica de un sistema de una compañía aérea que se dedica al transporte de paquetes de clientes. Se han creado tres clases principales: `Cliente`, `Paquete`, y `CompaniaAerea`.

- La clase `Cliente` representa a un cliente y tiene un atributo `nombre`.
- La clase `Paquete` representa un paquete que pertenece a un cliente. Cada paquete se crea asociado a un cliente.
- La clase `CompaniaAerea` es la entidad principal y tiene la responsabilidad de transportar paquetes y generar informes diarios. Lleva un registro de los paquetes transportados y del total recaudado.

El método `transportar_paquete` en la clase `CompaniaAerea` permite añadir paquetes a la lista de paquetes transportados y actualizar el total recaudado.

El método `generar_reporte_diario` en la misma clase genera un informe que incluye el total de paquetes transportados y el total recaudado para un día específico.

# Descripción de las Pruebas Unitarias:

Se han creado pruebas unitarias utilizando el módulo `unittest` para verificar el correcto funcionamiento de la solución. Estas pruebas se centran en dos aspectos clave de la funcionalidad:

1. **Prueba `test_transportar_paquete`:**
   - Verifica que el método `transportar_paquete` de la clase `CompaniaAerea` añada correctamente paquetes a la lista de paquetes transportados.
   - Verifica que el total recaudado se actualice correctamente después de transportar un paquete.

2. **Prueba `test_generar_reporte_diario`:**
   - Transporta algunos paquetes para asegurar que haya datos para incluir en el informe.
   - Utiliza una fecha específica para generar el informe diario y verifica que el informe generado coincida con el resultado esperado.

Estas pruebas proporcionan una cobertura básica para garantizar que la lógica principal del sistema funcione correctamente y que los informes diarios se generen de manera precisa.

