
function prisao(frm, url){

    path = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');
    $.ajax({
    	url: path + url,
        type: 'post',
        dataType: 'json',
        data: frm.serialize(),
        success: function (response, textStatus, xhr) {

			if(response.success){

                $('#presos_livres').html(response.presos_livres_html);
                $('#soltar_presos').html(response.soltar_presos_html);
                $('#tb_presos').html(response.presos_html);
                $('#alerta').html('');

                $('input[name=prender]').val('');
                $('input[name=soltar]').val('');
			}
			else{
			    $('#alerta').html(response.msg);
			}
        },
        error : function(jqXHR, textStatus, errorThrown){
            alert('error: ' + textStatus + errorThrown);
        }
    });
}

function atualizar() {

    path = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');

    $.ajax({
        url: path + '/atualizar/',
        type: 'get',
        dataType: 'json',
        success: function (response, textStatus, xhr) {

            if(response.success){

                $('#presos_livres').html(response.presos_livres_html);
                $('#soltar_presos').html(response.soltar_presos_html);
                $('#tb_presos').html(response.presos_html);
            }
        },
        error : function(jqXHR, textStatus, errorThrown){
            alert('error: ' + textStatus + errorThrown);
        }
    });
}

$(document).ready(function(){
    path = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');

    $('#form_prender').submit( function() {
        var frm = $('#form_prender');
        prisao(frm, '/prender/');

        return false;
    });

    $('#form_soltar').submit( function() {
        var frm = $('#form_soltar');
        prisao(frm, '/soltar/');

        return false;
    });

    window.setInterval(function() {
        atualizar()
    }, 10000);
});