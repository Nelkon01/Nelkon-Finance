$(document).ready(function () {
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true
    });


});
//
// // Wait for the DOM to fully load before executing the script
// var budgetExpensesData = JSON.parse(document.getElementById('budgetExpensesPieChart').getAttribute('data-expenses'))['Budget Expenses by Category'];
//
// var categoryNames = budgetExpensesData.map(function(item){
//     return item.category_name;
// })
//
// var categorySums = budgetExpensesData.map(function(item){
//     return item.budget_amount;
// })
//
// var pieData = [{
//     values: categorySums,
//     labels: categoryNames,
//     type: 'pie'
// }];
//
// var pieLayout = {
//     height: 400,
//     width: 500
// };
//
// Plotly.newPlot('budgetExpensesPieChart', pieData, pieLayout);

const barChart = document.getElementById('barChart');

new Chart(barChart, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
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
