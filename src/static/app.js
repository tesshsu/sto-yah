document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            const stockList = document.getElementById('stock-list');
            for (const [company, price] of Object.entries(data)) {
                const stockCard = document.createElement('div');
                stockCard.className = 'stock-card';
                stockCard.innerHTML = `
                    <h3>${company}</h3>
                    <p>$${price}</p>
                `;
                stockList.appendChild(stockCard);
            }
        })
        .catch(error => {
            console.error('Error fetching stock prices:', error);
            const stockList = document.getElementById('stock-list');
            stockList.innerHTML = '<p>Error loading stock prices.</p>';
        });
});

function refreshStocks() {
    document.getElementById('stock-list').innerHTML = '';
    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            const stockList = document.getElementById('stock-list');
            for (const [company, price] of Object.entries(data)) {
                const stockCard = document.createElement('div');
                stockCard.className = 'stock-card';
                stockCard.innerHTML = `
                    <h3>${company}</h3>
                    <p>$${price}</p>
                `;
                stockList.appendChild(stockCard);
            }
        })
        .catch(error => {
            console.error('Error fetching stock prices:', error);
            document.getElementById('stock-list').innerHTML = '<p>Error loading stock prices.</p>';
        });
}

document.addEventListener('DOMContentLoaded', refreshStocks);