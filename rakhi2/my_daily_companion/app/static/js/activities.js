document.addEventListener('DOMContentLoaded', function () {
    // Safe parsing of JSON data with a fallback to an empty array
    function safeParse(data) {
        try {
            return JSON.parse(data);
        } catch (e) {
            console.error('Error parsing JSON:', e);
            return [];
        }
    }

    // Calendar Heatmap
    var calendarHeatmapData = safeParse('{{ calendar_heatmap_data|escapejs }}');
    var heatmapChart = echarts.init(document.getElementById('calendar-heatmap'));
    var heatmapOption = {
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
            data: calendarHeatmapData.map(item => [item.date, item.activity_count])
        }]
    };
    heatmapChart.setOption(heatmapOption);

    // Mood Tracker Pie
    var moodTrackerData = safeParse('{{ mood_tracker_data|escapejs }}');
    var moodTrackerPie = echarts.init(document.getElementById('mood-tracker-pie'));
    var moodTrackerOption = {
        series: [{
            type: 'pie',
            data: moodTrackerData.map(item => ({ name: item.date, value: item.count })),
        }]
    };
    moodTrackerPie.setOption(moodTrackerOption);

    // Journal Pie
    var journalData = safeParse('{{ journal_data|escapejs }}');
    var journalPie = echarts.init(document.getElementById('journal-pie'));
    var journalOption = {
        series: [{
            type: 'pie',
            data: journalData.map(item => ({ name: item.date, value: item.count })),
        }]
    };
    journalPie.setOption(journalOption);

    // Reward Pie
    var rewardData = safeParse('{{ reward_data|escapejs }}');
    var rewardPie = echarts.init(document.getElementById('reward-pie'));
    var rewardOption = {
        series: [{
            type: 'pie',
            data: rewardData.map(item => ({ name: item.date, value: item.count })),
        }]
    };
    rewardPie.setOption(rewardOption);

    // Note Pie
    var noteData = safeParse('{{ note_data|escapejs }}');
    var notePie = echarts.init(document.getElementById('note-pie'));
    var noteOption = {
        series: [{
            type: 'pie',
            data: noteData.map(item => ({ name: item.date, value: item.count })),
        }]
    };
    notePie.setOption(noteOption);
});
