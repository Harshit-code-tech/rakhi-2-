document.addEventListener("DOMContentLoaded", function() {
    let moodData;
    try {
        // Parse the mood data from the template
        moodData = JSON.parse(document.getElementById('moodData').textContent);
        console.log('Parsed moodData:', moodData); // Debugging: check the parsed data
    } catch (e) {
        console.error('Error parsing JSON data:', e);
        return;
    }

    // Get the canvas context for the chart
    var ctxLine = document.getElementById('moodTimelineChart').getContext('2d');

    if (!ctxLine || !moodData.dates || !moodData.dates.length) {
        console.error('No data available or canvas not found.');
        return;
    }

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
