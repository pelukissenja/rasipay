document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById('userChart').getContext('2d');
    var userChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
            datasets: [{
                label: 'Pengguna Baru',
                data: [10, 20, 30, 40, 50, 60],
                backgroundColor: '#3498DB'
            }]
        },
        options: {
            responsive: false,
            maintainAspectRatio: false
        }
    });
});
