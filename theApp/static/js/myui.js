$(function () {
  // niceScroll
  $(function() {
    $("html").niceScroll();
  });
  /* Date Picker */
  $('.date').datepicker({
    format: "mm/dd/yyyy"
  });
  /* Google Place Search */
  // var autoComplete = [];
  $('.place').each(function(index){
    // console.log(this);
    var ap = new google.maps.places.Autocomplete(this, {types: ['geocode']});
    google.maps.event.addListener(ap, 'place_changed', function() {
      var place = ap.getPlace();
      console.log(place);
    });
    // autoComplete.push(ap);
  });
});
