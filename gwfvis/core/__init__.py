import base64
import json

_APP_BASE_URL = "https://gwf-vis.usask.ca/app"
_EMPTY_CONFIG = {"imports": {}, "plugins": []}


def create_config():
    return _EMPTY_CONFIG


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
