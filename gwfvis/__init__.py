import base64
import json

_APP_BASE_URL = "https://gwf-vis.usask.ca/app"
_DEFAULT_PLUGIN_PATH = "https://gwf-vis.usask.ca/plugins/default"
_RECOMMENDED_PLUGIN_IMPORTS = {
    "gwf-default.sqlite-local-data-provider": f"{_DEFAULT_PLUGIN_PATH}/sqlite-local-data-provider.plugin.js",
    "gwf-default.gwfvisdb-data-provider": f"{_DEFAULT_PLUGIN_PATH}/gwfvisdb-data-provider.plugin.js",
    "gwf-default.test-data-fetcher": f"{_DEFAULT_PLUGIN_PATH}/test-data-fetcher.plugin.js",
    "gwf-default.tile-layer": f"{_DEFAULT_PLUGIN_PATH}/tile-layer.plugin.js",
    "gwf-default.geojson-layer": f"{_DEFAULT_PLUGIN_PATH}/geojson-layer.plugin.js",
    "gwf-default.legend": f"{_DEFAULT_PLUGIN_PATH}/legend.plugin.js",
    "gwf-default.data-control": f"{_DEFAULT_PLUGIN_PATH}/data-control.plugin.js",
    "gwf-default.metadata": f"{_DEFAULT_PLUGIN_PATH}/metadata.plugin.js",
    "gwf-default.markdown": f"{_DEFAULT_PLUGIN_PATH}/markdown.plugin.js",
}
_RECOMMENDED_CONFIG = {
    "imports": _RECOMMENDED_PLUGIN_IMPORTS,
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
                },
            },
        }
    ],
}
_EMPTY_CONFIG = {"imports": {}, "plugins": []}


def create_config():
    return _EMPTY_CONFIG

def create_recommended_config():
    return _RECOMMENDED_CONFIG

def set_prefer_canvas(config, value: bool = True):
    config["preferCanvas"] = value


def set_view(config, center: [float, float], zoom: int):
    config["view"] = {"center": center, "zoom": zoom}


def import_plugin(config, name: str, url: str):
    config["imports"][name] = url


def add_plugin(config, name: str, container: str = "", props={}, container_props={}):
    plugin = {
        "import": name,
        "container": container,
        "props": props,
        "containerProps": container_props,
    }
    config["plugins"].append(plugin)
    return plugin


def set_plugin_container(plugin, container: str = ""):
    plugin["container"] = container


def set_plugin_container_props(plugin, container_props={}):
    plugin["containerProps"] = container_props


def set_plugin_props(plugin, props={}):
    plugin["props"] = props


def generate_vis_url(config):
    json_str = json.dumps(config)
    url = f"{_APP_BASE_URL}?configUrl={_make_data_url(json_str)}"
    return url


def _make_data_url(content):
    prefix = "data:application/json;base64,"
    data_url = prefix + base64.b64encode(content.encode()).decode()
    return data_url
