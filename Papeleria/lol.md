## Diagrama de clases
secucnia, procesos, clases
---
>**Usuarios de DB, nosql**
```mermaid
classDiagram
    class Usuario {
        - _id: int
        - nombre: String
        - email: String
        - contraseña: Sting
        - iniciarSesion: String
    }
```

>**entidad relacion**
```mermaid
classDiagram
    class Usuario {
        +id: int
        +nombre: string
        +email: string
        +contrasena: string
        +registrar()
        +iniciarSesion()
    }

    class Publicacion {
        +id: int
        +titulo: string
        +contenido: string
        +fechaCreacion: date
        +usuario: Usuario
    }

    Usuario "1" -- "*" Publicacion : publica
```

## Diagrama casos de uso
>**Para Inicio de sesion**

```mermaid
sequenceDiagram
    participant Usuario
    participant Sistema

    Usuario->>Sistema: Iniciar sesión
    activate Sistema
    Sistema-->>Usuario: Solicitar usuario y contraseña
    Usuario->>Sistema: Ingresar usuario y contraseña
    Sistema->>Sistema: Validar credenciales
    alt Credenciales válidas
        Sistema-->>Usuario: Acceso concedido
    else Credenciales inválidas
        Sistema-->>Usuario: Acceso denegado
    end
    deactivate Sistema

```

>**para iniciar una compra**
```mermaid
sequenceDiagram
    participant Cliente
    participant Sistema
    participant Cocina
    participant Caja

    Cliente->>Sistema: Buscar menú
    activate Sistema
    Sistema-->>Cliente: Mostrar menú
    Cliente->>Sistema: Seleccionar plato
    Cliente->>Sistema: Agregar al carrito
    Cliente->>Sistema: Finalizar compra
    activate Caja
    Sistema->>Caja: Procesar pago
    Caja-->>Sistema: Pago confirmado/rechazado
    deactivate Caja
    alt Pago confirmado
        Sistema->>Cocina: Preparar pedido
        activate Cocina
        Cocina-->>Sistema: Pedido listo
        deactivate Cocina
        Sistema->>Cliente: Pedido listo para recoger
    else Pago rechazado
        Sistema->>Cliente: Pago rechazado
    end
    deactivate Sistema

```

>**para iniciar una reserva**
```mermaid
sequenceDiagram
    participant Cliente
    participant Sistema
    participant Cocina
    participant Caja

    Cliente->>Sistema: Buscar menú
    activate Sistema
    Sistema-->>Cliente: Mostrar menú
    loop Agregar platos
        Cliente->>Sistema: Seleccionar plato
        Sistema->>Cliente: Agregar al carrito
    end
    Cliente->>Sistema: Finalizar compra
    activate Caja
    Sistema->>Caja: Procesar pago
    alt Pago confirmado
        Caja-->>Sistema: Pago confirmado
        Sistema->>Cocina: Preparar pedido
        activate Cocina
        Cocina-->>Sistema: Pedido listo
        deactivate Cocina
        Sistema->>Cliente: Pedido listo para recoger
    else Pago rechazado
        Caja-->>Sistema: Pago rechazado
        Sistema->>Cliente: Pago rechazado
    end
    deactivate Caja
    deactivate Sistema

```
>**para gestion de menu**
```mermaid
sequenceDiagram
    participant Administrador
    participant Sistema

    Administrador->>Sistema: Agregar nuevo plato
    activate Sistema
    Sistema-->>Administrador: Confirmar adición o mostrar error
    deactivate Sistema

    Administrador->>Sistema: Modificar plato existente
    activate Sistema
    Sistema-->>Administrador: Confirmar modificación o mostrar error
    deactivate Sistema

    Administrador->>Sistema: Eliminar plato
    activate Sistema
    Sistema-->>Administrador: Confirmar eliminación o mostrar error
    deactivate Sistema
```
>**para gestion de reservas**
```mermaid
sequenceDiagram
    participant Cliente
    participant Sistema
    participant Administrador

    Cliente->>Sistema: Realizar reserva
    activate Sistema
    Sistema-->>Cliente: Confirmar reserva o mostrar disponibilidad
    deactivate Sistema

    Administrador->>Sistema: Consultar reservas
    activate Sistema
    Sistema-->>Administrador: Mostrar lista de reservas
    deactivate Sistema

    Administrador->>Sistema: Cancelar reserva
    activate Sistema
    Sistema-->>Administrador: Confirmar cancelación
    deactivate Sistema
```


