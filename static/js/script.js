const ctx = document.getElementById('Loss');
const data = {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35'],
    datasets: [{
        label: 'Losses',
        data: [2174.31812, 609.358643, 22.6190357, 2.349473, 2.11710572, 1.91894054, 1.73087537, 1.5582974, 1.40478837, 1.26993871, 1.15075076, 1.04381275, 0.942400098, 0.836814702, 0.722695708, 0.59255749, 0.434774339, 0.251131505, 0.108983561, 0.0427514166, 0.0195923373, 0.0122664059, 0.00920730364, 0.00745935412, 0.00620386284, 0.00520433998, 0.00435827486, 0.00370792765, 0.00321059395, 0.00275137974, 0.00237334846, 0.00203526672, 0.00175132533, 0.00151430862, 0.00129613292],
        fill: false,
        borderColor: 'white',
        tension: 0.2
    }]
};
new Chart(ctx, {
    type: 'line',
    data: data
});

const on_try = function () {
    window.location.href = '/test';
}