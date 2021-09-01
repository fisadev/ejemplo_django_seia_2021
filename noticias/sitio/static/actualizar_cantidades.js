function pedir_nuevas_cantidades() {
    console.log("empezamos a hacer la request");

    $.ajax({
        url: "/api/cantidades/html/"
    }).done(actualizar_cantidades_html);

    $.ajax({
        url: "/api/cantidades/"
    }).done(actualizar_cantidades_json);

    console.log("request encolada!");

    setTimeout(pedir_nuevas_cantidades, 2000);
}


function actualizar_cantidades_html(data) {
    console.log("llegó la response del html! tiene esta data:");
    console.log(data);
    $("#cantidades").html(data);
}


function actualizar_cantidades_json(data) {
    console.log("llegó la response del json! tiene esta data:");
    console.log(data);
    $("#cantidad_total_json").html(data.cantidad_noticias);
    $("#cantidad_archivadas_json").html(data.cantidad_noticias_archivadas);
}


setTimeout(pedir_nuevas_cantidades, 2000);
