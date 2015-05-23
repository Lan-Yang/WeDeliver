var appMaster = {

    preLoader: function(){
        imageSources = []
        $('img').each(function() {
            var sources = $(this).attr('src');
            imageSources.push(sources);
        });
        if($(imageSources).load()){
            $('.pre-loader').fadeOut('slow');
        }
    },

    smoothScroll: function() {
        // Smooth Scrolling
        $('a[href*=#]:not([href=#carousel-example-generic])').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    },

    reviewsCarousel: function() {
        // Reviews Carousel
        $('.review-filtering').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 5000
        });
    },

    screensCarousel: function() {
        // Screens Carousel
        $('.filtering').slick({
            slidesToShow: 4,
            slidesToScroll: 4,
            dots: false,
            responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2,
                    infinite: true,
                    dots: true
                }
            }, {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            }, {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }]
        });

        $('.js-filter-all').on('click', function() {
            $('.filtering').slickUnfilter();
            $('.filter a').removeClass('active');
            $(this).addClass('active');
        });

        $('.js-filter-one').on('click', function() {
            $('.filtering').slickFilter('.one');
            $('.filter a').removeClass('active');
            $(this).addClass('active');
        });

        $('.js-filter-two').on('click', function() {
            $('.filtering').slickFilter('.two');
            $('.filter a').removeClass('active');
            $(this).addClass('active');
        });

        $('.js-filter-three').on('click', function() {
            $('.filtering').slickFilter('.three');
            $('.filter a').removeClass('active');
            $(this).addClass('active');
        });

    },

    animateScript: function() {
        $('.scrollpoint.sp-effect1').waypoint(function(){$(this).toggleClass('active');$(this).toggleClass('animated fadeInLeft');},{offset:'100%'});
        $('.scrollpoint.sp-effect2').waypoint(function(){$(this).toggleClass('active');$(this).toggleClass('animated fadeInRight');},{offset:'100%'});
        $('.scrollpoint.sp-effect3').waypoint(function(){$(this).toggleClass('active');$(this).toggleClass('animated fadeInDown');},{offset:'100%'});
        $('.scrollpoint.sp-effect4').waypoint(function(){$(this).toggleClass('active');$(this).toggleClass('animated fadeIn');},{offset:'100%'});
        $('.scrollpoint.sp-effect5').waypoint(function(){$(this).toggleClass('active');$(this).toggleClass('animated fadeInUp');},{offset:'100%'});
    },

    revSlider: function() {
        var docHeight = $(window).height();
        var mainSlider = $('.tp-banner').revolution({
            delay: 9000,
            startwidth: 1170,
            startheight: docHeight,
            hideThumbs: 10,
            touchenabled: false,
            fullWidth: "on",
            hideTimerBar: "on",
            fullScreen: "on",
            onHoverStop: "off",
            fullScreenOffsetContainer: ""
        });
    },

    scrollMenu: function(){
        var num = 50; //number of pixels before modifying styles
        $(window).bind('scroll', function () {
            if ($(window).scrollTop() > num) {
                $('nav').addClass('scrolled');
            } else {
                $('nav').removeClass('scrolled');
            }
        });
    },

    placeHold: function(){
        // run Placeholdem on all elements with placeholders
        // Placeholdem(document.querySelectorAll('[placeholder]'));
    }

}; // AppMaster

$(document).ready(function() {
    appMaster.smoothScroll();
    appMaster.reviewsCarousel();
    appMaster.screensCarousel();
    appMaster.animateScript();
    appMaster.revSlider();
    appMaster.scrollMenu();
    appMaster.placeHold();
});


function urldecode(str) {
    return decodeURIComponent((str+'').replace(/\+/g, '%20'));
}

$(function() {
    /* google search modals */
    $('#place-modal').on('show.bs.modal', function(e) {
        $(this).find('.modal-content').load('/placemodal');
    });
    $('#place-modal').on('shown.bs.modal', function(e) {
        var source = e.relatedTarget;
        initGmapSearch();
        $(this).data('source', source);
        $('#pac-input').val($(source).val());
    });
    $('#place-modal').on('hide.bs.modal', function(e) {
        var source = $(this).data('source');
        var addr = $('#pac-input').data('addr');
        var latlng = $('#pac-input').data('latlng');
        if (addr) {
            $(source).val(addr);
            $(source).siblings('.addr_lat').val(latlng.lat());
            $(source).siblings('.addr_lng').val(latlng.lng());
        }
    });
});
/*
 * Initialize google map with address search modal-dialog
 * Make sure the there are div#map-canvas and input#pac-input
 */
function initGmapSearch() {
    var marker = null;
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(40.8130, -73.9625),
        new google.maps.LatLng(40.8148, -73.9567));
    map.fitBounds(defaultBounds);

    // Create the search box and link it to the UI element.
    var input = document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var searchBox = new google.maps.places.Autocomplete(input);

    google.maps.event.addListener(searchBox, 'place_changed', function() {
        var place = searchBox.getPlace();
        if (marker) { marker.setMap(null); }
        var bounds = new google.maps.LatLngBounds();

        var image = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
        };
        marker = new google.maps.Marker({
            map: map,
            icon: image,
            title: place.name,
            position: place.geometry.location
        });

        bounds.extend(place.geometry.location);
        map.fitBounds(bounds);

        // Write data back to DOM
        var _input = $(input);
        _input.data("latlng", place.geometry.location);
        _input.data("addr", place.formatted_address)
    });

    google.maps.event.addListener(map, 'bounds_changed', function() {
        var bounds = map.getBounds();
        searchBox.setBounds(bounds);
    });
}

/* logout */
function logout(next) {
    location.href = '/logout?next=' + next;
}
