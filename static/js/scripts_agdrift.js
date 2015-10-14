$(document).ready(function () {
    $('#id_boom_height').closest('tr').hide();
    $('#id_orchard_type').closest('tr').hide();
    $('#id_drop_size').closest('tr').hide();

    $("#id_ecosystem_type option[value='Terrestrial']").prop('disabled',true);
    $("#id_calculation_input option[value='Fraction']").prop('disabled',true);
    $("#id_calculation_input option[value*='Initial Average']").prop('disabled',true);
    $("#id_orchard_type option[value='Normal']").prop('disabled',true);
    $("#id_orchard_type option[value='Dense']").prop('disabled',true);
    $("#id_orchard_type option[value='Sparse']").prop('disabled',true);

    $('#id_application_method').change(function () {
        if ($(this).val() == "Ground") {
            $('#id_boom_height').closest('tr').show();
            $('#id_orchard_type').closest('tr').hide();
            $('#id_drop_size').closest('tr').show();
            $('#id_drop_size').find('option:eq(3)').detach();
            // $('#id_drop_size').find('option:eq(4)').hide();
        }
          else if ($(this).val() == "Aerial") {
            $('#id_boom_height').closest('tr').hide();
            $('#id_orchard_type').closest('tr').hide();
            $('#id_drop_size').closest('tr').show();
        } 
        else if ($(this).val() == "Orchard/Airblast") {
            $('#id_boom_height').closest('tr').hide();
            $('#id_drop_size').closest('tr').hide();
            $('#id_orchard_type').closest('tr').show();
            }
    
    });

    $(window).bind('beforeunload', function () {
        $(":reset").click();
    });
});