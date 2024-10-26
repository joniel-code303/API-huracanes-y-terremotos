# API de Huracanes y Terremotos

Esta API permite gestionar y monitorear información sobre huracanes y terremotos. Proporciona endpoints para agregar y obtener datos de huracanes y terremotos, así como para verificar alertas de eventos severos. Utiliza Flask como framework web y está diseñada para ser fácil de usar y extender.

## Funcionalidades

- **Gestión de Huracanes**: 
  - Agregar nuevos huracanes con información relevante como nombre, categoría, velocidad del viento, presión y ubicación.
  - Obtener una lista de todos los huracanes almacenados o consultar información específica de un huracán.

- **Gestión de Terremotos**:
  - Agregar nuevos terremotos con datos como magnitud, ubicación y profundidad.
  - Obtener una lista de todos los terremotos almacenados.

- **Verificación de Alertas**:
  - Monitorear y enviar notificaciones sobre alertas de huracanes y terremotos críticos a través de correo electrónico.
  
- **Interfaz de Usuario**: 
  - Implementación de autenticación de usuario para una gestión segura de la API.

## Tecnologías Utilizadas

- **Flask**: Framework web para desarrollar la API.
- **APScheduler**: Para programar la verificación de alertas.
- **Requests**: Para hacer llamadas a APIs externas.
- **Flask-Login**: Para gestionar la autenticación de usuarios.
- **SMTP**: Para enviar notificaciones por correo electrónico.

## Instalación

Para ejecutar esta API localmente, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/joniel-code303/tu-repo.git
   cd tu-repo

pip install -r requirements.txt


python app.py



Puedes personalizar los detalles según sea necesario, como el nombre del repositorio y cualquier otra información relevante que quieras incluir. ¡Déjame saber si necesitas ajustes o más información!



### File Descriptions

1. **app.py**: The main application file where the Flask app is initialized and runs.
2. **requirements.txt**: Contains all the necessary Python packages required for the application.
3. **email_notifier.py**: Manages the email notification functionality.
4. **hurricane_checker.py**: Contains the logic to check for hurricane alerts.
5. **logging_config.py**: Configures logging for the application.
6. **models.py**: Defines the data models used in the application (e.g., Hurricane, Earthquake).
7. **routes.py**: Defines the API endpoints for managing hurricanes and earthquakes.
8. **templates/**: Contains any HTML templates for rendering web pages.

Feel free to adjust the file names and structure to suit your specific needs. If you have any further requests or questions, let me know!
