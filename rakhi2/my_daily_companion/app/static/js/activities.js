document.addEventListener('DOMContentLoaded', function () {
    console.log('JS loaded successfully');

    function safeParse(scriptId) {
        const dataElement = document.getElementById(scriptId);
        console.log('Parsing data for:', scriptId);
        if (dataElement) {
            try {
                const parsedData = JSON.parse(dataElement.textContent);
                console.log('Parsed data:', parsedData);
                return parsedData;
            } catch (e) {
                console.error('Error parsing JSON from script ID:', scriptId, e);
                return [];
            }
        } else {
            console.error('No script element found for ID:', scriptId);
            return [];
        }
    }

    function initializeHeatmap(elementId, data) {
        const chart = echarts.init(document.getElementById(elementId));
        const option = {
            tooltip: {
                position: 'top',
                formatter: function (params) {
                    return params.value[0] + ': ' + params.value[1];
                }
            },
            visualMap: {
                min: 0,
                max: 35,
                inRange: {
                    color: ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#084594']
                },
                top: '35%'
            },
            calendar: {
                range: new Date().getFullYear(),
                cellSize: [20, 'auto'],
                orient: 'horizontal'
            },
            series: [{
                type: 'heatmap',
                coordinateSystem: 'calendar',
                data: data.map(item => [item.date_only, item.activity_count])
            }]
        };
        chart.setOption(option);
    }

    function initializePieChart(elementId, data) {
        const chart = echarts.init(document.getElementById(elementId));
        const option = {
            series: [{
                type: 'pie',
                data: data.map(item => ({ name: item.date_only, value: item.count })),
            }]
        };
        chart.setOption(option);
    }

    initializeHeatmap('calendar-heatmap', safeParse('calendar-heatmap-data'));
    initializePieChart('mood-tracker-pie', safeParse('mood-tracker-data'));
    initializePieChart('journal-pie', safeParse('journal-data'));
    initializePieChart('reward-pie', safeParse('reward-data'));
    initializePieChart('note-pie', safeParse('note-data'));
});