## Diagrama de secuencia

>**para la utenticaion dcon emai**
```mermaid
sequenceDiagram
    participant Usuario
    participant Aplicación
    participant API Autenticación

    Usuario->>Aplicación: Ingresar email y contraseña
    activate Aplicación
    Aplicación->>API Autenticación: Verificar credenciales
    activate API Autenticación
    API Autenticación-->>Aplicación: Usuario autenticado/no autenticado
    deactivate API Autenticación
    alt Usuario autenticado
        Aplicación->>Usuario: Bienvenido
        Aplicación->>Aplicación: Cargar datos de usuario
    else Usuario no autenticado
        Aplicación->>Usuario: Credenciales incorrectas
    end
    deactivate Aplicación
```
---
# Segundo Sprint
<br>
<br>

---
#### Diagramas de secuencia.
>**Para el registro de usuarios**
```mermaid
sequenceDiagram
    participant Usuario
    participant SistemaWeb as Sistema Bambu
    participant BaseDatos as Base de Datos

    Usuario->>SistemaWeb: Inicia el registro
    SistemaWeb->>Usuario: Solicita datos (nombre, correo, etc.)
    Usuario->>SistemaWeb: Envia datos del registro
    SistemaWeb->>BaseDatos: Verifica si el correo ya está registrado
    BaseDatos->>SistemaWeb: Responde con el estado (registrado OK/ocurrio un error! )
    SistemaWeb->>Usuario: Informa si el correo está disponible o no
    alt Correo disponible
        SistemaWeb->>BaseDatos: Guarda los datos del usuario
        BaseDatos->>SistemaWeb: Datos registrados con éxito
        SistemaWeb->>Usuario: Muestra mensaje de registro exitoso
    else Correo no disponible
        SistemaWeb->>Usuario: Muestra mensaje de error (correo ya registrado)
    end

```
>**Para la pasarela de pagos**
```mermaid
sequenceDiagram
    participant Cliente
    participant Sistema Bambu
    participant PasarelaPago

    Cliente->>Sistema Bambu: Buscar producto
    activate Sistema Bambu
    Sistema Bambu->>Cliente: Mostrar resultados
    Cliente->>Sistema Bambu: Seleccionar producto
    Sistema Bambu->>Cliente: Mostrar detalles del producto
    Cliente->>Sistema Bambu: Agregar al carrito
    Cliente->>Sistema Bambu: Ir a pagar
    activate PasarelaPago
    Sistema Bambu->>PasarelaPago: Procesar pago
    PasarelaPago-->>Sistema Bambu: Pago exitoso/fallido
    deactivate PasarelaPago
    alt Pago exitoso
        Sistema Bambu->>Cliente: Confirmar compra
        Sistema Bambu->>Cliente: Enviar confirmación por email
    else Pago fallido
        Sistema Bambu->>Cliente: Informar error de pago
    end
    deactivate Sistema Bambu
```
>**Para la verificacion del pago**
```mermaid
sequenceDiagram
    participant Usuario
    participant SistemaWeb as Sistema Bambu
    participant SistemaPago as Sistema de Pago "Stripe"
    participant BaseDatos as Base de Datos 

    Usuario->>SistemaWeb: Inicia el pago
    SistemaWeb->>Usuario: Solicita datos de pago (tarjeta D/C)
    Usuario->>SistemaWeb: Envía datos de pago
    SistemaWeb->>SistemaPago: Envía detalles de pago
    SistemaPago->>SistemaPago: Verifica información del pago
    alt Pago aprobado
        SistemaPago->>SistemaWeb: Responde con aprobación de pago
        SistemaWeb->>BaseDatos: Actualiza estado del pedido (pagado)
        BaseDatos->>SistemaWeb: Estado actualizado
        SistemaWeb->>Usuario: Muestra confirmación de pago y pedido
    else Pago rechazado
        SistemaPago->>SistemaWeb: Responde con rechazo de pago
        SistemaWeb->>Usuario: Muestra mensaje de error (pago fallido)
    end

```

