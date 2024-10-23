## Diagrama de clases

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

```mermaid
sequenceDiagram
    participant Cliente
    participant Tienda
    participant PasarelaPago

    Cliente->>Tienda: Buscar producto
    activate Tienda
    Tienda->>Cliente: Mostrar resultados
    Cliente->>Tienda: Seleccionar producto
    Tienda->>Cliente: Mostrar detalles del producto
    Cliente->>Tienda: Agregar al carrito
    Cliente->>Tienda: Ir a pagar
    activate PasarelaPago
    Tienda->>PasarelaPago: Procesar pago
    PasarelaPago-->>Tienda: Pago exitoso/fallido
    deactivate PasarelaPago
    alt Pago exitoso
        Tienda->>Cliente: Confirmar compra
        Tienda->>Cliente: Enviar confirmación por email
    else Pago fallido
        Tienda->>Cliente: Informar error de pago
    end
    deactivate Tienda
```

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