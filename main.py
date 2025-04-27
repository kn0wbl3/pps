from src import create_app
import logging

logger = logging.getLogger(__name__)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
