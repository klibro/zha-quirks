"""tuya _TZ3000_tgddllx4 TS0001 On/Off In-line Switches with metering support."""

from zigpy.profiles import zgp, zha
from zigpy.zcl.clusters.general import (
    Basic,
    Identify,
    Groups,
    Scenes,
    OnOff,
)

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODEL,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import (
    EnchantedDevice,
    TuyaZBElectricalMeasurement,
    TuyaZBMeteringCluster,
    TuyaZBOnOffAttributeCluster,
    TuyaZBExternalSwitchTypeCluster,
)


class Tuya_1G_Wall_Switch_Metering(EnchantedDevice):
    """Tuya 1 gang wall switch with metering support."""

    signature = {
#        MODELS_INFO: [
#            ("_TZ3000_tgddllx4", "TS0001"),
#        ],
        MODEL: "TS0001",
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    TuyaZBMeteringCluster.cluster_id,
                    TuyaZBElectricalMeasurement.cluster_id,
                    TuyaZBExternalSwitchTypeCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaZBOnOffAttributeCluster,
                    TuyaZBMeteringCluster,
                    TuyaZBElectricalMeasurement,
                    TuyaZBExternalSwitchTypeCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
        },
    }