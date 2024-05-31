# Pruebas de la API

Este proyecto contiene pruebas automatizadas para la API de `https://jsonplaceholder.typicode.com/albums`.

## Instrucciones para Ejecutar las Pruebas

### Requisitos

- Python 3.x
- `requests` y `requests-oauthlib`

### Instalación de Dependencias

Instala las dependencias necesarias usando `pip`:

```bash
pip install requests requests-oauthlib
```

### Ejecución de las Pruebas
#### Pruebas sin Autenticación

Para ejecutar las pruebas sin autenticación:

```bash
python test_api.py
```

#### Pruebas con Autenticación de Client Credentials

Para ejecutar las pruebas con autenticación de client credentials:

```bash
python test_api_with_auth.py
```

#### Pruebas con Autenticación de Authorization Code

Para ejecutar las pruebas con autenticación de authorization code:

```bash
python test_api_with_auth_code.py
```

### BDD Given-When-Then

#### Sin Autenticación

Dado que el API de `https://jsonplaceholder.typicode.com/albums` está disponible,
Cuando realizo una solicitud GET a la API,
Entonces la respuesta debe contener al menos los primeros 5 elementos con los títulos esperados.

#### Con Autenticación OAuth 2.0 (Client Credentials)

Dado que el API requiere autenticación OAuth 2.0 con client credentials,
Cuando obtengo un token de acceso válido usando client credentials,
Entonces puedo realizar una solicitud GET a la API con el token y obtener los datos esperados.

#### Con Autenticación OAuth 2.0 (Authorization Code)

Dado que el API requiere autenticación OAuth 2.0 con authorization code,
Cuando obtengo un token de acceso válido usando authorization code,
Entonces puedo realizar una solicitud GET a la API con el token y obtener los datos esperados.
