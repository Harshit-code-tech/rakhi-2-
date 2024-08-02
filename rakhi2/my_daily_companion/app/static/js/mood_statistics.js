document.addEventListener("DOMContentLoaded", function() {
    // Parse the mood data from the template
    const moodData = JSON.parse(document.getElementById('moodData').textContent);

    // Get the canvas context for the chart
    var ctxLine = document.getElementById('moodTimelineChart').getContext('2d');
    var datasets = [];
    var colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'];

    // Prepare datasets for each mood type
    Object.keys(moodData.intensity_data).forEach((mood, index) => {
        datasets.push({
            label: mood,
            data: moodData.intensity_data[mood],
            borderColor: colors[index % colors.length],
            fill: false
        });
    });

    // Create the line chart
    var moodTimelineChart = new Chart(ctxLine, {
        type: 'line',
        data: {
            labels: moodData.dates,
            datasets: datasets
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Mood Intensity'
                    }
                }
            }
        }
    });
});
