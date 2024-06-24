document.addEventListener('DOMContentLoaded', function() {
    console.log("Script loaded");

    const baseURL = "";  // Set your base URL here if necessary

    let columns, regions;

    // Function to populate dropdown options
    function populateDropdown(selector, data) {
        const dropdown = d3.select(selector);
        dropdown.selectAll('option').remove(); // Clear existing options

        data.forEach(item => {
            dropdown.append('option')
                .attr('value', item)
                .text(item);
        });
    }

    // Fetch all columns and populate dropdown on page load
    d3.json(baseURL + "/api/allcolumns")
        .then(function(data) {
            columns = data;
            console.log("Columns:", columns);
            populateDropdown("#selDataset", columns);
        })
        .catch(function(error) {
            console.error("Error fetching columns:", error);
        });

    // Fetch region names and populate dropdown on page load
    d3.json(baseURL + "/api/regionnames")
        .then(function(data) {
            regions = data;
            console.log("Regions:", regions);
            populateDropdown("#selRegion", regions);
        })
        .catch(function(error) {
            console.error("Error fetching regions:", error);
        });

    // Function to handle column dropdown change
    function optionChanged(column) {
        console.log("Selected column:", column);
        // Fetch data for the selected column
        d3.json(baseURL + `/api/pricecut/${column}`)
            .then(function(data) {
                console.log("Column data:", data);
                const cardBody = d3.select("#sample-metadata");
                cardBody.html(""); // Clear previous content

                cardBody.append("p").html(data.message);
                cardBody.append("p").html(`RegionName: ${data.RegionName}`);
                if (data.StateName) {
                    cardBody.append("p").html(`StateName: ${data.StateName}`);
                }
            })
            .catch(function(error) {
                console.error("Error fetching price cut data:", error);
            });
    }

    // Function to handle region dropdown change
    function regionChanged(region) {
        console.log("Selected region:", region);
        // Fetch plot for the selected region
        d3.json(baseURL + `/api/plot/${region}`)
            .then(function(data) {
                console.log("Plot data:", data);
                d3.select(".plot-container").html(`<img src="data:image/png;base64,${data.plot_url}" alt="Plot"/>`);
            })
            .catch(function(error) {
                console.error("Error fetching plot data:", error);
            });
    }

    // Event listeners for dropdown changes
    document.getElementById("selDataset").addEventListener("change", function() {
        optionChanged(this.value);
    });

    document.getElementById("selRegion").addEventListener("change", function() {
        regionChanged(this.value);
    });

    // Load initial heatmap on page load
    d3.json(baseURL + "/api/heatmap")
        .then(function(data) {
            console.log("Heatmap data:", data);
            const heatmapPath = data.heatmap_path;
            d3.select("#map .map-container").html(`<iframe src="${heatmapPath}" width="100%" height="600px" frameborder="0"></iframe>`);
        })
        .catch(function(error) {
            console.error("Error fetching heatmap data:", error);
        });
});
