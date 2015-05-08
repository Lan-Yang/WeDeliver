$(function () {
  /* niceScroll */
  $("html").niceScroll();
  /* popover tooltip */
  $('[data-toggle="tooltip"]').each(function(){
    var title = $(this).attr("placeholder");
    $(this).attr("title", title).tooltip();
  });
  /* Date Picker */
  $('.date').datepicker({
    format: "mm/dd/yyyy"
  });
  /* Google Place Search */
  $('.place').each(function(index){
    // console.log(this);
    var ap = new google.maps.places.Autocomplete(this, {types: ['geocode']});
    google.maps.event.addListener(ap, 'place_changed', function() {
      var place = ap.getPlace();
      console.log(place);
    });
  });
});
