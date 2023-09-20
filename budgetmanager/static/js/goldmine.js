





const lineChart = document.getElementById('lineChart');
new Chart(lineChart, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [{
            label: 'Trend of Expenses',
            data: [200, 500, 350, 300, 400, 300],
            fill: false,
            borderColor: 'rgb(255, 255, 255)',
            tension: 0.1
        }]
    }

});

const doughnutChart = document.getElementById('doughnutChart');

new Chart(doughnutChart, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Yellow', 'Blue', 'Purple', 'Green'],
        datasets: [{
            label: 'Expenses by Category',
            data: [10, 20, 30, 15, 10]
        }]
    }
});

// Function to create or update the Doughnut chart for the month