// Hide submenus
$('#body-row .collapse').collapse('hide');

// Collapse/Expand icon
$('#collapse-icon').addClass('fa-angle-double-left');

// Collapse click
$('[data-toggle=sidebar-collapse]').click(function() {
    console.log('collapse');
    SidebarCollapse();
});

function SidebarCollapse () {
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');

    // Treating d-flex/d-none on separators with title
    var SeparatorTitle = $('.sidebar-separator-title');
    if ( SeparatorTitle.hasClass('d-flex') ) {
        SeparatorTitle.removeClass('d-flex');
    } else {
        SeparatorTitle.addClass('d-flex');
    }

    // Collapse/Expand icon
    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
}

$(function () {
    $('[data-toggle="tooltip"]').tooltip();

    const inputs = $('input');
    for (let i = 0; i < inputs.length; i++) {
        let initialValue = inputs[i].value;
        $(inputs[i]).on("change keydown paste input", function() {
            if (initialValue !== this.value) {
                this.classList.remove("bg-light", "text-muted", "changed");
                this.classList.add("changed");
            } else {
                this.classList.add("bg-light", "text-muted", "changed");
                this.classList.remove("changed");
            }
            if($('.changed').length) {
                $('.twm-save-button').removeAttr('disabled');
                $('.twm-save-button-hint').hide();
            } else {
                $('.twm-save-button').attr('disabled', 'disabled');
                $('.twm-save-button-hint').show();
            }
        });
    }

});