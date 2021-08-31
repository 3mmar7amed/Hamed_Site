$(document).ready( function () {
    $('#table_id').DataTable({
        'ajax':'data.json',
        "columns": [
            {'data':'color'},
            {'data':'value'}
        ]

    });
} );