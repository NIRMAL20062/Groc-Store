async function search() {
    const product = document.getElementById("product").value;
    const response = await fetch(`/search?product=${encodeURIComponent(product)}`);
    const data = await response.json();

    // Display prices
    document.getElementById("amazon-price").innerText = `Amazon: $${data.prices.amazon}`;
    document.getElementById("ebay-price").innerText = `eBay: $${data.prices.ebay}`;

    // Draw price history chart
    const ctx = document.getElementById("priceChart").getContext("2d");
    new Chart(ctx, {
        type: "line",
        data: {
            labels: data.history.dates,
            datasets: [
                {
                    label: "Amazon",
                    data: data.history.prices.amazon,
                    borderColor: "#FF9900",
                    fill: false
                },
                {
                    label: "eBay",
                    data: data.history.prices.ebay,
                    borderColor: "#0066CC",
                    fill: false
                }
            ]
        },
        options: {
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}