conversion_factor = {
    "weight": {
        "gram": {
            "kilogram": "x / 1000",
            "ton": "x / 1000000",
            "pound": "x / 453.6",
            "ounce": "x / 28.34952"
        },
        "kilogram": {
            "gram": "x * 1000",
            "ton": "x / 1000",
            "pound": "x * 2.20462",
            "ounce": "x * 35.274"
        },
        "ton": {
            "gram": "x * 1000000",
            "kilogram": "x * 1000",
            "pound": "x * 2204.62",
            "ounce": "x * 35274"
        },
        "pound": {
            "gram": "x * 453.6",
            "kilogram": "x / 2.20462",
            "ton": "x / 2204.62",
            "ounce": "x * 16"
        },
        "ounce": {
            "gram": "x * 28.34952",
            "kilogram": "x / 35.274",
            "ton": "x / 35274",
            "pound": "x / 16"
        }
    },
    "length": {
        "millimeter": {
            "centimeter": "x / 10",
            "meter": "x / 1000",
            "kilometer": "x / 1000000",
            "inch": "x / 25.4",
            "foot": "x / 304.8",
            "yard": "x / 914.4",
            "mile": "x / 1609344"
        },
        "centimeter": {
            "millimeter": "x * 10",
            "meter": "x / 100",
            "kilometer": "x / 100000",
            "inch": "x / 2.54",
            "foot": "x / 30.48",
            "yard": "x / 91.44",
            "mile": "x / 160934.4"
        },
        "meter": {
            "millimeter": "x * 1000",
            "centimeter": "x * 100",
            "kilometer": "x / 1000",
            "inch": "x * 39.37",
            "foot": "x * 3.281",
            "yard": "x * 1.094",
            "mile": "x / 1609.344"
        },
        "kilometer": {
            "millimeter": "x * 1000000",
            "centimeter": "x * 100000",
            "meter": "x * 1000",
            "inch": "x * 39370.079",
            "foot": "x * 3280.84",
            "yard": "x * 1093.613",
            "mile": "x / 1.609"
        },
        "inch": {
            "millimeter": "x * 25.4",
            "centimeter": "x * 2.54",
            "meter": "x / 39.37",
            "kilometer": "x / 39370.079",
            "foot": "x / 12",
            "yard": "x / 36",
            "mile": "x / 63360"
        },
        "foot": {
            "millimeter": "x * 304.8",
            "centimeter": "x * 30.48",
            "meter": "x / 3.281",
            "kilometer": "x / 3280.84",
            "inch": "x * 12",
            "yard": "x / 3",
            "mile": "x / 5280"
        },
        "yard": {
            "millimeter": "x * 914.4",
            "centimeter": "x * 91.44",
            "meter": "x / 1.094",
            "kilometer": "x / 1093.613",
            "inch": "x * 36",
            "foot": "x * 3",
            "mile": "x / 1760"
        },
        "mile": {
            "millimeter": "x * 1609344",
            "centimeter": "x * 160934.4",
            "meter": "x * 1609.344",
            "kilometer": "x * 1.609",
            "inch": "x * 63360",
            "foot": "x * 5280",
            "yard": "x * 1760"
        }
    },
    "temperature": {
        "celsius": {
            "fahrenheit": "(x * 9/5) + 32",
            "kelvin": "x + 273.15"
        },
        "fahrenheit": {
            "celsius": "(x - 32) * 5/9",
            "kelvin": "(x + 459.67) * 5/9"
        },
        "kelvin": {
            "celsius": "x - 273.15",
            "fahrenheit": "(x * 9/5) - 459.67"
        }
    },
    "time": {
        "second": {
            "minute": "x / 60",
            "hour": "x / 3600",
            "day": "x / 86400",
            "week": "x / 604800",
            "month": "x / 2592000",
            "year": "x / 31536000"
        },
        "minute": {
            "second": "x * 60",
            "hour": "x / 60",
            "day": "x / 1440",
            "week": "x / 10080",
            "month": "x / 43200",
            "year": "x / 525600"
        },
        "hour": {
            "second": "x * 3600",
            "minute": "x * 60",
            "day": "x / 24",
            "week": "x / 168",
            "month": "x / 720",
            "year": "x / 8760"
        },
        "day": {
            "second": "x * 86400",
            "minute": "x * 1440",
            "hour": "x * 24",
            "week": "x / 7",
            "month": "x / 30.4167",
            "year": "x / 365"
        },
        "week": {
            "second": "x * 604800",
            "minute": "x * 10080",
            "hour": "x * 168",
            "day": "x * 7",
            "month": "x / 4.34524",
            "year": "x / 52.143"
        },
        "month": {
            "second": "x * 2592000",
            "minute": "x * 43200",
            "hour": "x * 720",
            "day": "x * 30.4167",
            "week": "x * 4.34524",
            "year": "x / 12"
        },
        "year": {
            "second": "x * 31536000",
            "minute": "x * 525600",
            "hour": "x * 8760",
            "day": "x * 365",
            "week": "x * 52.143",
            "month": "x * 12"
        }
    },
    "bytes": {
        "bit": {
            "byte": "x / 8",
            "kilobyte": "x / 8000",
            "megabyte": "x / 8000000",
            "gigabyte": "x / 8000000000",
            "terabyte": "x / 8000000000000",
            "petabyte": "x / 8000000000000000"
        },
        "byte": {
            "bit": "x * 8",
            "kilobyte": "x / 1000",
            "megabyte": "x / 1000000",
            "gigabyte": "x / 1000000000",
            "terabyte": "x / 1000000000000",
            "petabyte": "x / 1000000000000000"
        },
        "kilobyte": {
            "bit": "x * 8000",
            "byte": "x * 1000",
            "megabyte": "x / 1000",
            "gigabyte": "x / 1000000",
            "terabyte": "x / 1000000000",
            "petabyte": "x / 1000000000000"
        },
        "megabyte": {
            "bit": "x * 8000000",
            "byte": "x * 1000000",
            "kilobyte": "x * 1000",
            "gigabyte": "x / 1000",
            "terabyte": "x / 1000000",
            "petabyte": "x / 1000000000"
        },
        "gigabyte": {
            "bit": "x * 8000000000",
            "byte": "x * 1000000000",
            "kilobyte": "x * 1000000",
            "megabyte": "x * 1000",
            "terabyte": "x / 1000",
            "petabyte": "x / 1000000"
        },
        "terabyte": {
            "bit": "x * 8000000000000",
            "byte": "x * 1000000000000",
            "kilobyte": "x * 1000000000",
            "megabyte": "x * 1000000",
            "gigabyte": "x * 1000",
            "petabyte": "x / 1000"
        },
        "petabyte": {
            "bit": "x * 8000000000000000",
            "byte": "x * 1000000000000000",
            "kilobyte": "x * 1000000000000",
            "megabyte": "x * 1000000000",
            "gigabyte": "x * 1000000",
            "terabyte": "x * 1000"
        }
    },
    "speed": {
        "meter/second": {
            "kilometer/hour": "x * 3.6",
            "mile/hour": "x * 2.23694"
        },
        "kilometer/hour": {
            "meter/second": "x / 3.6",
            "mile/hour": "x / 1.60934"
        },
        "mile/hour": {
            "meter/second": "x / 2.23694",
            "kilometer/hour": "x * 1.60934"
        }
    },
    "volume": {
        "milliliter": {
            "liter": "x / 1000",
            "gallon": "x / 3785.41",
            "cubic inch": "x / 16.3871",
            "cubic foot": "x / 28316.85",
            "cubic meter": "x / 1000000"
        },
        "liter": {
            "milliliter": "x * 1000",
            "gallon": "x / 3.78541",
            "cubic inch": "x * 61.0237",
            "cubic foot": "x / 28.31685",
            "cubic meter": "x / 1000"
        },
        "gallon": {
            "milliliter": "x * 3785.41",
            "liter": "x * 3.78541",
            "cubic inch": "x * 231",
            "cubic foot": "x / 7.48052",
            "cubic meter": "x / 264.172"
        },
        "cubic inch": {
            "milliliter": "x * 16.3871",
            "liter": "x / 61.0237",
            "gallon": "x / 231",
            "cubic foot": "x / 1728",
            "cubic meter": "x / 61023.7"
        },
        "cubic foot": {
            "milliliter": "x * 28316.85",
            "liter": "x * 28.31685",
            "gallon": "x * 7.48052",
            "cubic inch": "x * 1728",
            "cubic meter": "x / 35.3147"
        },
        "cubic meter": {
            "milliliter": "x * 1000000",
            "liter": "x * 1000",
            "gallon": "x * 264.172",
            "cubic inch": "x * 61023.7",
            "cubic foot": "x * 35.3147"
        }
    },
    "area": {
        "sq. meter": {
            "sq. kilometer": "x / 1000000",
            "sq. mile": "x / 2590000",
            "sq. yard": "x * 1.196",
            "sq. foot": "x * 10.764",
            "acre": "x / 4047",
            "hectare": "x / 10000"
        },
        "sq. kilometer": {
            "sq. meter": "x * 1000000",
            "sq. mile": "x / 2.59",
            "sq. yard": "x * 1196000",
            "sq. foot": "x * 10764000",
            "acre": "x * 247.105",
            "hectare": "x * 100"
        },
        "sq. mile": {
            "sq. meter": "x * 2590000",
            "sq. kilometer": "x * 2.59",
            "sq. yard": "x * 3097600",
            "sq. foot": "x * 27878400",
            "acre": "x * 640",
            "hectare": "x * 258.999"
        },
        "sq. yard": {
            "sq. meter": "x / 1.196",
            "sq. kilometer": "x / 1196000",
            "sq. mile": "x / 3097600",
            "sq. foot": "x * 9",
            "acre": "x / 4840",
            "hectare": "x / 11959.9"
        },
        "sq. foot": {
            "sq. meter": "x / 10.764",
            "sq. kilometer": "x / 10764000",
            "sq. mile": "x / 27878400",
            "sq. yard": "x / 9",
            "acre": "x / 43560",
            "hectare": "x / 107639"
        },
        "acre": {
            "sq. meter": "x * 4047",
            "sq. kilometer": "x / 247.105",
            "sq. mile": "x / 640",
            "sq. yard": "x * 4840",
            "sq. foot": "x * 43560",
            "hectare": "x / 2.471"
        },
        "hectare": {
            "sq. meter": "x * 10000",
            "sq. kilometer": "x / 100",
            "sq. mile": "x / 258.999",
            "sq. yard": "x * 11959.9",
            "sq. foot": "x * 107639",
            "acre": "x * 2.471"
        }
    },
    "energy": {
        "joule": {
            "calorie": "x / 4.184",
            "kilocalorie": "x / 4184",
            "kilowatt hour": "x / 3600000",
            "electron volt": "x / 1.602e-19",
            "BTU": "x / 1055",
            "foot-pound": "x / 1.356"
        },
        "calorie": {
            "joule": "x * 4.184",
            "kilocalorie": "x / 1000",
            "kilowatt hour": "x / 860420",
            "electron volt": "x / 3.829e-20",
            "BTU": "x / 252",
            "foot-pound": "x / 3.086"
        },
        "kilocalorie": {
            "joule": "x * 4184",
            "calorie": "x * 1000",
            "kilowatt hour": "x / 860",
            "electron volt": "x / 2.611e-23",
            "BTU": "x / 2.521",
            "foot-pound": "x / 3086"
        },
        "kilowatt hour": {
            "joule": "x * 3600000",
            "calorie": "x * 860420",
            "kilocalorie": "x * 860",
            "electron volt": "x / 2.246e-22",
            "BTU": "x * 3.412",
            "foot-pound": "x * 2655"
        },
        "electron volt": {
            "joule": "x * 1.602e-19",
            "calorie": "x * 3.829e-20",
            "kilocalorie": "x * 2.611e-23",
            "kilowatt hour": "x * 2.246e-22",
            "BTU": "x * 3.827e-20",
            "foot-pound": "x * 1.181e-19"
        },
        "BTU": {
            "joule": "x * 1055",
            "calorie": "x * 252",
            "kilocalorie": "x * 2.521",
            "kilowatt hour": "x / 3.412",
            "electron volt": "x * 3.827e-20",
            "foot-pound": "x * 778"
        },
        "foot-pound": {
            "joule": "x * 1.356",
            "calorie": "x * 3.086",
            "kilocalorie": "x * 3086",
            "kilowatt hour": "x / 2655",
            "electron volt": "x * 1.181e-19",
            "BTU": "x / 778"
        }
    },
}
