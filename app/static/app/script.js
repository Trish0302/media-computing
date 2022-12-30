$('input[type="file"]').change(() => {
    $('button[type="submit"]').click()
})

currentService = $('button[type="submit"]').data("id")

if (currentService !== "") {
    document.querySelector("#" + currentService).scrollIntoView();
}



