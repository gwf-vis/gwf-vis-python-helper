import base64
import json

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


def create_recommended_config():
    return _RECOMMENDED_CONFIG
