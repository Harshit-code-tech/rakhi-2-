document.addEventListener("DOMContentLoaded", function () {
    const moodDataElement = document.getElementById('moodData');

    if (!moodDataElement) {
        console.error('No element with id "moodData" found.');
        return;
    }

    const moodDataText = moodDataElement.textContent.trim(); // Ensure no extra whitespace
    console.log('Raw moodDataText:', moodDataText); // Log the raw JSON data

    let moodData;
    try {
        moodData = JSON.parse(moodDataText);
        console.log('Parsed moodData:', moodData);
    } catch (e) {
        console.error('Error parsing JSON data:', e);
        return;
    }

    // Function to initialize ECharts
    const initChart = (id, options) => {
        const chart = echarts.init(document.getElementById(id));
        chart.setOption(options);
        return chart;
    };

    // Pie Chart for Mood Category Distribution
    const categoryOption = {
        title: {
            text: 'Mood Category Distribution',
            left: 'center',
            textStyle: {fontSize: 24, color: '#2c3e50'}
        },
        series: [{
            name: 'Mood Categories',
            type: 'pie',
            radius: '50%',
            data: moodData.category_data.map(item => ({name: item.category, value: item.value})),
            emphasis: {
                itemStyle: {
                    shadowBlur: 20,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.3)'
                }
            },
            itemStyle: {borderRadius: 10},
            tooltip: {formatter: '{b}: {c} ({d}%)'}
        }],
        legend: {
            orient: 'vertical',
            left: 'left',
            data: moodData.category_data.map(item => item.category)
        }
    };

    // Pie Chart for Mood Wheel
    const wheelOption = {
        title: {
            text: 'Mood Wheel',
            left: 'center',
            textStyle: {fontSize: 24, color: '#2c3e50'}
        },
        series: [{
            name: 'Mood Wheel',
            type: 'pie',
            radius: ['40%', '70%'],
            data: moodData.wheel_data.map(item => ({name: item.category, value: item.value})), // Fixed key 'mood' to 'category'
            label: {
                show: true,
                formatter: '{b}: {c} ({d}%)',
                color: '#333'
            },
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }],
        legend: {
            orient: 'vertical',
            right: 'right',
            data: moodData.wheel_data.map(item => item.category) // Fixed key 'mood' to 'category'
        }
    };

    // Mood Timeline Chart
    const colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'];
    const seriesData = Object.keys(moodData.intensity_data).map((mood, index) => ({
        name: mood,
        type: 'line',
        data: moodData.intensity_data[mood].map((value, idx) => [moodData.dates[idx], parseFloat(value)]),
        itemStyle: {color: colors[index % colors.length]},
        smooth: true
    }));

    const timelineOption = {
        title: {
            text: 'Mood Intensity Over Time',
            left: 'center',
            bottom: '5%'
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

    // Initialize all charts
    initChart('category-distribution', categoryOption);
    initChart('mood-wheel', wheelOption);
    initChart('intensity-timeline', timelineOption);
});
