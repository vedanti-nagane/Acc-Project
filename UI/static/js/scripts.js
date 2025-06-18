document.addEventListener("DOMContentLoaded", () => {
    // Chart 1: Pie Chart
    new Chart(document.getElementById("chart1"), {
        type: "pie",
        data: {
            labels: ["Allowed", "Not allowed"],
            datasets: [{
                data: [20, 30],
                backgroundColor: ["green", "blue"]
            }]
        }
    });

    // Chart 2: Bar Chart
    new Chart(document.getElementById("chart2"), {
        type: "bar",
        data: {
            labels: ["Allowed", "Not Allowed"],
            datasets: [{
                label: "Allowed",
                data: [1, 2],
                backgroundColor: ["green", "blue"]
            }]
        }
    });

    // Fetch table data
    fetch("/data")
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("data-table");
            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                <td>${row["Timestamp"]}</td>
                <td>${row["IP Address"]}</td>
                <td>${row["Username"]}</td>
                <td>${row["Process Name"]}</td>
                <td>${row["Permission"]}</td>
                `;
                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});

function exportPDF() {
    const element = document.querySelector("table");
    const opt = {
        margin: 0.5,
        filename: 'report.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
    };

    if (typeof html2pdf !== 'undefined') {
        html2pdf().set(opt).from(element).save();
    } else {
        console.error("html2pdf library not loaded.");
    }
}