>**Para el proceso de compra de comida**
```mermaid
sequenceDiagram
    participant Usuario
    participant SistemaWeb as Sistema Bambu
    participant BaseDatos as Base de Datos
    participant SistemaPago as Sistema de Pago

    Usuario->>SistemaWeb: Inicia sesión
    SistemaWeb->>Usuario: Muestra menú de comidas
    Usuario->>SistemaWeb: Selecciona productos y agrega al carrito
    SistemaWeb->>Usuario: Muestra el carrito de compras
    Usuario->>SistemaWeb: Revisa el carrito y confirma compra
    SistemaWeb->>BaseDatos: Valida disponibilidad de productos
    BaseDatos->>SistemaWeb: Responde disponibilidad
    SistemaWeb->>Usuario: Muestra opción de pago
    Usuario->>SistemaWeb: Ingresa datos de pago (Stripe)
    SistemaWeb->>SistemaPago: Envía datos de pago
    SistemaPago->>SistemaWeb: Responde con resultado de pago (realizado/fallido)
    SistemaWeb->>Usuario: Muestra resultado de la transacción
    SistemaWeb->>BaseDatos: Actualiza estado de la compra
    BaseDatos->>SistemaWeb: Compra registrada

```

---
# Para el Quinto Hito - Analisi y Diseño II
<br>

>**Diagrama de secucnia: para registro e inicio de sesion, antes de pedir un plato.**
```mermaid
sequenceDiagram
    participant Usuario
    participant Sistema
    
    Usuario->>Sistema: Visitar la página principal (comida)
    Sistema->>Usuario: Mostrar opción de "Iniciar sesión" o "Registrarse"
    
    Usuario->>Sistema: Elige "Registrarse"
    Sistema->>Usuario: Solicitar datos (nombre, correo, teléfono)
    Usuario->>Sistema: Enviar datos de registro
    Sistema->>Sistema: Validar correo electrónico
    Sistema->>Sistema: Cifrar datos sensibles
    Sistema->>Usuario: Confirmar registro exitoso

    Usuario->>Sistema: Elige "Iniciar sesión"
    Sistema->>Usuario: Solicitar correo y contraseña
    Usuario->>Sistema: Enviar correo y contraseña
    Sistema->>Sistema: Validar credenciales
    Sistema->>Usuario: Confirmar inicio de sesión
    
    Usuario->>Sistema: Realizar pedido de comida
    Sistema->>Usuario: Mostrar menú de comida
    Usuario->>Sistema: Seleccionar artículos para el pedido
    Sistema->>Usuario: Confirmar pedido

```

>**Diagrama de secucnia: para el contacto del WhatsApp**
```mermaid
sequenceDiagram
    participant Cliente
    participant Sistema 'Bambu'
    participant WhatsApp

    Cliente->>Sistema: Ver botón de WhatsApp
    Sistema->>Cliente: Mostrar botón de WhatsApp
    
    Cliente->>Sistema: Hacer clic en el botón de WhatsApp
    Sistema->>WhatsApp: Redirigir al cliente a la conversación
    WhatsApp->>Cliente: Mostrar conversación de WhatsApp

```

