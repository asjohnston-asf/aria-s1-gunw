from collections import defaultdict
from datetime import datetime

import requests


# TODO: support frames crossing antimeridian
# TODO: support ascending frames crossing equator


def get_frame_by_id(frame_id: int) -> dict:
    for direction in ['ascending', 'descending']:
        response = requests.get(f'https://d3g9emy65n853h.cloudfront.net/ARIA_S1_GUNW/{direction}.geojson')
        response.raise_for_status()
        for frame in response.json()['features']:
            if frame['properties']['id'] == frame_id:
                return frame
    raise ValueError(f'No frame found for id {frame_id}')


def get_polygon(frame):
    coordinates = ','.join(' '.join(str(coord) for coord in point) for point in frame['geometry']['coordinates'][0])
    return f'polygon(({coordinates}))'


def get_granules_for_frame(frame: dict) -> list[dict]:
    params = {
        'dataset': 'SENTINEL-1',
        'processingLevel': 'SLC',
        'beamMode': 'IW',
        'polarization': 'VV,VV+VH',
        'flightDirection': frame['properties']['dir'],
        'relativeOrbit': frame['properties']['path'],
        'intersectsWith': get_polygon(frame),
        'output': 'jsonlite2',
    }
    response = requests.get('https://api-prod-private.asf.alaska.edu/services/search/param', params=params)
    response.raise_for_status()
    return response.json()['results']


def group_granules(granules: list[dict]) -> list[dict]:
    groups = defaultdict(list)
    for granule in granules:
        group_id = granule['d'] + '_' + granule['o'][0]
        groups[group_id].append(granule)
    return [
        {
            'date': min(datetime.fromisoformat(g['st']) for g in group),
            'granules': [g['gn'] for g in group],
        }
        for group in groups.values()
    ]


def get_stack_for_frame(frame_id: int) -> list[dict]:
    frame = get_frame_by_id(frame_id)
    granules = get_granules_for_frame(frame)
    groups = group_granules(granules)
    groups.sort(key=lambda x: x['date'])
    return groups
