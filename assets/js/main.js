(function($) {
  
  "use strict";  

  $(window).on('load', function() {
    /* 
   MixitUp
   ========================================================================== */
  $('#portfolio').mixItUp();

  /* 
   One Page Navigation & wow js
   ========================================================================== */
    var OnePNav = $('.onepage-nev');
    var top_offset = OnePNav.height() - -0;
    OnePNav.onePageNav({
      currentClass: 'active',
      scrollOffset: top_offset,
    });
  
  /*Page Loader active
    ========================================================*/
    $('#preloader').fadeOut();

  // Sticky Nav
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 200) {
            $('.scrolling-navbar').addClass('top-nav-collapse');
        } else {
            $('.scrolling-navbar').removeClass('top-nav-collapse');
        }
    });

    /* slicknav mobile menu active  */
    $('.mobile-menu').slicknav({
        prependTo: '.navbar-header',
        parentTag: 'liner',
        allowParentLinks: true,
        duplicate: true,
        label: '',
        closedSymbol: '<i class="icon-arrow-right"></i>',
        openedSymbol: '<i class="icon-arrow-down"></i>',
      });

      /* WOW Scroll Spy
    ========================================================*/
     var wow = new WOW({
      //disabled for mobile
        mobile: false
    });

    wow.init();

    /* Nivo Lightbox 
    ========================================================*/
    $('.lightbox').nivoLightbox({
        effect: 'fadeScale',
        keyboardNav: true,
      });

    /* Counter
    ========================================================*/
    $('.counterUp').counterUp({
     delay: 10,
     time: 1000
    });


    /* Back Top Link active
    ========================================================*/
      var offset = 200;
      var duration = 500;
      $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
          $('.back-to-top').fadeIn(400);
        } else {
          $('.back-to-top').fadeOut(400);
        }
      });

      $('.back-to-top').on('click',function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: 0
        }, 600);
        return false;
      });

  }); 
/* Resume Link active
    ========================================================*/
  $(document).on('click', '#get-resume', function() {
    window.open("https://dwebstar.auth.us-east-2.amazoncognito.com/oauth2/authorize?identity_provider=Google&redirect_uri=https://auth.dwebstar.com/authenticate&response_type=CODE&client_id=i7gqd7llbe7f2t34540q4h72m&scope=email openid profile");
  });

/* Contact Me Link
    ========================================================*/
    $(document).on('click', '#contact-me', function() {
      if (document.getElementById('contact').style.display === 'none') 
      { 
        document.getElementById('contact').style.display = 'block'; 
      } 
      else 
      { 
        document.getElementById('contact').style.display = 'none'; 
      }
      
    });

}(jQuery));
