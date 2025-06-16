// Custom scripts to fix theme issues
(function($) {
    // Log when script is loaded
    console.log('[MK Debug] Custom.js loaded');
    
    // Function to force image positioning
    function forceImagePositioning() {
        console.log('[MK Debug] Applying image positioning');
        
        // AGGRESSIVE APPROACH:
        // 1. Create a new image element with direct src to bg.jpg
        var bgImg = new Image();
        bgImg.onload = function() {
            console.log('[MK Debug] Direct BG image loaded and ready');
            
            // 2. Add inline CSS to body for a direct background image
            $('body').attr('style', 'background-image: url("/assets/images/bg.jpg") !important; background-position: 0% center !important; background-size: cover !important;');
            
            // 3. Override ALL possible backgrounds
            $('#wrapper > .bg').css({
                'backgroundImage': 'url("/assets/images/bg.jpg")',
                'backgroundPosition': '0% center',
                'backgroundSize': 'cover',
                'transform': 'none'
            });
            
            // 4. Force direct styles on wrapper
            $('#wrapper').attr('style', 'background-position: 0% center !important; background-size: cover !important;');
            
            // 5. Target any parallax-created elements
            $('.bg, #bg').css({
                'backgroundPosition': '0% center',
                'transform': 'none'
            });
            
            // 6. Add !important through attr style for maximum override
            $('.bg, #bg').attr('style', 'background-position: 0% center !important; transform: none !important;');
            
            console.log('[MK Debug] Direct styling applied');
        };
        
        // Set the source to trigger load
        bgImg.src = '/assets/images/bg.jpg';
    }
    
    // Apply immediately on load
    $(document).ready(function() {
        console.log('[MK Debug] Document ready');
        forceImagePositioning();
        
        // Apply again after a delay to catch dynamic elements
        setTimeout(forceImagePositioning, 500);
    });
    
    // Apply again if window is resized
    $(window).on('resize', function() {
        console.log('[MK Debug] Window resized');
        forceImagePositioning();
    });
    
    // Apply on scroll to catch any lazy-loaded parallax effects
    $(window).on('scroll', function() {
        // Use throttling to avoid excessive calls
        if (!window.scrollThrottleTimeout) {
            window.scrollThrottleTimeout = setTimeout(function() {
                console.log('[MK Debug] Window scrolled');
                forceImagePositioning();
                window.scrollThrottleTimeout = null;
            }, 250);
        }
    });
    
    // Also expose the function globally for debugging
    window.forceImagePositioning = forceImagePositioning;
    
})(jQuery);