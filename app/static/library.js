
$(document).ready(function () {
    $('#libTable').DataTable({
        "aoColumnDefs": [
            // UK date format
            { "aTargets": [2], "sType": "uk_date" }
        ]
    });
});

function toggleAdvSearch() {
    var advancedSearch = document.getElementById("advancedSearchToggle").checked;
    if (advancedSearch) {
        document.getElementById("simSearch").hidden = true;
        document.getElementById("advSearch").className = '';
    } else {
        document.getElementById("simSearch").hidden = false;
        document.getElementById("advSearch").className = 'hidden';
    }
}