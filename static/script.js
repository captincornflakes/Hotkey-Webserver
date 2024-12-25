let statsInterval = null;

document.addEventListener("DOMContentLoaded", function () {
    const groupSelect = document.querySelector("#group-select");

    // Load the initially selected group
    loadGroup(groupSelect.value);

    // Listen for dropdown changes
    groupSelect.addEventListener("change", function () {
        const selectedGroup = groupSelect.value;
        loadGroup(selectedGroup);

        // Clear stats update interval if not "System Stats"
        if (selectedGroup !== "System Stats") {
            clearInterval(statsInterval);
            statsInterval = null;
        }
    });
});

// Load a button group or system stats
async function loadGroup(filename) {
    const response = await fetch("/load_group", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ filename: filename }),
    });
    const result = await response.json();

    if (result.status === "success") {
        if (filename === "System Stats") {
            updateStats(result.stats);
            setupStatsUpdate(); // Start periodic updates
        } else {
            updateButtons(result.config);
        }
        showAlert(`Loaded configuration: ${filename}`, "success");
    } else {
        showAlert(result.message, "danger");
    }
}

// Update the button container with buttons
function updateButtons(config) {
    const container = document.querySelector("#content-container");
    container.innerHTML = "";
    config.forEach((group) => {
        const groupDiv = document.createElement("div");
        groupDiv.className = "mb-4";
        groupDiv.innerHTML = `<h2>${group.group}</h2>`;
        const rowDiv = document.createElement("div");
        rowDiv.className = "row";
        group.buttons.forEach((button) => {
            const colDiv = document.createElement("div");
            colDiv.className = "col-auto mb-3";
            colDiv.innerHTML = `
                <button class="btn btn-${button.color} narrow-button" onclick="pressKey('${button.hotkey}')">
                    ${button.label}
                </button>
            `;
            rowDiv.appendChild(colDiv);
        });
        groupDiv.appendChild(rowDiv);
        container.appendChild(groupDiv);
    });
}

// Update the button container with system stats
function updateStats(stats) {
    const container = document.querySelector("#content-container");
    container.innerHTML = `<h2>System Stats</h2>`;
    let table = `
        <table class="table table-dark table-striped">
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
    `;
    for (const [key, value] of Object.entries(stats)) {
        table += `
            <tr>
                <td>${key}</td>
                <td>${value}</td>
            </tr>
        `;
    }
    table += "</tbody></table>";
    container.innerHTML += table;
}


// Set up periodic updates for system stats
function setupStatsUpdate() {
    if (statsInterval) clearInterval(statsInterval); // Clear existing interval
    statsInterval = setInterval(async () => {
        const response = await fetch("/load_group", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ filename: "System Stats" }),
        });
        const result = await response.json();
        if (result.status === "success") {
            updateStats(result.stats);
        }
    }, 60000); // Update every minute
}

// Simulate a key press
async function pressKey(hotkey) {
    const response = await fetch("/press", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hotkey: hotkey }),
    });
    const result = await response.json();
    showAlert(result.message, result.status === "success" ? "success" : "danger");
}

// Show an alert for user feedback
function showAlert(message, type) {
    const alertContainer = document.querySelector(".alert-container");
    const alert = document.createElement("div");
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        <strong>${type === "success" ? "Success!" : "Error!"}</strong> ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    alertContainer.appendChild(alert);
    setTimeout(() => alert.remove(), 3000);
}
