import json
from flask import Response

import utils.app_setup as AppSetup

import services.ship_service as ShipService

app = AppSetup.create_flask_app()


@app.route('/health', methods=['GET'])
def health():
    health_res = {
        'status': 'Server is running.'
    }
    return Response(response=json.dumps(health_res),
                    status=200,
                    mimetype='application/json')


@app.route('/freighters', methods=['GET'])
def get_all_freighters():
    all_freighters = ShipService.get_all_freighters_from_boatnerd()
    return Response(response=json.dumps(all_freighters),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
    app.run(port=6565)
