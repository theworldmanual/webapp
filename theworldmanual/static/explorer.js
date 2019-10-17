function getHashValue(key) {
    let matches = location.hash.match(new RegExp(key+'=([^&]*)'));
    return matches ? matches[1] : null;
}

function openPage(page_id) {
    window.location = '#page=' + page_id;
    navigateToPage();
}

function navigateToPage() {
    $.ajax('/api/v1/get-page/' + getHashValue('page') + '/rendered')
        .done(function (data) {
            $('div.content').html(data);
        });
}

$(function () {
    $('.explorer-menu-collapse-btn').on('click', function (e) {
        $('.explorer-menu-collapse').toggleClass('d-none-important');
        e.preventDefault();
    });

    $('#jstree_div').jstree({
        'core': {
            'data': {
                'url': '/api/v1/get-categories/' + WORLD_ID,
            }
        },
        "plugins" : ['sort'],
    })
        .on('select_node.jstree', function (e, data) {
            let $el = $(data.event.target);

            // If world is selected -- we produce no popover
            if ($el.data('type') !== 'page') return;

            openPage(data.node.a_attr['data-page']);
        });

    navigateToPage();
});