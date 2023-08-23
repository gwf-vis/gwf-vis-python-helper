import base64
import json
from strenum import StrEnum


class PluginNames(StrEnum):
    SQLITE_LOCAL_DATA_PROVIDER = "gwf-default.sqlite-local-data-provider"
    GWFVISDB_DATA_PROVIDER = "gwf-default.gwfvisdb-data-provider"
    TEST_DATA_FETCHER = "gwf-default.test-data-fetcher"
    TILE_LAYER = "gwf-default.tile-layer"
    GEOJSON_LAYER = "gwf-default.geojson-layer"
    LEGEND = "gwf-default.legend"
    DATA_CONTROL = "gwf-default.data-control"
    METADATA = "gwf-default.metadata"
    MARKDOWN = "gwf-default.markdown"

_DEFAULT_PLUGIN_PATH = "https://gwf-vis.usask.ca/plugins/default"
_RECOMMENDED_PLUGIN_IMPORTS = {
    PluginNames.SQLITE_LOCAL_DATA_PROVIDER: f"{_DEFAULT_PLUGIN_PATH}/sqlite-local-data-provider.plugin.js",
    PluginNames.GWFVISDB_DATA_PROVIDER: f"{_DEFAULT_PLUGIN_PATH}/gwfvisdb-data-provider.plugin.js",
    PluginNames.TEST_DATA_FETCHER: f"{_DEFAULT_PLUGIN_PATH}/test-data-fetcher.plugin.js",
    PluginNames.TILE_LAYER: f"{_DEFAULT_PLUGIN_PATH}/tile-layer.plugin.js",
    PluginNames.GEOJSON_LAYER: f"{_DEFAULT_PLUGIN_PATH}/geojson-layer.plugin.js",
    PluginNames.LEGEND: f"{_DEFAULT_PLUGIN_PATH}/legend.plugin.js",
    PluginNames.DATA_CONTROL: f"{_DEFAULT_PLUGIN_PATH}/data-control.plugin.js",
    PluginNames.METADATA: f"{_DEFAULT_PLUGIN_PATH}/metadata.plugin.js",
    PluginNames.MARKDOWN: f"{_DEFAULT_PLUGIN_PATH}/markdown.plugin.js",
}
_CONFIG = {
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


def create_config():
    return _CONFIG
