document.addEventListener("DOMContentLoaded", function() {
    let moodDataElement = document.getElementById('moodData');

    if (!moodDataElement) {
        console.error('No element with id "moodData" found.');
        return;
    }

    let moodDataText = moodDataElement.textContent;
    console.log('Raw moodData text:', moodDataText);

    let decodedMoodDataText;
    try {
        // Decode and parse the JSON data
        decodedMoodDataText = decodeURIComponent(JSON.parse('"' + moodDataText.replace(/\"/g, '\\"') + '"'));
        console.log('Decoded moodData text:', decodedMoodDataText);
    } catch (e) {
        console.error('Error decoding JSON data:', e);
        return;
    }

    let moodData;
    try {
        moodData = JSON.parse(decodedMoodDataText);
        console.log('Parsed moodData:', moodData);
    } catch (e) {
        console.error('Error parsing JSON data:', e);
        return;
    }

    // Initialize ECharts instance
    var chart = echarts.init(document.getElementById('moodTimelineChart'));

    var colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'];
    var seriesData = Object.keys(moodData.intensity_data).map((mood, index) => ({
        name: mood,
        type: 'line',
        data: moodData.intensity_data[mood].map((value, idx) => [moodData.dates[idx], parseFloat(value)]), // Ensure value is a float
        itemStyle: { color: colors[index % colors.length] },
        smooth: true
    }));

    var option = {
        title: {
            text: 'Mood Intensity Over Time',
            left: 'center',
            bottom: '5%' // Adjusted for better placement
        },
        tooltip: {
            trigger: 'axis',
            formatter: function (params) {
                var date = params[0].axisValueLabel;
                var tooltip = `${date}<br/>`;
                params.forEach(param => {
                    tooltip += `${param.marker} ${param.seriesName}: ${param.value[1]}<br/>`;
                });
                return tooltip;
            }
        },
        legend: {
            data: Object.keys(moodData.intensity_data),
            selectedMode: 'multiple'
        },
        xAxis: {
            type: 'category',
            data: moodData.dates,
            axisLabel: {
                rotate: 45,
                align: 'right',
                formatter: function (value) {
                    return echarts.format.formatTime('yyyy-MM-dd', new Date(value));
                }
            },
            boundaryGap: false,
            name: 'Date'
        },
        yAxis: {
            type: 'value',
            axisLabel: {
                formatter: '{value}'
            },
            name: 'Mood Intensity'
        },
        series: seriesData
    };

    chart.setOption(option);
});
