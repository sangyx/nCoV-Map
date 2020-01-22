var chart_e245bd46323e4c0d9d2e31b64c18d137 = echarts.init(
    document.getElementById('e245bd46323e4c0d9d2e31b64c18d137'), 'white', {
        renderer: 'canvas'
    });
var option_e245bd46323e4c0d9d2e31b64c18d137 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [{
        "type": "effectScatter",
        "name": "\u75ab\u60c5",
        "coordinateSystem": "geo",
        "showEffectOn": "render",
        "rippleEffect": {
            "show": true,
            "brushType": "stroke",
            "scale": 2.5,
            "period": 4
        },
        "symbolSize": 12,
        "data": [{
                "name": "\u6e56\u5317",
                "value": [
                    114.341861,
                    30.546498,
                    270
                ]
            },
            {
                "name": "\u5317\u4eac",
                "value": [
                    116.407526,
                    39.90403,
                    10
                ]
            },
            {
                "name": "\u5e7f\u4e1c",
                "value": [
                    113.26653,
                    23.132191,
                    17
                ]
            },
            {
                "name": "\u4e0a\u6d77",
                "value": [
                    121.473701,
                    31.230416,
                    6
                ]
            },
            {
                "name": "\u6d59\u6c5f",
                "value": [
                    120.152791,
                    30.267446,
                    5
                ]
            },
            {
                "name": "\u4e91\u5357",
                "value": [
                    102.710002,
                    25.045806,
                    1
                ]
            },
            {
                "name": "\u56db\u5ddd",
                "value": [
                    104.075931,
                    30.651651,
                    1
                ]
            },
            {
                "name": "\u5c71\u4e1c",
                "value": [
                    117.020359,
                    36.66853,
                    1
                ]
            },
            {
                "name": "\u5e7f\u897f",
                "value": [
                    108.327546,
                    22.815478,
                    1
                ]
            },
            {
                "name": "\u8d35\u5dde",
                "value": [
                    106.70741,
                    26.598194,
                    1
                ]
            },
            {
                "name": "\u5b89\u5fbd",
                "value": [
                    117.284922,
                    31.861184,
                    1
                ]
            },
            {
                "name": "\u6d77\u5357",
                "value": [
                    110.349228,
                    20.017377,
                    1
                ]
            },
            {
                "name": "\u5b81\u590f",
                "value": [
                    106.258754,
                    38.471317,
                    1
                ]
            },
            {
                "name": "\u5409\u6797",
                "value": [
                    125.32599,
                    43.896536,
                    1
                ]
            },
            {
                "name": "\u6c5f\u897f",
                "value": [
                    115.909228,
                    28.675696,
                    2
                ]
            },
            {
                "name": "\u5929\u6d25",
                "value": [
                    117.200983,
                    39.084158,
                    2
                ]
            },
            {
                "name": "\u6cb3\u5357",
                "value": [
                    113.753602,
                    34.765515,
                    1
                ]
            },
            {
                "name": "\u91cd\u5e86",
                "value": [
                    106.551556,
                    29.563009,
                    5
                ]
            },
            {
                "name": "\u8fbd\u5b81",
                "value": [
                    123.42944,
                    41.835441,
                    1
                ]
            },
            {
                "name": "\u53f0\u6e7e",
                "value": [
                    121.509062,
                    25.044332,
                    1
                ]
            },
            {
                "name": "\u9999\u6e2f",
                "value": [
                    114.173355,
                    22.320048,
                    117
                ]
            },
            {
                "name": "\u9ed1\u9f99\u6c5f",
                "value": [
                    126.661669,
                    45.742347,
                    1
                ]
            },
            {
                "name": "\u6e56\u5357",
                "value": [
                    112.98381,
                    28.112444,
                    1
                ]
            }
        ],
        "label": {
            "show": false,
            "position": "top",
            "margin": 8
        }
    }],
    "legend": [{
        "data": [
            "\u75ab\u60c5"
        ],
        "selected": {
            "\u75ab\u60c5": true
        },
        "show": true,
        "padding": 5,
        "itemGap": 10,
        "itemWidth": 25,
        "itemHeight": 14
    }],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": function (params) {
            return params.name + ' : ' + params.value[2];
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    // "title": [{
    //     "text": "\u75ab\u60c5\u53ef\u89c6\u5316",
    //     "padding": 5,
    //     "itemGap": 10
    // }],
    "geo": {
        "map": "china",
        "roam": true,
        "emphasis": {}
    }
};
chart_e245bd46323e4c0d9d2e31b64c18d137.setOption(option_e245bd46323e4c0d9d2e31b64c18d137);