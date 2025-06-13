// Custom scripts to fix theme issues
(function($) {
    $(function() {
        // Fix for background image positioning on mobile
        // Direct override of the theme's background image handling
        
        // Delay execution to ensure the page is fully loaded
        setTimeout(function() {
            // Target the specific elements created by the theme
            var $bg = $('#bg');
            
            // If bg element exists (created by parallax)
            if ($bg.length > 0) {
                // Force left-aligned positioning
                $bg.css('background-position', '0% center');
                
                // Remove any transforms that might be repositioning the image
                $bg.css('transform', 'none');
            }
            
            // Handle direct background images (not using bg element)
            $('#intro').css('background-position', '0% center');
            $('#wrapper > .bg').css('background-position', '0% center');
            
            // Force background-size to ensure the image covers properly
            $('#intro, #wrapper > .bg, .bg').css('background-size', 'cover');
            
            // Create a mutation observer to watch for dynamically added elements
            var observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.addedNodes) {
                        for (var i = 0; i < mutation.addedNodes.length; i++) {
                            // If a new bg element is added
                            if ($(mutation.addedNodes[i]).hasClass('bg')) {
                                $(mutation.addedNodes[i]).css({
                                    'background-position': '0% center',
                                    'transform': 'none'
                                });
                            }
                        }
                    }
                });
            });
            
            // Observe the wrapper for changes
            observer.observe(document.getElementById('wrapper'), {
                childList: true,
                subtree: true
            });
        }, 100);
    });
})(jQuery);