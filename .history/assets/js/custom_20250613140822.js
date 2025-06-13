// Custom scripts to fix theme issues
(function($) {
    $(function() {
        // Fix for background image positioning on mobile
        if (skel.breakpoint('medium').active || skel.breakpoint('small').active) {
            // On mobile, disable parallax entirely and apply fixed positioning
            $('#intro, #wrapper > .bg').css({
                'background-attachment': 'scroll',
                'background-position': '0% 50%',
                'transform': 'none'
            });
            
            // Directly set background properties on the dynamically created .bg element
            $('.bg').css({
                'background-position': '0% 50%',
                'transform': 'none'
            });
            
            // Add resize listener to maintain positioning when screen size changes
            $(window).on('resize', function() {
                $('#intro, #wrapper > .bg, .bg').css({
                    'background-position': '0% 50%',
                    'transform': 'none'
                });
            });
        }
    });
})(jQuery);