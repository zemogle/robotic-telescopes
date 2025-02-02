Title: List of Telescopes  
slug: list
draft: false

    <section class="section">
        <div class="container">
            <h1 class="title">Data Table</h1>
            <table class="table is-striped is-fullwidth">
                <thead>
                    <tr>
                        <th>Facility</th>
                        <th>Instrumentaion</th>
                        <th>Waveband</th>
                        <th>Hours</th>
                    </tr>
                </thead>
                <tbody id="data-table-body">
                    <!-- Data will be inserted here -->
                </tbody>
            </table>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            fetch('theme/telescopes.json')
                .then(response => response.json())
                .then(data => {
                    const tableBody = document.getElementById('data-table-body');
                    data.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${item.facility}</td>
                            <td>${item.instrumentation}</td>
                            <td>${item.waveband}</td>
                            <td>${item.hours}</td>
                        `;
                        tableBody.appendChild(row);
                    });
                })
                .catch(error => console.error('Error fetching data:', error));
        });
    </script>