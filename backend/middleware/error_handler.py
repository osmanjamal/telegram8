from flask import jsonify

def handle_error(error):
    response = jsonify({
        "error": {
            "type": error.__class__.__name__,
            "message": str(error)
        }
    })
    response.status_code = getattr(error, 'code', 500)
    return response