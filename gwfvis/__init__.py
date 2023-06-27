import base64
import json

_APP_BASE_URL = 'https://gwf-vis.usask.ca/app'
_DEFAULT_PLUGIN_PATH = 'https://gwf-vis.usask.ca/plugins/default'

def create_config(with_recommandations: bool = False):
    return {
        "imports": {
            "gwf-default.sqlite-local-data-provider": f"{_DEFAULT_PLUGIN_PATH}/sqlite-local-data-provider.plugin.js",
            "gwf-default.gwfvisdb-data-provider": f"{_DEFAULT_PLUGIN_PATH}/gwfvisdb-data-provider.plugin.js",
            "gwf-default.test-data-fetcher": f"{_DEFAULT_PLUGIN_PATH}/test-data-fetcher.plugin.js",
            "gwf-default.tile-layer": f"{_DEFAULT_PLUGIN_PATH}/tile-layer.plugin.js",
            "gwf-default.geojson-layer": f"{_DEFAULT_PLUGIN_PATH}/geojson-layer.plugin.js",
            "gwf-default.legend": f"{_DEFAULT_PLUGIN_PATH}/legend.plugin.js",
            "gwf-default.data-control": f"{_DEFAULT_PLUGIN_PATH}/data-control.plugin.js",
            "gwf-default.metadata": f"{_DEFAULT_PLUGIN_PATH}/metadata.plugin.js"
        },
        "plugins": [
            {
                "import": "gwf-default.tile-layer",
                "container": "",
                "props": {
                    "displayName": "World_Imagery",
                    "active": True,
                    "urlTemplate": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                    "options": {
                    "attribution": "Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community"
                    }
                }
            }
        ]
    } if with_recommandations else {
        'imports': {},
        'plugins': []
    }

def set_prefer_canvas(config, value: bool = True):
    config['preferCanvas'] = value

def set_view(config, center: [float, float], zoom: int):
    config['view'] = {
        'center': center,
        'zoom': zoom
    }

def import_plugin(config, name: str, url: str):
    config['imports'][name] = url

def add_plugin(config, name: str, container: str = '', props = {}):
    plugin = {
        'import': name,
        'container': container,
        'props': props
    } 
    config['plugins'].append(plugin)
    return plugin

def generate_vis_url(config):
    json_str = json.dumps(config)
    url = f'{_APP_BASE_URL}?configUrl={_make_data_url(json_str)}'
    return url

def _make_data_url(content):
    prefix = 'data:application/json;base64,'
    data_url = prefix + base64.b64encode(content.encode()).decode()
    return data_url