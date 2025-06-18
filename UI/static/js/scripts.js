document.addEventListener("DOMContentLoaded", () => {
    fetch("/data")
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("data-table");
            let allowed = 0, notAllowed = 0;

            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${row["Timestamp"]}</td>
                    <td>${row["IP Address"]}</td>
                    <td>${row["Username"]}</td>
                    <td>${row["Process Name"]}</td>
                    <td>${row["Permission"] === "true" ? "Allowed" : row["Permission"] === "false" ? "Not Allowed" : "Invalid"}</td>
                `;
                tbody.appendChild(tr);

                // Count permission types
                if (row["Permission"] === "true") allowed++;
                else if (row["Permission"] === "false") notAllowed++;
            });

            // PIE Chart
            new Chart(document.getElementById("chart1"), {
                type: "pie",
                data: {
                    labels: ["Allowed", "Not Allowed"],
                    datasets: [{
                        data: [allowed, notAllowed],
                        backgroundColor: ["green", "blue"]
                    }]
                }
            });

            // BAR Chart
            new Chart(document.getElementById("chart2"), {
                type: "bar",
                data: {
                    labels: ["Allowed", "Not Allowed"],
                    datasets: [{
                        label: "Accesses",
                        data: [allowed, notAllowed],
                        backgroundColor: ["green", "blue"]
                    }]
                }
            });

            // Optional: summary text
            const summary = document.getElementById("summary-text");
            if (summary) {
                summary.textContent = `Allowed: ${allowed} | Not Allowed: ${notAllowed}`;
            }
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
