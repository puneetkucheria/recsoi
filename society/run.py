from society_registry import app
import os

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)

