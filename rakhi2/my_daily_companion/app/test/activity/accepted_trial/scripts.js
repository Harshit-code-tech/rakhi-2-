let currentVisibleBox = 'year-box'; // Track the currently visible box
let selectedYear = null; // Track selected year
let selectedMonth = null; // Track selected month

function initChart(id, options) {
    const chart = echarts.init(document.getElementById(id));
    chart.setOption(options);
    return chart;
}

function resizeCharts() {
    document.querySelectorAll('.chart-container').forEach(container => {
        const chart = echarts.getInstanceByDom(container);
        if (chart) {
            chart.resize(); // Resize the chart to fit the container
        }
    });
}

function updateMonthChart(year) {
    selectedYear = year;
    const months = generateMonths();
    const data = months.map(() => Math.floor(Math.random() * 100)); // Random data for example

    const monthOption = {
        title: { text: `Monthly Contribution for ${selectedYear}`, left: 'center' },
        xAxis: {
            type: 'category',
            data: months,
            axisLabel: {
                rotate: 45, // Tilt the labels
            }
        },
        yAxis: { type: 'value' },
        series: [{ data, type: 'bar' }],
        tooltip: { trigger: 'axis' }
    };
    initChart('month-chart', monthOption);
}

function updateDayChart(month) {
    selectedMonth = month;
    const days = Array.from({ length: 30 }, (_, i) => `Day ${i + 1}`); // Example for a month
    const data = generateRandomData(days.length);

    const dayOption = {
        title: { text: `Daily Activity for ${selectedMonth} (${selectedYear})`, left: 'center' },
        xAxis: {
            type: 'category',
            data: days,
            axisLabel: {
                rotate: 45, // Tilt the labels if necessary
            }
        },
        yAxis: { type: 'value' },
        series: [{ data, type: 'line' }],
        tooltip: { trigger: 'axis' }
    };
    initChart('day-chart', dayOption);
}

function showMonthBox() {
    document.getElementById('loading').style.display = 'block';
    setTimeout(() => { // Simulate loading time
        document.getElementById('year-box').classList.remove('show');
        document.getElementById('month-box').style.display = 'block';
        document.getElementById('month-box').classList.add('show');
        document.getElementById('day-box').style.display = 'none';
        document.getElementById('day-box').classList.remove('show');
        updateMonthChart(selectedYear || 'Year 2022'); // Example year
        currentVisibleBox = 'month-box'; // Update the visible box tracker
        document.getElementById('loading').style.display = 'none';
        resizeCharts(); // Resize charts when expanding the month box
    }, 500);
}

function showDayBox() {
    document.getElementById('loading').style.display = 'block';
    setTimeout(() => { // Simulate loading time
        document.getElementById('month-box').classList.remove('show');
        document.getElementById('day-box').style.display = 'block';
        document.getElementById('day-box').classList.add('show');
        currentVisibleBox = 'day-box'; // Update the visible box tracker
        updateDayChart(selectedMonth || 'Month 1'); // Example month
        document.getElementById('loading').style.display = 'none';
        resizeCharts(); // Resize charts when expanding the day box
    }, 500);
}

function generateRandomData(length) {
    return Array.from({ length }, () => Math.floor(Math.random() * 100));
}

function generateMonths() {
    return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
}

function generateYears(startYear, numYears) {
    return Array.from({ length: numYears }, (_, i) => `Year ${startYear + i}`);
}

const years = generateYears(2022, 3); // 3 years from 2022

const yearOption = {
    title: { text: 'Yearly Contribution', left: 'center' },
    xAxis: { type: 'category', data: years },
    yAxis: { type: 'value' },
    series: [{ data: years.map(() => Math.floor(Math.random() * 1000)), type: 'bar' }],
    tooltip: { trigger: 'axis' }
};
initChart('year-chart', yearOption);

document.getElementById('year-box').classList.add('show');
resizeCharts(); // Ensure charts are sized correctly on initial load

// Event handling for chart clicks
document.getElementById('year-chart').addEventListener('click', function () {
    showMonthBox();
});

document.getElementById('month-chart').addEventListener('click', function () {
    showDayBox();
});

// Click handler for document to manage box visibility
document.addEventListener('click', function (event) {
    if (!event.target.closest('.chart-box')) {
        if (currentVisibleBox === 'month-box') {
            document.getElementById('month-box').classList.remove('show');
            document.getElementById('month-box').style.display = 'none';
            document.getElementById('year-box').classList.add('show');
            currentVisibleBox = 'year-box';
        } else if (currentVisibleBox === 'day-box') {
            document.getElementById('day-box').classList.remove('show');
            document.getElementById('day-box').style.display = 'none';
            document.getElementById('month-box').classList.add('show');
            currentVisibleBox = 'month-box';
        }
    }
});
