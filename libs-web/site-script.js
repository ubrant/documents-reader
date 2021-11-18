(function () {
    'use strict'

    // Tooltip and popover
    document.querySelectorAll('.tooltip-demo')
        .forEach(function (tooltip) {
            new bootstrap.Tooltip(tooltip, {
                selector: '[data-bs-toggle="tooltip"]'
            })
        })

    document.querySelectorAll('[data-bs-toggle="popover"]')
        .forEach(function (popover) {
            new bootstrap.Popover(popover)
        })

    document.querySelectorAll('.toast')
        .forEach(function (toastNode) {
            var toast = new bootstrap.Toast(toastNode, {
                autohide: false
            })

            toast.show()
        })

    // Disable empty links and submit buttons
    document.querySelectorAll('[href="#"], [type="submit"]')
        .forEach(function (link) {
            link.addEventListener('click', function (event) {
                event.preventDefault()
            })
        })

    function setActiveItem() {
        var ids = $('meta[name="ubrant-ids"]')
        var majorId = ids.attr("major-id")
        var minorId = ids.attr("minor-id")
        var sectionId = ids.attr("section-id")
        var pageId = ids.attr("page-id")

        console.log("ID = ", majorId, minorId, sectionId, pageId);

        var major = $("#Major" + majorId)
        var minor = $("#Minor" + minorId)
        var section = $("#Section" + sectionId)
        //Page-@MajorID-@MinorID-@SectionID-@PageID
        var page = $("#Page-" + majorId + "-" + minorId + "-" + sectionId + "-" + pageId)

        if (!major) return
        if (!minor) return
        if (!section) return
        if (!page) return

        major.prev().click()
        minor.prev().click()
        section.prev().click()

        page.addClass('focus')
    }

    setActiveItem()

    // Hide blank Question options
    $(".card .form-check label").each(function(i){
        var text = $(this).text().trim()
        if (!text) $(this).parent().hide();
    })
})()