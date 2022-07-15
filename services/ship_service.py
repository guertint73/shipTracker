import json
import logging
import requests
from utils.constants import Constants
from requests.exceptions import ConnectionError, Timeout, ConnectTimeout


def make_api_call(method, url, expected_code=200, timeout=60):
    """Make an API call."""
    try:
        res = requests.request(method=method, url=url, timeout=timeout)

        res_json = res.json()
    except (ConnectTimeout, Timeout) as e:
        pass

    except ConnectionError as e:
        pass
    except json.decoder.requests.JSONDecodeError as e:
        pass
    except Exception as e:
        pass

    else:
        if res.status_code != expected_code:
            return
        else:
            logging.info(f'Successfully completed the {method} '
                         f'call to url: {url}.')
            return res_json


def get_all_freighters_from_boatnerd(port):
    """Get all vessels from Boatnerd."""
    all_freighters = {
        'freighters': {}
    }

    get_all_res = make_api_call(method='GET', url=Constants.boatnerd_url)
    features = get_all_res.get('features', [])
    for feature in features:
        vessel = feature.get('properties')
        if not vessel:
            return

        if vessel.get('vesselType') == Constants.freighter:
            vessel_status = vessel.get('status')
            vessel_destination = vessel.get('destination')
            freighter = {
                'name': vessel.get('name'),
                'status': vessel_status,
                'eta': vessel.get('eta'),
                'destination': vessel_destination,
                'speed': vessel.get('speed'),
                'length': vessel.get('length'),
                'width': vessel.get('width'),
                'draft': vessel.get('draft')
            }
            if vessel_destination and vessel_destination.lower() == port.lower():
                if vessel_status in all_freighters['freighters'].keys():
                    all_freighters['freighters'][vessel_status].append(freighter)
                else:
                    all_freighters['freighters'][vessel_status] = [freighter]

    return all_freighters
