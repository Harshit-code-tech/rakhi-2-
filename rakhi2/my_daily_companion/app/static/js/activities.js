document.addEventListener('DOMContentLoaded', function () {
    function safeParse(scriptId) {
        const dataElement = document.getElementById(scriptId);
        if (dataElement) {
            try {
                console.log("Parsing data from script ID:", scriptId);
                return JSON.parse(dataElement.textContent);
            } catch (e) {
                console.error('Error parsing JSON from script ID:', scriptId, e);
                return [];
            }
        } else {
            console.error('No script element found for ID:', scriptId);
            return [];
        }
    }

    /**
     * Initialize a heatmap chart.
     * @param {string} elementId - The ID of the DOM element where the chart will be rendered.
     * @param {Array} data - The data to be used in the heatmap.
     */
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
                data: data.map(item => [item.date, item.activity_count])
            }]
        };
        chart.setOption(option);
    }

    /**
     * Initialize a pie chart.
     * @param {string} elementId - The ID of the DOM element where the chart will be rendered.
     * @param {Array} data - The data to be used in the pie chart.
     */
    function initializePieChart(elementId, data) {
        const chart = echarts.init(document.getElementById(elementId));
        const option = {
            series: [{
                type: 'pie',
                data: data.map(item => ({ name: item.date, value: item.count })),
            }]
        };
        chart.setOption(option);
    }

    // Initialize the charts with their respective data
    initializeHeatmap('calendar-heatmap', safeParse('calendar-heatmap-data'));
    initializePieChart('mood-tracker-pie', safeParse('mood-tracker-data'));
    initializePieChart('journal-pie', safeParse('journal-data'));
    initializePieChart('reward-pie', safeParse('reward-data'));
    initializePieChart('note-pie', safeParse('note-data'));
});
