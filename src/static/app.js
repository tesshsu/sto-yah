document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            const stockList = document.getElementById('stock-list');
            for (const [company, info] of Object.entries(data)) {
                const stockCard = document.createElement('div');
                stockCard.className = 'stock-card';

                // Create a unique ID for the canvas
                const canvasId = `chart-${company.replace(/\s+/g, '-')}`;

                // Determine the class for percentage change (positive/negative)
                const percentClass = info.percent_change >= 0 ? 'positive' : 'negative';
                const percentSign = info.percent_change >= 0 ? '+' : '';

                stockCard.innerHTML = `
                    <h3>${company}</h3>
                    <p class="price">$${info.current_price}</p>
                    <p class="percent-change ${percentClass}">${percentSign}${info.percent_change}%</p>
                    <canvas id="${canvasId}" height="60"></canvas>
                `;
                stockList.appendChild(stockCard);

                // Create the sparkline chart
                const ctx = document.getElementById(canvasId).getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: info.price_history.map((_, index) => index), // Simple index for x-axis
                        datasets: [{
                            data: info.price_history,
                            borderColor: info.percent_change >= 0 ? '#2ecc71' : '#e74c3c',
                            borderWidth: 2,
                            fill: false,
                            pointRadius: 0, // No points on the line
                            tension: 0.1 // Slight curve
                        }]
                    },
                    options: {
                        plugins: {
                            legend: { display: false }, // Hide legend
                            tooltip: { enabled: false } // Disable tooltips
                        },
                        scales: {
                            x: { display: false }, // Hide x-axis
                            y: { display: false }  // Hide y-axis
                        }
                    }
                });
            }
        })
        .catch(error => {
            console.error('Error fetching stock prices:', error);
            document.getElementById('stock-list').innerHTML = '<p>Error loading stock prices.</p>';
        });
});

function renderStocks() {
    const stockList = document.getElementById('stock-list');
    stockList.innerHTML = '<p>Loading...</p>';
    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            stockList.innerHTML = '';
            for (const [company, info] of Object.entries(data)) {
                const stockCard = document.createElement('div');
                stockCard.className = 'stock-card';
                const canvasId = `chart-${company.replace(/\s+/g, '-')}`;
                const percentClass = info.percent_change >= 0 ? 'positive' : 'negative';
                const percentSign = info.percent_change >= 0 ? '+' : '';
                stockCard.innerHTML = `
                    <h3>${company}</h3>
                    <p class="price">$${info.current_price}</p>
                    <p class="percent-change ${percentClass}">${percentSign}${info.percent_change}%</p>
                    <canvas id="${canvasId}" height="60"></canvas>
                `;
                stockList.appendChild(stockCard);
                const ctx = document.getElementById(canvasId).getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: info.price_history.map((_, index) => index),
                        datasets: [{
                            data: info.price_history,
                            borderColor: info.percent_change >= 0 ? '#2ecc71' : '#e74c3c',
                            borderWidth: 2,
                            fill: false,
                            pointRadius: 0,
                            tension: 0.1
                        }]
                    },
                    options: {
                        plugins: {
                            legend: { display: false },
                            tooltip: { enabled: false }
                        },
                        scales: {
                            x: { display: false },
                            y: { display: false }
                        }
                    }
                });
            }
        })
        .catch(error => {
            console.error('Error fetching stock prices:', error);
            stockList.innerHTML = '<p>Error loading stock prices.</p>';
        });
}

document.addEventListener('DOMContentLoaded', renderStocks);