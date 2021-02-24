from homeassistant.const import (
    CONF_HOST,
    CONF_MONITORED_CONDITIONS,
    CONF_PASSWORD,
    ENERGY_WATT_HOUR,
    ENERGY_KILO_WATT_HOUR,
    MASS_GRAMS,
    FREQUENCY_HERTZ,
    ELECTRICAL_CURRENT_AMPERE,
    VOLT,
    PERCENTAGE,
    POWER_WATT,
)

CONF_DCINPUTS = "dc_inputs"
CONF_DCINPUTS_DEFAULT = 2

SENSOR_TYPES = {
    "BatteryPercent": [
        "devices:local:battery",
        "SoC",
        "Kostal Battery State of Charge",
        PERCENTAGE,
        "mdi:battery-high",
    ],
    "BatteryCycles": [
        "devices:local:battery",
        "Cycles",
        "Kostal Battery Cycles",
        None,
        "mdi:recycle",
    ],
    "BatteryPower": [
        "devices:local:battery",
        "P",
        "Kostal Battery Power",
        POWER_WATT,
        "mdi:recycle",
    ],
    "HomeOwnPower": [
        "devices:local",
        "Home_P",
        "Kostal Home Power",
        POWER_WATT,
        "mdi:home",
    ],
    "HomePVPower": [
        "devices:local",
        "HomePv_P",
        "Kostal Home Power from PV",
        POWER_WATT,
        "mdi:solar-power",
    ],
    "HomeBatteryPower": [
        "devices:local",
        "HomeBat_P",
        "Kostal Home Power from Battery",
        POWER_WATT,
        "mdi:battery-charging-90",
    ],
    "HomeGridPower": [
        "devices:local",
        "HomeGrid_P",
        "Kostal Home Power from Grid",
        POWER_WATT,
        "mdi:transmission-tower",
    ],
    "GridPower": [
        "devices:local",
        "Grid_P",
        "Kostal Power Grid",
        POWER_WATT,
        "mdi:transmission-tower",
    ],
    "PV1Power": [
        "devices:local:pv1",
        "P",
        "Kostal PV1 Power",
        POWER_WATT,
        "mdi:solar-power",
    ],
    "PV1Voltage": [
        "devices:local:pv1",
        "U",
        "Kostal PV1 Voltage",
        VOLT,
        "mdi:solar-power",
    ],
    "PV1Current": [
        "devices:local:pv1",
        "I",
        "Kostal PV1 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:solar-power",
    ],
    "PVPower": [
        "pvcombined",
        "P",
        "Kostal PV Power",
        POWER_WATT,
        "mdi:solar-power"
    ],
    "DCPower": [
        "devices:local",
        "Dc_P",
        "Kostal DC Power",
        POWER_WATT,
        "mdi:power-cycle",
    ],
    "AutarkyDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:Autarky:Day",
        "Kostal Autarky Day",
        PERCENTAGE,
        "mdi:power-plug",
    ],
    "AutarkyMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:Autarky:Month",
        "Kostal Autarky Month",
        PERCENTAGE,
        "mdi:power-plug",
    ],
    "AutarkyTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:Autarky:Total",
        "Kostal Autarky Total",
        PERCENTAGE,
        "mdi:power-plug",
    ],
    "AutarkyYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:Autarky:Year",
        "Kostal Autarky Year",
        PERCENTAGE,
        "mdi:power-plug",
    ],
    "HomeConsumptionDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHome:Day",
        "Kostal Home Consumption Day",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHome:Month",
        "Kostal Home Consumption Month",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHome:Total",
        "Kostal Home Consumption Total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHome:Year",
        "Kostal Home Consumption Year",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromBatDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeBat:Day",
        "Kostal Home Consumption from Battery Day",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromBatMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeBat:Month",
        "Kostal Home Consumption from Battery Month",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromBatTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeBat:Total",
        "Kostal Home Consumption from Battery Total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromBatYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeBat:Year",
        "Kostal Home Consumption from Battery Year",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromGridDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeGrid:Day",
        "Kostal Home Consumption from Grid Day",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromGridMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeGrid:Month",
        "Kostal Home Consumption from Grid Month",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromGridTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeGrid:Total",
        "Kostal Home Consumption from Grid Total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromGridYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomeGrid:Year",
        "Kostal Home Consumption from Grid Year",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromPVDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomePv:Day",
        "Kostal Home Consumption from PV Day",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromPVMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomePv:Month",
        "Kostal Home Consumption from PV Month",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromPVTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomePv:Total",
        "Kostal Home Consumption from PV Total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionFromPVYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:EnergyHomePv:Year",
        "Kostal Home Consumption from PV Year",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionYieldDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:Yield:Day",
        "Kostal Yield Day",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionYieldMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:Yield:Month",
        "Kostal Yield Month",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionYieldTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:Yield:Total",
        "Kostal Yield Total",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "HomeConsumptionYieldYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:Yield:Year",
        "Kostal Yield Year",
        ENERGY_KILO_WATT_HOUR,
        "mdi:power-plug",
    ],
    "CO2SavingDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:CO2Saving:Day",
        "Kostal CO2 Saving Day",
        MASS_GRAMS,
        "mdi:molecule-co2",
    ],
    "CO2SavingMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:CO2Saving:Month",
        "Kostal CO2 Saving Month",
        MASS_GRAMS,
        "mdi:molecule-co2",
    ],
    "CO2SavingTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:CO2Saving:Total",
        "Kostal CO2 Saving Total",
        MASS_GRAMS,
        "mdi:molecule-co2",
    ],
    "CO2SavingYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:CO2Saving:Year",
        "Kostal CO2 Saving Year",
        MASS_GRAMS,
        "mdi:molecule-co2",
    ],
    "ACFrequency": [
        "devices:local:ac",
        "Frequency",
        "Kostal Frequency",
        FREQUENCY_HERTZ,
        "mdi:power-plug",
    ],
    "ACL1Current": [
        "devices:local:ac",
        "L1_I",
        "Kostal L1 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:power-plug",
    ],
    "ACL1Power": [
        "devices:local:ac",
        "L1_P",
        "Kostal L1 Power",
        POWER_WATT,
        "mdi:power-plug",
    ],
    "ACL1Voltage": [
        "devices:local:ac",
        "L1_U",
        "Kostal L1 Voltage",
        VOLT,
        "mdi:power-plug",
    ],
    "ACL2Current": [
        "devices:local:ac",
        "L2_I",
        "Kostal L2 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:power-plug",
    ],
    "ACL2Power": [
        "devices:local:ac",
        "L2_P",
        "Kostal L2 Power",
        POWER_WATT,
        "mdi:power-plug",
    ],
    "ACL2Voltage": [
        "devices:local:ac",
        "L2_U",
        "Kostal L2 Voltage",
        VOLT,
        "mdi:power-plug",
    ],
    "ACL3Current": [
        "devices:local:ac",
        "L3_I",
        "Kostal L3 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:power-plug",
    ],
    "ACL3Power": [
        "devices:local:ac",
        "L3_P",
        "Kostal L3 Power",
        POWER_WATT,
        "mdi:power-plug",
    ],
    "ACL3Voltage": [
        "devices:local:ac",
        "L3_U",
        "Kostal L3 Voltage",
        VOLT,
        "mdi:power-plug",
    ],
    "OwnConsumptionRateDay": [
        "scb:statistic:EnergyFlow",
        "Statistic:OwnConsumptionRate:Day",
        "Kostal Own Consumption Rate Day",
        PERCENTAGE,
        "mdi:percent",
    ],
    "OwnConsumptionRateMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:OwnConsumptionRate:Month",
        "Kostal Own Consumption Rate Month",
        PERCENTAGE,
        "mdi:percent",
    ],
    "OwnConsumptionRateMonth": [
        "scb:statistic:EnergyFlow",
        "Statistic:OwnConsumptionRate:Month",
        "Kostal Own Consumption Rate Month",
        PERCENTAGE,
        "mdi:percent",
    ],
    "OwnConsumptionRateTotal": [
        "scb:statistic:EnergyFlow",
        "Statistic:OwnConsumptionRate:Total",
        "Kostal Own Consumption Rate Total",
        PERCENTAGE,
        "mdi:percent",
    ],
    "OwnConsumptionRateYear": [
        "scb:statistic:EnergyFlow",
        "Statistic:OwnConsumptionRate:Year",
        "Kostal Own Consumption Rate Year",
        PERCENTAGE,
        "mdi:percent",
    ],
    "MinSoC": [
        "devices:local",
        "Battery:MinSoc",
        "Kostal Min State of Charge",
        PERCENTAGE,
        "mdi:percent",
    ],
    "SmartBatteryControl": [
        "devices:local",
        "Battery:SmartBatteryControl:Enable",
        "Kostal Smart Battery Control Enable",
        None,
        "mdi:lock-smart",
    ],
    "LimitEvuAbs": [
        "devices:local",
        "LimitEvuAbs",
        "Kostal LimitEvuAbs",
        POWER_WATT,
        "mdi:lock-smart",
    ],
    "InverterState": [
        "devices:local",
        "Inverter:State",
        "Kostal Inverter State",
        None,
        "mdi:solar-panel",
    ],
}

SENSORS_DC3 = {
    "PV3Power": [
        "devices:local:pv3",
        "P",
        "Kostal PV3 Power",
        POWER_WATT,
        "mdi:solar-power",
    ],
    "PV3Voltage": [
        "devices:local:pv3",
        "U",
        "Kostal PV3 Voltage",
        VOLT,
        "mdi:solar-power",
    ],
    "PV3Current": [
        "devices:local:pv3",
        "I",
        "Kostal PV3 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:solar-power",
    ]
}

SENSORS_DC2 = {
    "PV2Power": [
        "devices:local:pv2",
        "P",
        "Kostal PV2 Power",
        POWER_WATT,
        "mdi:solar-power",
    ],
    "PV2Voltage": [
        "devices:local:pv2",
        "U",
        "Kostal PV2 Voltage",
        VOLT,
        "mdi:solar-power",
    ],
    "PV2Current": [
        "devices:local:pv2",
        "I",
        "Kostal PV2 Current",
        ELECTRICAL_CURRENT_AMPERE,
        "mdi:solar-power",
    ]
}
