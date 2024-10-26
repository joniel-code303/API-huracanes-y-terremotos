from flask import Flask, jsonify, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from apscheduler.schedulers.background import BackgroundScheduler
from models import Hurricane, Earthquake
from clients import NOAAClient, EarthquakeClient
from notifier import send_email
from logger import setup_logging

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Cambia a un valor seguro en producción
setup_logging()

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Simulación de base de datos
users = {}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Inicializa clientes
noaa_client = NOAAClient()
earthquake_client = EarthquakeClient()

# Almacenamiento en memoria para huracanes y terremotos
hurricanes = []
earthquakes = []

@app.route('/hurricanes', methods=['POST', 'GET'])
def manage_hurricanes():
    """Agrega o obtiene huracanes."""
    if request.method == 'POST':
        data = request.json
        hurricane = Hurricane(**data)
        hurricanes.append(hurricane)
        app.logger.info(f"Huracán agregado: {hurricane.to_dict()}")
        return jsonify({"message": "Huracán agregado"}), 201
    return jsonify([hurricane.to_dict() for hurricane in hurricanes]), 200

@app.route('/earthquakes', methods=['POST', 'GET'])
def manage_earthquakes():
    """Agrega o obtiene terremotos."""
    if request.method == 'POST':
        data = request.json
        earthquake = Earthquake(**data)
        earthquakes.append(earthquake)
        app.logger.info(f"Terremoto agregado: {earthquake.to_dict()}")
        return jsonify({"message": "Terremoto agregado"}), 201
    return jsonify([earthquake.to_dict() for earthquake in earthquakes]), 200

@app.route('/alerts')
def check_alerts():
    """Verifica alertas de huracanes y terremotos."""
    hurricane_alerts = noaa_client.get_hurricane_alerts()
    earthquake_alerts = earthquake_client.get_earthquake_alerts()

    if hurricane_alerts:
        send_email("Alertas de Huracán", hurricane_alerts)
    if earthquake_alerts:
        send_email("Alertas de Terremoto", earthquake_alerts)

    return jsonify({"message": "Verificación de alertas realizada."}), 200

# Scheduler para verificar alertas periódicamente
scheduler = BackgroundScheduler()
scheduler.add_job(check_alerts, 'interval', minutes=10)
scheduler.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
